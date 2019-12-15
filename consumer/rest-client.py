import requests

# NOTE: 先從 Registry 得知 有哪些 Services
# 再根據這些 Services 的 Definition 拿到該服務的資訊
# 組合這些服務並 即可快速變更企業流程！
res = requests.get("http://localhost:8001/api/inventory/")
print(res.json()["inventory"])
