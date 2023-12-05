
'''

def obliczenia_dla_danych(dane):
    suma = sum(dane)
    srednia = suma / len(dane)

    suma_kwadratow_roznicy = sum((x - srednia) ** 2 for x in dane)
    wariancja = suma_kwadratow_roznicy / len(dane)

    licznik = {}
    for liczba in dane:
        licznik[liczba] = licznik.get(liczba, 0) + 1
    dominanty = [k for k, v in licznik.items() if v == max(licznik.values())]

    min_wartosc = min(dane)
    max_wartosc = max(dane)

    return suma, srednia, wariancja, dominanty, min_wartosc, max_wartosc

def wczytaj_dane_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        dane = [int(line.strip()) for line in plik]

    return dane

def wyswietl_wyniki(suma, srednia, wariancja, dominanty, min_wartosc, max_wartosc):
    print(f"Suma: {suma}")
    print(f"Średnia: {srednia}")
    print(f"Wariancja: {wariancja}")
    print(f"Dominanta: {', '.join(map(str, dominanty))}")
    print(f"Min: {min_wartosc}")
    print(f"Max: {max_wartosc}")


nazwa_pliku = 'dane.txt' 
dane = wczytaj_dane_z_pliku(in.txt)
wyniki = obliczenia_dla_danych(dane)

'''

def zad3():
    with open('in_3.txt', 'r') as f:
        slowa = f.read().split()
        slownik = set()
        try:
            with open("dict.txt",'r') as f:
                slownik = set(line.strip() for line in f)

        except FileNotFoundError:
            with open('dict.txt', 'w') as f:
              pass
        slownik.update(word.lower() for word in slowa)

        with open('dict.txt','w') as f:
            for slowo in sorted(slownik):
                f.write(slowo+'\n')

zad3()


def Cezar_Zad2():
  with open('in_cezar.txt', 'r') as f:
        text = f.read()
  mode = input("'szyfruj' lub 'deszyfruj' teskt: ")

  key = int(input("Podaj klucz: "))
  if key > 0:

    al = 'abcdefghijklmnopqrstuvwxyz'

    wynik = ''

    for char in text:
        if char.lower() in al:
            index = al.index(char.lower())

            if mode == 'szyfruj':
                new_index = (index + key) % len(al)
            else:  
                new_index = (index - key) % len(al)

            if char.isupper():
                wynik += al[new_index].upper()
            else:
                wynik += al[new_index]
                    
        else:
            wynik += char

    with open('out_cezar.txt', 'w') as f:
        f.write(wynik)

Cezar_Zad2()


# do zad 3, jeśli w pliku wystąpi słowo więcej niż 1 raz pisze obok ilość
# tych słów

def wczytaj_slownik(nazwa_pliku):
    slownik = {}
    with open(nazwa_pliku, 'r') as plik:
            for linia in plik:
                wyraz, liczba_wystapien = linia.strip().split()
                slownik[wyraz.lower()] = int(liczba_wystapien)
    return slownik

def zapisz_slownik(slownik, nazwa_pliku):
    with open(nazwa_pliku, 'w') as plik:
        for wyraz, liczba_wystapien in slownik.items():
            plik.write(f"{wyraz} {liczba_wystapien}\n")

def analizuj_dane(tekst, slownik):
    slowa = tekst.split()
    for wyraz in slowa:
        wyraz = wyraz.lower().strip('.,?!()[]{}:;')
        slownik[wyraz] = slownik.get(wyraz, 0) + 1


nazwa_pliku_in = 'in_4.txt'
nazwa_pliku_dict = 'dict1.txt'

slownik = wczytaj_slownik(nazwa_pliku_dict)

with open(nazwa_pliku_in, 'r') as plik_in:
    tekst = plik_in.read()
    analizuj_dane(tekst, slownik)

zapisz_slownik(slownik, nazwa_pliku_dict)

for wyraz, liczba_wystapien in slownik.items():
    print(f"{wyraz}: {liczba_wystapien}")
