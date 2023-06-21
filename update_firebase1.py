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

#db.child("khai").child("khai1").child("khai2").child("khai's info").update({"age": 50})
#data={"khai/khai1/khai2":{"khai3":40},"khai":{"age" : 20}}
data={"khai/khai1/khai2":{"khai3":40}}
db.update(data)

#lấy khoá
khoa_stack= db.child("the").child("the1").get()
for tack in khoa_stack.each():
    #print(tack.val())
    #print(tack.key())
    if(tack.val()=="dep trai"):
        key=tack.key()

db.child("the").child("the1").update({key:"xinh gai"})