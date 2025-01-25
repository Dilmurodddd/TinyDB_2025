from tinydb import TinyDB
from tinydb.table import Document

db = TinyDB("db.json")

user = Document({
    'lastname': 'Elmurodov',
    'name': 'Ziyodullo',
    'age': 20,
    'job': 'student'
}, doc_id=10)

db.insert(user)