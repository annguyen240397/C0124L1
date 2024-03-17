n=input("Hay nhap 2 so bat ki: ")
n1 = n.split()
a= int(n1[0])
b= int(n1[1])
for i in range(a,b,1):
    if i % 3 == 0 and i % 5 !=0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 !=0:
        print("Buzz")
    elif i % 3 ==0 and i % 5 ==0:
        print("FizzBuzz")
    else:
        print(i)