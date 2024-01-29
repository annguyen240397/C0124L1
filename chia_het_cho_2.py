import math
a = int(input('Nhap gia tri: '))
if a == 0 :
    print("Khong xac dinh duoc so chan hay so le")
else :
    if a % 2 == 0 :
        print("{a} la so chan.".format(a=a))
    else :
        print("{a} la so le. ".format(a=a))
###toan tu 3 ngoi
print("day la so chan") if a % 2 == 0 else print("day la so le")
