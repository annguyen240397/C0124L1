test = ["a","b","c","d","e"]
test2 = ["f","g"]
test.append("f")
print(test)
test.insert(2,"f")
print(test)
test.extend(test2)
print(test)
test3 = test + test2
print(test3)