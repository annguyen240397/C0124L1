a = float(input("Nhap gia tri cua a: "))
b = float(input("Nhap gia tri cua b: "))
c = float(input("Nhap gia tri cua c: "))
if a == b and a == c :
    print("ca 3 so bang nhau va bang {}".format(a))
elif a>=b and a>=c :
    print("So lon nhat la {}".format(a))
elif b>=a and b>=c :
    print("So lon nhat la {}".format(b))
elif c>=a and c>=b :
    print("So lon nhat la {}".format(c))
else :
    print("Gia tri nhap vao khong hop le")
