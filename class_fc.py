import random
class flashcard:
    def __init__(self):
        self.animals = {
            'con ong': 'bee',
            'con tho' : 'rabbit',
            'con cua' : 'crab',
            'con meo' : 'cat',
            'con ngua' : 'horse',
            'con khi' : 'monkey',
            'con lua' : 'donkey'
        }
    def quiz(self):
        while True:

            vietnamese, english = random.choice(list(self.animals.items()))

            print("Tiếng Anh của '{}' là: ".format(vietnamese))
            user_answer = input()

            if user_answer.lower() == english:
                print("Đúng")
            else:
                print("Sai")

            option = int(input("Nhập 0 để tiếp tục : "))
            if option:
                break
        print("Kết thúc")
fc = flashcard()
fc.quiz()