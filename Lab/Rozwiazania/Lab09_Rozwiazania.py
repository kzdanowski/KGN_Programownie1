"""
1. Napisz funkcję del_empty_lines(plik_in, plik_out)
która wczyta plik_in i zapisze go do plik_out
pomijając puste linie.


Napisz funkcję otwierającą plik z obsługą błędów:
plik nie istnieje,
brak uprawnień,
złe kodowanie.
"""

def del_empty_lines(file_in, file_out, text_encoding):
    try:
        fin = open(file_in, "r", encoding=text_encoding)
        fout = open(file_out, "w", encoding=text_encoding)
        for line in fin.readlines():
            print(f"Dlugosc '{line} to {len(line)}")
            if line != '\n':
                fout.write(line)
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)
    except UnicodeDecodeError as e:
        print(e)
    finally:
        fin.close()
        fout.close()

# W poniższej wersji otwieramy pliki konstrukcją "with"
# co jest wygodniejsze, bardziej czytelne,
# nie musimy ręcznie zamykać plików
# Do pliku fout zapisujemy tylko linie, które nie zawierają
# samych "białych znaków"
def del_empty_lines2(file_in, file_out, text_encoding):
    try:
        with open(file_in, "r", encoding=text_encoding) as fin, \
               open(file_out, "w", encoding=text_encoding) as fout:
            for line in fin.readlines():
                if len(line.strip()) != 0:
                    fout.write(line)
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)
    except UnicodeDecodeError as e:
        print(e)
