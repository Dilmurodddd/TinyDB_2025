from tinydb import TinyDB
from tinydb.table import Document
import requests

db = TinyDB("random.json")

shop = TinyDB("shop.json")


shopbase = {
    'samsung': [
        {'model': 'Galaxy S23 Ultra', 'memory': '512 GB', 'cost': '1.399$'},
        {'model': 'Galaxy Z Fold 5', 'memory': '1TB', 'cost': '1.799$'},
        {'model': 'Galaxy A54', 'memory': '128 GB', 'cost': '499$'}
    ],
    'iphone': [
        {'model': 'iPhone 15 Pro Max', 'memory': '1TB', 'cost': '1.599$'},
        {'model': 'iPhone 14 Pro', 'memory': '256 GB', 'cost': '1.199$'},
        {'model': 'iPhone SE (2023)', 'memory': '128 GB', 'cost': '599$'}
    ],
    'xiaomi': [
        {'model': 'Redmi Note 13 Pro', 'memory': '256 GB', 'cost': '399$'},
        {'model': 'Mi 13 Ultra', 'memory': '512 GB', 'cost': '899$'},
        {'model': 'Poco X5 Pro', 'memory': '128 GB', 'cost': '349$'}
    ]
}


shop.insert(shopbase)

url ="https://randommer.io/api/Name?nameType=firstname&quantity=10"

headers = {
    'X-Api-Key':"b9684522e39c47ab9cd0a655122028a5"
}

response = requests.get(url,headers=headers).json()



for  i in response:
    db.insert({"fulname":f"{i}"})