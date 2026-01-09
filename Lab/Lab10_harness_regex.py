"""
HARNESS TESTOWY – WYRAŻENIA REGULARNE (Python re)

Instrukcja:
- Dla każdego zadania wpisz regex jako string 
  definiujący PATTERN_<N>.
- Opis zadań zdajduje się w pliku Lab10_RegEx.txt.
- Harness automatycznie sprawdzi poprawność.
- Używany jest re.fullmatch, chyba że zaznaczono inaczej.
"""

""" 
==================================================
ZADANIE 1 – co najmniej jedna cyfra
==================================================
"""

PATTERN_1 = r".*\d.*"

YES_1 = ["abc123", "123"]
NO_1  = ["abc", ""]

"""
==================================================
ZADANIE 2 – dokładnie trzy małe litery
==================================================
"""
PATTERN_2 = r"[a-z]{3}"

YES_2 = ["abc"]
NO_2  = ["abcd", "ab", "a1c"]

"""
==================================================
ZADANIE 3 – ERROR na początku linii
==================================================
"""

PATTERN_3 = r"..."

YES_3 = ["ERROR coś się stało", "ERROR"]
NO_3  = ["INFO ERROR"]

"""
==================================================
ZADANIE 4 – color / colour
==================================================
"""
PATTERN_4 = r"..."

YES_4 = ["color", "colour"]
NO_4  = ["colouur"]

"""
==================================================
ZADANIE 5 – co najmniej dwie cyfry (search)
==================================================
"""

PATTERN_5 = r"..."

YES_5 = ["23", "456"]
NO_5  = ["1", "7"]

"""
==================================================
ZADANIE 6 – od 2 do 4 cyfr
==================================================
"""
PATTERN_6 = r"..."

YES_6 = ["12", "123", "1234"]
NO_6  = ["1", "12345"]

"""
==================================================
ZADANIE 7 – cat lub dog
==================================================
"""

PATTERN_7 = r"..."

YES_7 = ["cat", "dog"]
NO_7  = ["cow"]

"""
==================================================
ZADANIE 8 – (ab|cd)+
==================================================
"""

PATTERN_8 = r"..."

YES_8 = ["ab", "cd", "abab", "abcd"]
NO_8  = ["a", "abc", "abd"]

"""
==================================================
ZADANIE 9 – brak harnessu (opisowe)
==================================================

==================================================
ZADANIE 10 – pierwszy nawias (search)
==================================================
"""
PATTERN_10 = r"..."

YES_10 = ["(a)"]
NO_10  = ["(b)", "(c)"]

"""
==================================================
ZADANIE 11 – HTML <p>...</p> (findall)
==================================================
"""
PATTERN_11 = r"..."

HTML_11 = "<p>pierwszy</p> <p>drugi</p>"
EXPECTED_11 = ["<p>pierwszy</p>", "<p>drugi</p>"]

"""
==================================================
ZADANIE 12 – imię i nazwisko
==================================================
"""
PATTERN_12 = r"..."

YES_12 = ["Jan Kowalski"]
NO_12  = ["Jan", "JanKowalski"]

"""
==================================================
ZADANIE 13 – data YYYY-MM-DD
==================================================
"""
PATTERN_13 = r"..."

YES_13 = ["2024-03-15"]
NO_13  = ["15-03-2024"]

"""
==================================================
ZADANIE 14 – priorytet alternatywy
==================================================
"""
PATTERN_14 = r"^a|bc$"

YES_14 = ["a", "bc"]
NO_14  = ["abc"]

"""
==================================================
ZADANIE 15 – liczba całkowita (walidacja)
==================================================
"""
PATTERN_15 = r"..."

YES_15 = ["123", "-456", "0"]
NO_15  = ["12a", "abc-123"]

"""
==================================================
SILNIK TESTOWY
==================================================
"""
import re

def check_full(pattern, yes, no):
    for t in yes:
        assert re.fullmatch(pattern, t), f"FAIL: should match {t}"
    for t in no:
        assert not re.fullmatch(pattern, t), f"FAIL: should not match {t}"

def check_search(pattern, yes, no):
    for t in yes:
        assert re.search(pattern, t), f"FAIL: should find in {t}"
    for t in no:
        assert not re.search(pattern, t), f"FAIL: should not find in {t}"

def check_findall(pattern, text, expected):
    result = re.findall(pattern, text)
    assert result == expected, f"FAIL: {result} != {expected}"

print("Harness loaded. Wpisz regexy i uruchom testy ręcznie.")

TESTS = [(PATTERN_1, YES_1, NO_1, check_full),
         (PATTERN_2, YES_2, NO_2, check_full),
         (PATTERN_3, YES_3, NO_3, check_full),
         (PATTERN_4, YES_4, NO_4, check_full),
         (PATTERN_5, YES_5, NO_5, check_search),
         (PATTERN_6, YES_6, NO_6, check_full),
         (PATTERN_7, YES_7, NO_7, check_full),
         (PATTERN_8, YES_8, NO_8, check_full),
         (PATTERN_10, YES_10, NO_10, check_search),
         (PATTERN_11, None, None, lambda p, y, n: check_findall(p, HTML_11, EXPECTED_11)),
         (PATTERN_12, YES_12, NO_12, check_full),
         (PATTERN_13, YES_13, NO_13, check_full),
         (PATTERN_14, YES_14, NO_14, check_full),
         (PATTERN_15, YES_15, NO_15, check_full)]


ALL_OK = True

for i, (p, yes, no, fun) in enumerate(TESTS):
    if i == 9:
        continue  # brak harnessu dla zadania 9
    try:
        print(f'Wzorzec {i+1}: {p}: ', end='')
        fun(p, yes, no)
    except AssertionError as e:
        print(e)
        ALL_OK = False
        continue
    else:
        print("OK")

if ALL_OK:
    print("Wszystkie testy zakończone pomyślnie.")