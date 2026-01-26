
HARNESS TESTOWY – WYRAŻENIA REGULARNE (Python re)

Instrukcja:
- Dla każdego zadania wpisz regex jako string.
- Harness automatycznie sprawdzi poprawność.
- Używany jest re.fullmatch, chyba że zaznaczono inaczej.

==================================================
ZADANIE 1 – co najmniej jedna cyfra
==================================================
PATTERN_1 = r""

YES_1 = ["abc123", "123"]
NO_1  = ["abc", ""]

==================================================
ZADANIE 2 – dokładnie trzy małe litery
==================================================
PATTERN_2 = r"..."

YES_2 = ["abc"]
NO_2  = ["abcd", "ab", "a1c"]

==================================================
ZADANIE 3 – ERROR na początku linii
==================================================
PATTERN_3 = r"..."

YES_3 = ["ERROR coś się stało", "ERROR"]
NO_3  = ["INFO ERROR"]

==================================================
ZADANIE 4 – color / colour
==================================================
PATTERN_4 = r"..."

YES_4 = ["color", "colour"]
NO_4  = ["colouur"]

==================================================
ZADANIE 5 – co najmniej dwie cyfry (search)
==================================================
PATTERN_5 = r"..."

YES_5 = ["23", "456"]
NO_5  = ["1", "7"]

==================================================
ZADANIE 6 – od 2 do 4 cyfr
==================================================
PATTERN_6 = r"..."

YES_6 = ["12", "123", "1234"]
NO_6  = ["1", "12345"]

==================================================
ZADANIE 7 – cat lub dog
==================================================
PATTERN_7 = r"..."

YES_7 = ["cat", "dog"]
NO_7  = ["cow"]

==================================================
ZADANIE 8 – (ab|cd)+
==================================================
PATTERN_8 = r"..."

YES_8 = ["ab", "cd", "abab", "abcd"]
NO_8  = ["a", "abc", "abd"]

==================================================
ZADANIE 9 – brak harnessu (opisowe)
==================================================

==================================================
ZADANIE 10 – pierwszy nawias (search)
==================================================
PATTERN_10 = r"..."

YES_10 = ["(a)"]
NO_10  = ["(b)", "(c)"]

==================================================
ZADANIE 11 – HTML <p>...</p> (findall)
==================================================
PATTERN_11 = r"<p>.*?<\/p>"

EXPECTED_11 = ["<p>pierwszy</p>", "<p>drugi</p>"]

==================================================
ZADANIE 12 – imię i nazwisko
==================================================
PATTERN_12 = r""

YES_12 = ["Jan Kowalski"]
NO_12  = ["Jan", "JanKowalski"]

==================================================
ZADANIE 13 – data YYYY-MM-DD
==================================================
PATTERN_13 = r"..."

YES_13 = ["2024-03-15"]
NO_13  = ["15-03-2024"]

==================================================
ZADANIE 14 – priorytet alternatywy
==================================================
PATTERN_14 = r"^a|bc$"

YES_14 = ["a", "bc"]
NO_14  = ["abc"]

==================================================
ZADANIE 15 – liczba całkowita (walidacja)
==================================================
PATTERN_15 = r"..."

YES_15 = ["123", "-456", "0"]
NO_15  = ["12a", "abc-123"]

==================================================
SILNIK TESTOWY
==================================================

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
