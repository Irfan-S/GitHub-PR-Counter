import requests
import json
data = ["egoist", "andrew"]
res = requests.post("http://127.0.0.1:5000/api/prs/users/all", data=json.dumps(data))
print(res.json())