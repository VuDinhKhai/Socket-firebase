import pyrebase

firebaseConfig = {"apiKey": "AIzaSyCVLMAQV45E7kF6bcAQSPmVBT4g0e7YwFo",
    "authDomain": "bai1-66ccc.firebaseapp.com",
    "projectId": "bai1-66ccc",
    "storageBucket": "bai1-66ccc.appspot.com",
    "messagingSenderId": "885923323932",
    "appId": "1:885923323932:web:074d2b93a69fcea68fffd9",
    "measurementId": "G-L3B9DCD9ZV",
    "databaseURL": "https://bai1-66ccc.appspot.com/"}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

path_on_cloud= "images"
path_local = "D:/vscode/code Python/truyen_nhan_tin/the.jpg"

#storage.child(path_on_cloud).put(path_local)
#storage.child(path_on_cloud).download("D:/vscode/code Python/truyen_nhan_tin/anh_the.jpg")
##storage.child(path_on_cloud).get_url()

path_on_cloud1="file1/baitap"
path_local1="C:/Users/DELL/Downloads/Vũ Đình Khải - 20192927- 713530.pdf"
#storage.child(path_on_cloud1).put("C:/Users/DELL/Downloads/Vũ Đình Khải - 20192927- 713530.pdf")
storage.child(path_on_cloud1).download("D:/anhthe/filepdf.pdf")
