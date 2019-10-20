# Built by Irfan S for ACM HacktoberFest '19.
# Under guidance of Amit Jha.

import flask
from github import Github
import requests
import json
import sqlite3
from flask import jsonify, request
from collections import OrderedDict

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# TODO Enter a single username/password combination to access the GitHub API.
username = ""
token = ""

# TODO Edit the start and end dates to filter out PR's for a particular time range
start_date = "2000-09-30T10%3A00%3A00%2B00%3A00"  # start date
end_date = "2019-10-01T12%3A00%3A00%2B00%3A00"  # end date

gh_session = requests.Session()
gh_session.auth = (username, token)
pullreq_dict = {}

# we can use raw_input() to ask for a username, or feed in a list. Input needs to be handled
# Since it's running on a server, we can create a list , and append new inputs to it?


def get_users_data(users):
    global gh_session
    global pullreq_dict
    for u_name in users:
        repos_url = 'https://api.github.com/search/issues?q=-label:invalid+created:' + \
            start_date + ".." + end_date + '+type:pr+is:public+author:'+u_name+'&per_page=300'

        json_obj = json.loads(gh_session.get(repos_url).text)

        # Each dict key is mapped to another dict wrapped by a list.
        if(not json_obj.get("message") == 'Validation Failed'):
            pullreq_dict[u_name] = []
            for item in json_obj.get("items"):
                pullreq_dict[u_name].append({"pr-number:": item.get("number"), "html_url": item.get(
                    "html_url"), "title": item.get("title"), "body": item.get("body"), "state": item.get("state")})


@app.route('/', methods=['GET'])
def home():
    return "<h1>Home page for PR counter</h1><p>This site is an API end point for getting the no. of pull requests made by a specific user.</p><br><ul><li>Use /api/prs/users/all to get PR details of all users in the username list</li><li>Use /api/prs/users/top10 to get top 10 users and their PR count </li></ul><br><p>Built by Irfan S</p>"


@app.route('/api/prs/users/all', methods=['POST'])
def api_get_users():
    users_list = json.loads(request.data)
    get_users_data(users_list)
    return jsonify(pullreq_dict)


@app.route('/api/prs/users/top10', methods=["GET"])
def api_top10():
    sorted_dict = OrderedDict(
        sorted(pullreq_dict.items(), key=lambda x: len(x[1]), reverse=True))
    top10 = {}
    i = 0
    for item in sorted_dict:
        if(i < 10):
            top10[item] = sorted_dict[item]
            i += 1
        else:
            break

    top10 = dict(OrderedDict(
        sorted(top10.items(), key=lambda x: len(x[1]), reverse=True)))
    top10_list = []
    for item in top10.items():
        # Console logging.
        print("Name: " + item[0]+" -> No. of commits: " + str(len(item[1])))

        top10_list.append({'Name': item[0], "PRs": len(item[1])})

    # Return a list of 10 10, with a dictonary inside each element for name and pr pairs
    return jsonify(top10_list)

    # To return the top10 dictonary
    # return jsonify(top10)


app.run()
