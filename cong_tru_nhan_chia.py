def cong(a,b):
    return a+b
def tru(a,b):
    return a-b
def nhan(a,b):
    return a*b
def chia(a,b):
    return a/b
phep_tinh=input("Hay nhap phep tinh: ")
a=int(input("Nhap gia tri cua a: "))
b=int(input("Nhap gia tri cua b: "))
if phep_tinh == "+" :
    print(cong(a,b))
elif phep_tinh == "-" :
    print(tru(a,b))
elif phep_tinh == "*" :
    print(nhan(a,b))
elif phep_tinh == "/" :
    print(chia(a,b))
else:
    print("Khong the thuc hien phep tinh nay")