
try:
    def truk(a,b):
        for i in range (0, a):
            for j in range(0, b):
                print('*',end= "")
            print()
        print()
    print(truk)

except Exception as ex:
    print(f"error information:{ex}")
finally:
    print("exit")