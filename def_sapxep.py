a = int(input('Hay nhap so nguyen thu nhat: '))
b = int(input('Hay nhap so nguyen thu hai: '))
c = int(input('Hay nhap so nguyen thu ba: '))

def sapxep(a,b,c):
    d=0
    if b<a and b<c:
        d=a
        a=b
        b=d
    elif c<a and c<b:
        d=a
        a=c
        c=d
    if c<b:
        d=b
        b=c
        c=d
    return a,b,c
x,y,z= sapxep(a,b,c)
print('3 so ban dau la: ', a, b, c)
print('3 so sap xep theo thu tu tang dan la: ', x, y, z)