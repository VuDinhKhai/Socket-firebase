from PIL import Image


with open("D:/vscode/code Python/truyen_nhan_tin/Doremon.jpg",'rb') as f:
            im = Image.open(f)
            im.show()
            f.read()
            print(im)
            #client.send(f.read())
            f.close