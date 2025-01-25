from tinydb import TinyDB


db = TinyDB("db.json")

user = {
    'lastname': 'Elmurodov','name': 'Ziyodullo', 'age': 20 , 'job': 'student'
    }


user2 = {'lastname': 'Mamarajabov','name': 'Dilmurod', 'age': 22 , 'job': 'student'}

user3 = {'lastname': 'Odil','name': 'Kamronbek', 'age': 19 , 'job': 'engineer'}

user4 = {'lastname': 'Nuraliyev','name': 'Akobir', 'age': 15 , 'job': 'student'}

user5 = {'lastname': 'Aliyev','name': 'Qodir', 'age': 32 , 'job': 'teacher'}

db.insert_multiple([user,user2,user3,user4,user5])