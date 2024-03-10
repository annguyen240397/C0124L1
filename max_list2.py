n = int(input('Nhap so phan tu cua danh sach: '))
a = []
max = 0
max2 = 0
for i in range(n):
    temp = int(input('Nhap phan tu danh sach: '))
    a.append(temp)
print(a)
for i in range(1, n):
    if a[i] > max:
        max2 = max
        max = a[i]
print(max2)