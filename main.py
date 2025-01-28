from tinydb import TinyDB
from tinydb.table import Document

db = TinyDB("db.json")
user1 = {"lastname":"Mamarajabov","name":"Dilmurod","age":21,"job":"student"}
user2 = {"lastnema":"Elmurodov","name":"Ziyodullo","age":20,"job":"student"}
db.insert_multiple([user1, user2])
