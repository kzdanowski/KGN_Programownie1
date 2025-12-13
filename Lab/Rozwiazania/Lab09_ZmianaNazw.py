import os

"""
Plik uruchomiony jako __main__ zmienia nazwy plików *.txt
na liczbowe formatu xy.txt.
"""

def rename_txt_files(directory):
    # Pobieramy wszystkie pliki .txt
    txt_files = [f for f in os.listdir(directory) if f.lower().endswith(".txt")]
    txt_files.sort()  # Sortujemy, żeby numeracja była stabilna

    for i, filename in enumerate(txt_files, start=1):
        new_name = f"{i:02}.txt"  # format dwucyfrowy
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        # Jeżeli istnieje plik o nowej nazwie, usuń lub pomiń według potrzeb
        if os.path.exists(new_path):
            print(f"Pomijam – plik {new_name} już istnieje.")
            continue

        os.rename(old_path, new_path)
        print(f"{filename} → {new_name}")

# Przykład użycia:
# rename_txt_files("/ścieżka/do/katalogu")

def main():
    rename_txt_files('.')

if __name__== "__main__":
    main()
