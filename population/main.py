"""przykładowy plik"""

# Zapisywanie danych liczbowych
with open('numbers.txt', 'w') as file:
    file.write("1020 1230 1341 4444 1112 2002 3456 777 999 345 151 357 271 997 103")

# Zapisywanie danych miast
with open('cities.txt', 'w') as file:
    file.write("""Warszawa,1790658
Kraków,779115
Łódź,690422
Gdańsk,470907
Rzeszów,202036
Opole,129782""")

"""zad 1"""
def parzyste_czterocyfrowe(file_name):
    with open(file_name, 'r') as file:
        for number in file.read().split():
            if len(number) == 4 and int(number) % 2 == 0 and number[0] == number[2]:
                yield int(number)

def main():
    print("Czterocyfrowe liczby parzyste, gdzie pierwsza i trzecia cyfra są takie same:")
    for number in parzyste_czterocyfrowe("numbers.txt"):
        print(number)

if __name__ == "__main__":
    main()

"""zad 2"""
def nieparzyste_trzycyfrowe(file_name):
    with open(file_name, 'r') as file:
        for number in file.read().split():
            if len(number) == 3 and int(number) % 2 == 1 and number[0] == number[2]:
                yield int(number)

def main():
    print("Trzycyfrowe liczby nieparzyste, gdzie pierwsza i trzecia cyfra są takie same:")
    for number in nieparzyste_trzycyfrowe("numbers.txt"):
        print(number)

if __name__ == "__main__":
    main()

"""zad 3"""
def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def liczby_pierwsze(file_name):
    with open(file_name, 'r') as file:
        for number in file.read().split():
            if czy_pierwsza(int(number)):
                yield int(number)

def main():
    print("Liczby pierwsze:")
    for number in liczby_pierwsze("numbers.txt"):
        print(number)

if __name__ == "__main__":
    main()


"""zad 4"""
def duze_miasta(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            city, population = line.strip().split(',')
            if int(population) > 300000:
                yield f"{city}: {population}"
def main():
    print("Miasta z populacją przekraczającą 300 000:")
    for city_info in duze_miasta("cities.txt"):
        print(city_info)

if __name__ == "__main__":
    main()
