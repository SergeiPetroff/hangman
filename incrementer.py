def incrementer():
    i = 1
    while True:
        yield i
        i +=1

inc = incrementer()

for i in range(3):
    print(next(inc))
