dem = 0
while dem<31 :
    for i in range(1,210,1):
        if i % 7 == 0:
            print(i)
            dem +=1
print(dem)