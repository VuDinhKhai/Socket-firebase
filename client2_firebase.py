import pyrebase

firebaseConfig = {"apiKey": "AIzaSyCVLMAQV45E7kF6bcAQSPmVBT4g0e7YwFo",
    "authDomain": "bai1-66ccc.firebaseapp.com",
    "projectId": "bai1-66ccc",
    "storageBucket": "bai1-66ccc.appspot.com",
    "messagingSenderId": "885923323932",
    "appId": "1:885923323932:web:074d2b93a69fcea68fffd9",
    "measurementId": "G-L3B9DCD9ZV",
    "databaseURL": "https://bai1-66ccc-default-rtdb.firebaseio.com/"}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

# chat=db.child("duy").get()
# print(chat.key(), " : ",chat.val())

# data=str(input())
# db.update({"khai":data})

db = firebase.database()
print("nhap ten cua ban:",end="")
Ten=str(input())
print("Nhap ten nguoi ban muon chat: ",end="")
Client=str(input())
chat1=""
while True:
    while (db.child(Client).get()).val()!=chat1:
        print((db.child(Client).get()).key(), " : ",(db.child(Client).get()).val())
        chat1=(db.child(Client).get()).val()
        print(Ten ," :" , end="")
        data=str(input())
        db.update({Ten:data})
    if data=="Quit":
        break