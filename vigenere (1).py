import cv2
import numpy as np

MAX_LEN_IMG = 10

def generateKey(len_str, key): # len_str = Độ dài key cần tạo(int), key(string) => return key được lặp lại (string)
    key = list(key)
    if len_str == len(key):
        return(key)
    else:
        for i in range(len_str - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     
# TEXT
def cipherText(string, key): # Mã hóa text
    cipher_text = []
    key = generateKey(len(string), key)
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 256
        # x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

def decryptedText(cipher_text, key): # Giải mã text
    decry_text = []
    key = generateKey(len(cipher_text), key)
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 256) % 256
        # x += ord('A')
        decry_text.append(chr(x))
    return("" . join(decry_text))


# IMAGE
def num_to_arr(num): # chuyển số thành mảng 1 chiều có MAX_LEN_IMG phần tử
    arr = np.array([])
    for i in range(MAX_LEN_IMG):
        arr = np.insert(arr,0,num%10)
        num = num//10
    arr = arr.astype(int)
    return arr

def arr_to_num(arr): # Chuyển mảng về số
    num = 0
    for i in range(MAX_LEN_IMG):
        num+= arr[MAX_LEN_IMG-i-1] * 10 ** (i)
    return num

def formatImg(img):                                     # Chuyển ảnh sang vector
    img_format = np.array([len(img.shape),MAX_LEN_IMG])  # ô 0 lưu số chiều, ô 1 lưu độ dài tối đa của 1 độ dài ảnh        
                                                               
    for i in range(img_format[0]):
        conv_num = num_to_arr(img.shape[i])
        img_format = np.append(img_format, conv_num)   # (3*MAX_LEN_IMG) ô tiếp theo lưu cỡ của ảnh
    
    img_vector = np.reshape(img,-1)
    img_format = np.append(img_format, img)
    return img_format.astype(np.uint8)

def resImg(img):                                    # Chuyển từ vector về ảnh 
    dim = img[0]
    max_len = img[1]
    res_num = []
    for i in range(1,dim):
        res_num.append(arr_to_num(img[i*10+2 : i*10+12]))
    img_res = np.array(img[2+dim*max_len : ])
    res_num.insert(0,-1)
    img_res = np.reshape(img_res , res_num)
    return img_res.astype(np.uint8)

def encodeImg(img, key):    # img = Array của numpy , key(string) bất kì
    print("Proceed to encode the image...")
    format = formatImg(img)
    key = generateKey(format.size, key)
    cip = []
    for i in range(format.size):
        x =  (format[i] + ord(key[i]) ) % 256
        cip.append(chr(x))
        if(i%100000 == 0) : print(i,'/',format.size)
    print("Done")
    return ("".join(cip))

def decodeImg(img, key): # img = string, key của encodeImg
    print("Proceed to decode the image...")
    key = generateKey(len(img), key)
    dec = []
    for i in range(len(img)):
        x =  (ord(img[i]) - ord(key[i]) + 256) % 256
        dec.append(x)
        if(i%100000 == 0) : print(i,'/',len(img))
    print("Done")
    print(dec)
    return resImg(dec)

# file_img = cv2.imread('C:\\Users\\admin\\Desktop\\Temp\\pixel.png')

# text = open('test.txt', 'w+')

# img = np.array(file_img)

# en_img = encodeImg(img,"ThisIsKey")
# text.write(en_img)
# de_img = decodeImg(en_img,"ThisIsKey")
while 1:
    print("---------------------------------------"+
            "\n1. Text\n2. Image\n3. Exit\n>>",end ="")
    evt = int(input())
    
    if evt == 1:

        print("Input text: ",end="")
        text = input()

        print("Key: ",end="")
        key = input()

        cip = cipherText(text,key)

        print("Encode: ",cip)
        print("Decode: ",decryptedText(cip,key))
    elif evt == 2:

        print("Path: ",end="")
        path = input()

        file_img = cv2.imread(path)
        img = np.array(file_img)

        print("Key: ",end="")
        key = input()

        cip = encodeImg(img,key)

        print("(*)Encode: ",cip)
        print("Size of encrypted string: ", len(cip))
        de = decodeImg(cip,key)
        print("(*)Decode: ", de)
        print("Size of the decoded string ", de.shape)
        cv2.imshow("Image after decoding",de)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif evt == 3:
        break
    else:
        continue

# cv2.imshow("abc",de_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# text.close()


