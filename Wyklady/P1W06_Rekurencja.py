def silnia_rec(n):
    print(f"Wyołanie silnia_rec({n})")
    if n == 0:
        print(f"Koniec wywołania silnia({n}), zwracana wartość: {1}")
        return 1
    val =  n*silnia(n-1)
    print(f"Koniec wywołania silnia({n}), zwracana wartość: {val}")
    return val
