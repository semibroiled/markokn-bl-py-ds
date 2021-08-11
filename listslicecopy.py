while True:
    list = [i for i in range(10)]
    print(list)
    a= list[:]
    print(a)
    a[0] = 100
    print(a, list)



