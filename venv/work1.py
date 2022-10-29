
def truk(a,b):
    try:
        for i in range (0, a):
            for j in range(0, b):
                print('*',end= " ")
            print()
        print()

    except Exception as ex:
        print(f"error information:{ex}")


truk(2, 7)