import may_tinh
phep_tinh=input("Hay nhap phep tinh: ")
a=int(input("Nhap gia tri cua a: "))
b=int(input("Nhap gia tri cua b: "))
if phep_tinh == "+" :
    print(may_tinh.cong(a,b))
elif phep_tinh == "-" :
    print(may_tinh.tru(a,b))
elif phep_tinh == "*" :
    print(may_tinh.nhan(a,b))
elif phep_tinh == "/" :
    print(may_tinh.chia(a,b))
else:
    print("Khong the thuc hien phep tinh nay")