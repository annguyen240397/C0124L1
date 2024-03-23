n = int(input('Nhap so phan tu cua danh sach: '))
a = []
for i in range(n):
    temp = int(input('Nhap phan tu danh sach: '))
    a.append(temp)

max2=0
def tim_min(a):
    result = a[0]
    for num in a:
        if result < num:
            max2 = result
            result = num
    print('So lon nhat la: ',result)
    print('So lon thu hai la: ',max2)
tim_min(a)