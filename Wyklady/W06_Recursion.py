def silnia_rec(n):
    print(f"Wyołanie silnia_rec({n})")
    if n == 0:
        print(f"Koniec wywołania silnia({n}), zwracana wartość: {1}")
        return 1
    val =  n*silnia_rec(n-1)
    print(f"Koniec wywołania silnia({n}), zwracana wartość: {val}")
    return val

# dwumian Newtona dn(n,k) "n nad k" podaje ilość k-elementowych
# podzbiorów zbioru n-elementowego
# można go wyliczyć według rekurencyjnej zależności
# dn(n,0) = dn(n, n) = 1, dla 0<=n
# dn(n+1, k) = dn(n,k) + dn(n, k-1), dla 0<k<n+1

# Ten przykład pokazuje, że podczas wywołań rekurencyjnych
# możemy wiele razy obliczać te same wartości
# np. wywołanie dn(5,4) to pokazuje

def dn_rec(n,k):
    print(f"Wywołanie rekurencyjne dn({n}, {k})")
    if n < 0 or k < 0:
        return -1 # błąd danych wejściowych
    if n < k:
        return 0 # nie ma podzbiorów o mocy większej niż sam zbiór
    #przypadek bazowy
    if k == 0 or k == n:
        return 1
    # teraz 0<k<n
    assert 0 < k and k < n
    r1 = dn_rec(n-1, k)
    r2 = dn_rec(n-1, k-1)
    print(f"Koniec wywołania, zwracana wartość: {r1+r2}")
    return r1 + r2

# Teraz będziemy zapamiętywać obliczone wartości
# w słowniku

def dn_dict(n, k, obliczone_wartosci={}):
    print(f"Wywołanie dn_dict({n}, {k})")
    if (n,k) in obliczone_wartosci:
        print(f"Koniec wywołania dn_dict({n}, {k}), "
               f"wartość w słowniku {obliczone_wartosci[(n,k)]}")
        return obliczone_wartosci[(n,k)]
    # przypadki nieprawidłowe
    if n < k or n < 0 or k < 0:
        return -1
    if k == 0 or n == k:
        obliczone_wartosci[(n,k)] = 1
        print(f"Koniec wywołania dn_dict({n}, {k}) = 1")
        return 1
    r1 = dn_dict(n-1, k, obliczone_wartosci)
    r2 = dn_dict(n-1, k-1, obliczone_wartosci)
    print(f"Koniec wywołania dn_dict({n}, {k}) = {r1+r2}")


def max_rec_depth_counter(i):
    print(f"Recursion depth: {i}")
    max_rec_depth_counter(i+1)



def main():
    print("Silnia")
    silnia_rec(5)
    print("Dwumian Newtona dn(5,4)")
    print("Powtarzanie tych samych obliczeń")
    dn_rec(5,4)
    print("Dwumian Newtona przy pomocy słownika")
    dn_dict(5,4)
    max_rec_depth_counter(0)

if __name__ == "__main__":
    main()