a = float(input("Nhap gia tri cua a: "))
b = float(input("Nhap gia tri cua b: "))
if a==0 :
    if b==0 :
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghien")
else:
    x=-b/a
    print("Nghiem cua phuong trinh la {x}".format(x=x))