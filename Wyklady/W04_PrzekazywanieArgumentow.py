
def f(x):
    x = x+1
    print(f"Wartość x w funkcji f: {x}")
    print(f"id(x) w funkcji f: {id(x)}")

def g(x):
    x[0] = 10
    print(f"Wartość argumentu x w funkcji f: {x}")
    print(f"id(x) w funkcji g: {id(x)}")

"""
Poniższy przykład częściowo za Zingaro ,,Learn to Code by Solving Problems''

"""
def co_zwroci_mystery():

    def mystery1(s, lst):
        s = s.upper()
        lst = lst + [2]
        print(f"mystery1: ", s, lst)

    s = 'a'
    lst = [1]
    print(f"przed mystery1: ", s, lst)
    mystery1(s, lst)
    print(f"po mystery1: ", s, lst)

    def mystery2(s, lst):
        s.upper()
        lst.append(2)
        print(f"mystery2: ", s, lst)

    print(f"przed mystery2: ", s, lst)
    mystery2(s, lst)
    print(f"po mystery2: ", s, lst)
def main():
    x = 10
    print(f"Wartość x przed wykonaniem funkcji f: {x}")
    print(f"id(x) przed wykonaniem funkcji f: {id(x)}")
    f(x)
    print(f"Wartość x po wykonaniu funkcji f: {x}")
    print(f"id(x) po wykonaniu funkcji f: {id(x)}")
    print("")

    y = [0, 1, 2]
    print(f"Wartość y przed wykonaniem funkcji g: {y}")
    print(f"id(y) przed wykonaniem funkcji f: {id(y)}")
    g(y)
    print(f"Wartość y po wykonaniu funkcji g: {y}")
    print(f"id(y) po wykonaniu funkcji g: {id(y)}")

    print("")
    print("Jeszcze jeden przykład: co zwroci mystery?")
    co_zwroci_mystery()

if __name__ == "__main__":
    main()