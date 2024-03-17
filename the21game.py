import random as r

def the21():
    diem = 0
    while True:
        if r.randint(0,1) == 0:
            player = "Human"
            print("Human choi dau tien")
            break
        else:
            player = "Computer"
            print("Computer choi dau tien")
            break
    while diem < 21:
        if player == "Human":
            print("Diem so hien tai la: ",diem)
            player_choice=0
            player_choice=input("Nguoi choi hay nhap gia tri tu 1 den 3: ")
            while True:
                if int(player_choice) in [1,2,3]:
                    diem = diem + int(player_choice)
                    break
                else:
                    break
            if diem >= 21:
                print("Nguoi choi da thua")
            else:
                player = "Computer"
        else:
            print("Diem so hien tai la: ",diem)
            a=r.randint(1,3)
            print("May chon: ",a)
            diem = diem + a
            if diem >=21:
                print("Nguoi choi da thang")
            else:
                player = "Human"
the21()
while True:
    again = input("Ban co muon tiep tuc choi khong? Nhap y de tiep tuc.")
    if again == "y":
        the21()
    else:
        break