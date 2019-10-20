import requests
import json
data = ["darshildave", "tourist"]
res = requests.get("http://127.0.0.1:5000/api/prs/users/top10", data=json.dumps(data))
print(res.json())