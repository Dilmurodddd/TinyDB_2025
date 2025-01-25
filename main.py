from tinydb import TinyDB


db = TinyDB("db.json")

user = {
    'lastname': 'Elmurodov','name': 'Ziyodullo', 'age': 20 , 'job': 'student'
    }

db.insert(user)