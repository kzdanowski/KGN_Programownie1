from importlib import reload 

zmienna_globalna = 10
inna_zmienna_globalna = 20

def function_example(x):
    """This is an example of a doc string."""
    return x*x


def zmiana_argumentu(x, y):
    x = y
    print("Wewnątrz funkcji x =", x)

def zmiana_elementu(x,y):
    x[0] = y
    print("Wewnątrz funkcji x =", x) 

def zasieg_zmiennych():
    global zmienna_globalna
    zmienna_globalna += 5
    inna_zmienna_globalna = 15
    print("Wartosc zmiennej globalnej wewnatrz funkcji:", zmienna_globalna)
    print("Wartosc innej zmiennej globalnej wewnatrz funkcji:", inna_zmienna_globalna)

def lokalne_globalne2():
    zmienna_lokalna1 = 3
    zmienna_lokalna2 = 5
    print("Wartosc zmiennej lokalnej 1:", zmienna_lokalna1)
    print("Wartosc zmiennej lokalnej 2:", zmienna_lokalna2)

def lokalne_globalne1():
    lokalne_globalne2()
    print('Przypisanie wartości zmiennej zmienna_lokalna1 '\
          'nie spowoduje błędu, bo Python szuka najpierw '\
          'zmiennej lokalnej w funkcji, a potem globalnej.')
    print('Próba odczytu wartości zmiennej zmienna_lokalna2 '\
          'spowoduje błąd, bo Python nie znajdzie tej zmiennej '\
          'ani lokalnej, ani globalnej.') 
    zmienna_lokalna1 = 4
    x = zmienna_lokalna2


def main1():
    print("This is the main function.")
    print("This is a doc string for function_example: ") 
    print(function_example.__doc__)
    print("\nZasięg zmiennych")
    print(f"zmienna_globalna = {zmienna_globalna}")
    print(f"inna_zmienna_globalna = {inna_zmienna_globalna}")
    print("Wywołanie funkcji zasieg_zmiennych()... ")
    zasieg_zmiennych()
    print("Po wywołaniu funkcji zasieg_zmiennych():")
    print("Wartosc zmiennej globalnej poza funkcja:", zmienna_globalna)
    print("Wartosc innej zmiennej globalnej poza funkcja:", inna_zmienna_globalna)
    print("Inna zmiena globalna nie zmieniła wartości, "\
           "bo w funkcji użyto zmiennej lokalnej "\
           "inna_zmienna_globalna.")
    
    print('-'*50)
    print("W Pythonie przekazujemy argumentów przez wartość")
    x = 3
    tab = [1,2]
    print(f"Przed wywołaniem funkcji x = {x}, "\
          f"tab = {tab}")
    zmiana_argumentu(x, 10)
    print("Po wywołaniu funkcji x =", x)
    zmiana_elementu(tab, 19)
    print("Po wywołaniu funkcji tab =", tab)
    print('-'*50)
    print("Wywołanie funkcji lokalne_globalne1()...")
    lokalne_globalne1()

def main2():
    print('-'*50)
    print('Zmienne local i nonlocal')
    def outer():
        title1 = 'outer title1'
        title2 = 'outer title2'
        def inner():
            title1 = 'another title'
            nonlocal title2
            title2 = 'modified outer title2'
            print('inner title1:', title1)
            print('inner title2:', title2)
        inner()
        print('outer title1:', title1)
        print('outer title2:', title2)
    outer()

zmienna = 0
def funkcja1():
    zmienna = 1
    def funkcja2():
        zmienna = 2
        def funkcja31():
            global zmienna
            print("funkcja31 - zmienna =", zmienna)
        def funkcja32():
            nonlocal zmienna
            print("funkcja32 - zmienna =", zmienna)
        funkcja31()
        funkcja32()
    funkcja2()

def main3():
    print('-'*50)
    print('Przykład zmiennych globalnych, local i nonlocal')
    funkcja1()
    print("Z punktu widzenia funkcja31 i funkcja32 "\
          "zmienne z funkcja1 nie są ani global, ani nonlocal.")

if __name__ == "__main__":
    main1()
#    main2()