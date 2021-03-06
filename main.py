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
    rez = []  # rezultatul cerut
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


def test_is_palindrome():
    assert is_palindrome('1221') == True
    assert is_palindrome('322') == False
    assert is_palindrome('2') == True


def det_palidroame_din_a_concatenat_b(lst_a, lst_b):
    """
    determina palindroamele obtinute prin concatenarea nr de pe aceleasi pozitii
    :param lst_a: multimea A
    :param lst_b: multimea B
    :return: lista rezultata
    variabila var este de tip string
    """
    rez = []
    for x in range(len(lst_a)):
        for y in range(len(lst_b)):
            if x == y:
                var = str(lst_a[x]) + str(lst_b[y])
                if is_palindrome(var):
                    rez.append(int(var))
    return rez


def test_det_palidroame_din_a_concatenat_b():
    assert det_palidroame_din_a_concatenat_b([12, 22, 36, 11], [21, 23, 63, 55, 424]) == [1221, 3663]
    assert det_palidroame_din_a_concatenat_b([1, 23, 12], [21, 3, 21, 7]) == [121, 1221]


def oglindit(n):
    """
    calculeaza oglinditul lui n
    :param n: int
    :return: int
    """
    og = str(n)
    og = og[::-1]
    return int(og)


def test_oglindit():
    assert oglindit(122) == 221
    assert oglindit(93737) == 73739
    assert oglindit(3) == 3


def a_divizibil_cu_elem_din_lst(a, lst):
    """
    determinam daca variabila a este divizibila cu toate elementele din lista lst
    :param a: int
    :param lst: lista de nr intregi
    :return: true or false
    """
    for x in lst:
        if a % x != 0:
            return False
    return True


def test_a_divizibil_cu_elem_din_lst():
    assert a_divizibil_cu_elem_din_lst(12, [1, 2, 3, 4]) == True
    assert a_divizibil_cu_elem_din_lst(2, [1, 4, 6]) == False
    assert a_divizibil_cu_elem_din_lst(3, [6]) == False


def cerinta5(lst_a, lst_c):
    """
    inlocuieste toate elementele din lista lst_a cu
    oglinditul lor daca elementele sunt divizibile
    cu toate elemntele din lista lst_c
    :param lst_a: int
    :param lst_c: int
    :return: int
    """
    rez = []
    for x in lst_a:
        if a_divizibil_cu_elem_din_lst(x, lst_c):
            og = oglindit(x)
            rez.append(og)
        else:
            rez.append(x)
    return rez


def test_cerinta5():
    assert cerinta5([12, 22, 36, 363], [1, 2, 3, 4]) == [21, 22, 63, 363]
    assert cerinta5([22, 23, -6, 55, 363], [1, 2, 3, 4]) == [22, 23, -6, 55, 363]


def read_list():
    list_str = input("Introduceti termenii din lista: ").split(" ")
    lst = []
    for x in list_str:
        x = int(x)
        lst.append(x)
    return lst


def show_menu():
    print("""
    1. Citirea a dou?? mul??imi de numere ??ntregi de la tastatura sub forma a dou?? liste
    2. Afi??a??i dac?? cele dou?? liste au acela??i num??r de elemente pare
    3. Afi??a??i o list?? reprezent??nd intersec??ia listelor citite de la tastatur??
    4. Afi??a??i toate palindroamele ob??inute prin concatenarea elementelor de pe acelea??i pozi??ii ??n cele dou?? liste
    5. Citi??i o a treia list????i afi??a??i listele ob??inute prin ??nlocuirea ??n cele 
    dou?? liste citite la punctul 1 a tuturor elementelor cu oglinditul lor dac?? 
    ??ndeplinesc urm??toarea regul??: elementele sunt divizibile cu toate elementele din a treia lista
    6. Exit.
    """)


def main():
    lst_a = []
    lst_b = []
    while True:
        show_menu()
        cmd = input("Introduceti o comanda: ")
        if cmd == '1':
            lst_a = read_list()
            lst_b = read_list()
        elif cmd == '2':
            print(same_number_of_even_numbers(lst_a, lst_b))
        elif cmd == '3':
            print(a_intersectat_cu_b(lst_a, lst_b))
        elif cmd == '4':
            print(det_palidroame_din_a_concatenat_b(lst_a, lst_b))
        elif cmd == '5':
            lst_c = read_list()
            print(cerinta5(lst_a, lst_c))
            print(cerinta5(lst_b, lst_c))
        elif cmd == '6':
            break
        else:
            print("Comanda invalida!")


test_a_intersectat_cu_b()
test_same_number_of_even_numbers()
test_is_palindrome()
test_det_palidroame_din_a_concatenat_b()
test_oglindit()
test_a_divizibil_cu_elem_din_lst()
test_cerinta5()


if __name__ == '__main__':
    main()
