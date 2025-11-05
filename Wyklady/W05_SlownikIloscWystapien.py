import random

# Wygenerowane przez ChatGPT
# --- 1. Generowanie tablicy losowych liczb ---
# np. 20 losowych liczb z zakresu 1–10
tablica = [random.randint(1, 10) for _ in range(20)]
print("Wygenerowana tablica:", tablica)

# --- 2. Tworzenie słownika z ilością wystąpień ---
liczniki = {}

for liczba in tablica:
    if liczba in liczniki:
        liczniki[liczba] += 1
    else:
        liczniki[liczba] = 1

print("Słownik wystąpień:", liczniki)
