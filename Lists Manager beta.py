import random

N = input("Введите длину списков list и list 2: ")

def menu():
    menu_id = input("\n Меню\n1.Калькулятор списков \n2.Изменить элементы в списке\n3.Добавить/удалить элемент в списке\n4.Найти значение в списках \n5.Показать списки ")
    if menu_id.isdigit():
        if int(menu_id) == 1:
            menu_1()
        elif int(menu_id) == 2:
            menu_2()
        elif int(menu_id) == 3:
            menu_3()
        elif int(menu_id) == 4:
            menu_4()
        elif int(menu_id) == 5:
            show_list(list,list2)
        else:
            print("Неверный выбор меню!")
            menu()
    else:
        print("Неверный выбор")
        menu()

def menu_1():
    menu_1_2id = input("Выберите в какой список записать полученное значение: ")
    if menu_1_2id.isdigit():
        if int(menu_1_2id) == 1:
            menu_1_1(list, list2)
        elif int(menu_1_2id) == 2:
            menu_1_1(list2, list)
        else:
            print("Неверный ввод! Выберите номер списка 1 или 2!")
            menu_1()
    else:
        print("Назад...")
        menu()

def menu_1_1(l1,l2):
    print("Полученное значение будет записано в список:", l1)
    menu_1_1_op = input("Выберите знак операции со списком: ")
    if menu_1_1_op == "+":
        l1 = [l1[i] + l2[i] for i in range(len(l1))]
    elif menu_1_1_op == "-":
        l1 = [l1[i] - l2[i] for i in range(len(l1))]
    elif menu_1_1_op == "*":
        l1 = [l1[i] * l2[i] for i in range(len(l1))]
    elif menu_1_1_op == "/":
        l1 = [l1[i] / l2[i] for i in range(len(l1))]
    else:
        print("Ошибка! Выберите одну из операций + - * /!")
    print(l1)
    menu()

def menu_2():
    menu2_id = input("В каком списке нужно изменить элемент? \n1.list\n2.list2\n3.Назад")
    if menu2_id.isdigit():
        if int(menu2_id) == 1:
            menu2_1(list)
        elif int(menu2_id) == 2:
            menu2_1(list2)
        elif int(menu2_id) == 3:
            menu()
        else:
            print("Неверный ввод выбора списка!")
            menu_2()
    else:
        print("Неверный ввод выбора списка!")
        menu_2()

def menu2_1(l1):
    print(l1)
    menu2_1_op = input("Какой элемент нужно изменить: ")
    if menu2_1_op.isdigit():
        if 0 <= int(menu2_1_op) < len(l1):
            print("Элемент", menu2_1_op, "списка 1", l1[int(menu2_1_op)])
            l1[int(menu2_1_op)] = input("Заменить на: ")
            print(l1)

            menu2_1_op2 = input("1.Заменить ещё... \n2.Меню ")
            if menu2_1_op2.isdigit():
                if int(menu2_1_op2) == 1:
                    menu2_1(l1)
                else:
                    menu()
            else:
                print("Неверный ввод!")
                menu()


        else:
            print("Неверный номер элемента")
            menu2_1(l1)
    else:
        print("Неверный номер элемента!")
        menu2_1(l1)

def menu_3():
    print("В какой список нужно добавить/удалить элемент? \n1.",list,"\n2.",list2,"\n3.Назад")
    menu_3_op = input(":")
    if menu_3_op.isdigit():
        if int(menu_3_op) == 1:
            menu_3_1(list)

        if int(menu_3_op) == 2:
            menu_3_1(list2)
        if int(menu_3_op) == 3:
            menu()
        else:
            print("Выберите 1 или 2 или 3!")
            menu_3()
    else:
        print("Выберите 1 или 2! ")
        menu_3()


def menu_3_1(l1):
    menu_3_1_op = input("1.Добавить\n2.Удалить\n")
    if menu_3_1_op.isdigit():
        if int(menu_3_1_op) == 1:
            l1.append(input("Добавить в конец списка: "))
            print(l1)
            menu()
        if int(menu_3_1_op) == 2:
            print(l1)
            l1.pop(int(input("Введите индекс ячейки которую нужно удалить: ")))
        else:
            print("Выберите 1 или 2: ")
            menu_3_1(l1)
    else:
        print("Выберите 1 или 2: ")
        menu_3_1(l1)

def menu_4():
    menu_4_op = input("В каком списке нужно найти значение. \n1.\n2.\n3.Назад")
    if menu_4_op.isdigit():
        if int(menu_4_op) == 1:
            menu_4_1(list)
        elif int(menu_4_op) == 2:
            menu_4_1(list2)
        elif int(menu_4_op) == 3:
            menu()
        else:
            menu_4()
    else:
        print("Выберите 1, 2 или 3!")
        menu_4()

def menu_4_1(l1):
    menu_4_1op1 = input("Введите значение которое нужно найти:")
    if menu_4_1op1.isdigit():
        for x in range(len(l1)):
            if l1[x] == int(menu_4_1op1):
                print("Совпадение элемент", x, "=", l1[x])
    else:
        print("Можем найти только целые числы!")
        menu()
    menu()

def show_list(l1,l2):
    print("list:",l1,"\nlist2:",l2)
    menu()

if N.isdigit:
    a = int(input("Введите значение разброса: "))
    b = int(input("Введите значение разброса:"))
    list = [random.randint(a, b) for x in range(int(N))]
    list2 = [random.randint(a, b) for x in range(int(N))]
    menu()
else:
    print("Введите целое число: ")
    begin




