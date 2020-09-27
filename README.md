A Python REST API to fetch the number of pull requests made by a list of GitHub users. Runs on the Flask framework. Used by PESU-ECC for Hacktoberfest '19.

How to use:
- Enter your username and password, in the 'username' and 'token' variables to access the GitHub API
- Edit the start and end dates accordingly.
- Provide a list of usernames to 'u_name_list'. Will add a POST method to push the list via REST in the future.

Endpoints:
- http://127.0.0.1:5000/api/v1/prs/users/top10 -> used to get a JSON object of a list of the top 10 users with their usernames and number of PRs. You can also return the dict object which contains details of their PRs.

- http://127.0.0.1:5000/api/v1/prs/users/all -> returns a JSON object which contains a dict of all the usernames provided.

Dictionary attributes:
Key - username
Value -> list consisting of a Dictionary with the following keys.
- pr-number -> the unique PR number of the issue
- html-url -> link to the PR request
- title -> title of the PR
- body -> body text of PR
- state -> whether PR is open or closed

How to deploy:
- install flask using pip
- Navigate to the api.py file
- Run this command
    python3.6 api.py
- Link will be displayed in the console.











Built by Irfan S and Amit Jha
