from tinydb import TinyDB
from tinydb.table import Document

db = TinyDB("db.json")

user = Document({
    'lastname': 'Elmurodov',
    'name': 'Ziyodullo',
    'age': 20,
    'job': 'student'
}, doc_id=10)

print(db.all())

print(db.contains(doc_id=10))
print(db.contains(doc_id=10))
print(db.get(doc_id=10))
print(db.get(doc_id=1))