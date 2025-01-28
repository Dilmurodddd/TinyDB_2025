from tinydb import TinyDB
from tinydb.table import Document
import requests

db = TinyDB("random.json")




url ="https://randommer.io/api/Name?nameType=firstname&quantity=10"

headers = {
    'X-Api-Key':"b9684522e39c47ab9cd0a655122028a5"
}

response = requests.get(url,headers=headers).json()



for  i in response:
    db.insert({"fulname":f"{i}"})