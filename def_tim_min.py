n = int(input('Nhap so phan tu cua danh sach: '))
a = []
for i in range(n):
    temp = int(input('Nhap phan tu danh sach: '))
    a.append(temp)

def tim_min(a):
    result = a[0]
    for num in a:
        if result > num:
            result = num
    return result
min = tim_min(a)
print('Min number: ',min)