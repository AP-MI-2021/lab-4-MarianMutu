def same_number_of_even_numbers(lst_a, lst_b):
    """
    determinam daca cele doua multimi au un nr egal de nr pare
    :param lst_a: multimea A
    :param lst_b: multimea B
    :return: True or False
    """
    nr_a = 0
    nr_b = 0
    for x in lst_a:
        if x % 2 == 0:
            nr_a += 1
    for y in lst_b:
        if y % 2 == 0:
            nr_b += 1
    if nr_a == 0 or nr_b == 0:
        return False
    elif nr_a == nr_b:
        return True
    else:
        return False


def test_same_number_of_even_numbers():
    assert same_number_of_even_numbers([2, 4, 7, 8, 1], [1, 3, 4, 6, 2]) == True
    assert same_number_of_even_numbers([2, 1, 7, 8, 1], [1, 3, 4, 6, 2]) == False
    assert same_number_of_even_numbers([], []) == False

def a_intersectat_cu_b(lst_a, lst_b):
    """
    detremina intersectia multimii A cu multimea B
    :param lst_a: multimea A
    :param lst_b: multimea B
    :return: Intersectia multimilor
    """
    rez = [] # rezultatul cerut
    for x in lst_a:
        if x in lst_b:
            rez.append(x)
    return rez


def test_a_intersectat_cu_b():
    assert a_intersectat_cu_b([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert a_intersectat_cu_b([23, 34, 56, 78], [1, 2, 3, 4]) == []
    assert a_intersectat_cu_b([], []) == []

def is_palindrome(nr):
    """
    determina daca un nr scris sub forma de sir de caractere e palindrom sau nu
    :param nr: string
    :return: true or false
    """
    var = nr[::-1]
    if var == nr:
        return True
    else:
        return False


def read_lists():
    list_str_a = input("Introduceti termenii primei liste: ").split(" ")
    list_str_b = input("Introduceti termenii celei de a doua liste: ").split(" ")
    lst_a = []
    lst_b = []
    for x in list_str_a:
        lst_a.append(int(x))
    for y in list_str_b:
        lst_b.append(int(y))
    return lst_a, lst_b


def show_menu():
    print("""
    1. Citirea a două mulțimi de numere întregi de la tastatura sub forma a două liste
    2. Afișați dacă cele două liste au același număr de elemente pare
    3. Afișați o listă reprezentând intersecția listelor citite de la tastatură
    4. Afișați toate palindroamele obținute prin concatenarea elementelor de pe aceleași poziții în cele două liste
    5. Citiți o a treia listăși afișați listele obținute prin înlocuirea în cele 
    două liste citite la punctul 1 a tuturor elementelor cu oglinditul lor dacă 
    îndeplinesc următoarea regulă: elementele sunt divizibile cu toate elementele din a treia lista
    6. Exit.
    """)


def main():
    lst_a = []
    lst_b = []
    while True:
        show_menu()
        cmd = input("Introduceti o comanda: ")
        if cmd == '1':
            lst_a, lst_b = read_lists()
        elif cmd == '2':
            print(same_number_of_even_numbers(lst_a, lst_b))
        elif cmd == '3':
            print(a_intersectat_cu_b(lst_a, lst_b))
        elif cmd == '4':
            pass
        elif cmd == '5':
            pass
        elif cmd == '6':
            break
        else:
            print("Comanda invalida!")


test_a_intersectat_cu_b()
test_same_number_of_even_numbers()


if __name__ == '__main__':
    main()
