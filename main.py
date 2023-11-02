# my_array = [1, 2, 3, 4, 5, 6, 7, 34, 67, 23, 36, 41, 33, 22, 86, ]
#
# print(filter(lambda num: num % 2 == 0, my_array))
#
# print(map(lambda num: num % 2 == 0, my_array))

# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

import os


def count():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        count = 0
        contacts_list = file.read().rstrip().split("\n")
        for i in contacts_list:
            for j in contacts_list:
                x = j.lower().replace("\n", " ").split()
                xx = int(x[0])
                if count == xx:
                    count += 1
        return count






def print_data():
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        phonebook_str = file.read()
    print(phonebook_str)
    print()


def input_name():
    return input("Введите имя контакта: ")


def input_surname():
    return input("Введите фамилию контакта: ")


def input_patronymic():
    return input("Введите отчество контакта: ")


def input_phone():
    return input("Введите номер телефона контакта: ")


def input_address():
    return input("Введите адрес контакта: ")


def input_data():
    surname = input_surname().title()
    name = input_name().title()
    patronymic = input_patronymic().title()
    phone = input_phone()
    address = input_address().title()
    my_sep = ' '
    return f"{count()}{my_sep}{surname}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}{my_sep}{address}"


def add_contact():
    new_contact_str = input_data()
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(new_contact_str)
        file.write('\n')


def search_contact():
    print("Варианты поиска:\n"
          "1. По номеру\n"
          "2. По фамилии\n"
          "3. По имени\n"
          "4. По отчеству\n"
          "5. По телефону\n"
          "6. По адресу\n")
    command = input("Выберете вариант поиска: ")

    while command not in ("1", "2", "3", "4", "5", "6"):
        print("Некорректный ввод, повторите ввод:")
        command = input("Выберете вариант поиска: ")

    i_search = int(command) - 1
    search = input("Введите данные для поиска: ").lower()
    print()
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        contacts_list = file.read().rstrip().split("\n")

    check_cont = False
    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace("\n", " ").split()
        if search in lst_contact[i_search]:
            print(contact_str)
            print()
            check_cont = True

    if not check_cont:
        print("Такого контакта нет.")


def interface():
    with open("phonebook.txt", "a", encoding="UTF-8"):
        pass
    command = ""
    os.system("cls")
    while command != "5":
        print("Меню пользователя:\n"
              "1. Вывод данных на экран\n"
              "2. Добавление контакта\n"
              "3. Поиск контакта\n"
              "4. Импорт контакта\n"
              "5. Выход\n"
              "6. Удаление контакта\n"
              "7. Редактировать контакт")

        command = input("Введите пункт меню: ")

        while command not in ("1", "2", "3", "4", "5", "6", "7"):
            print("Некорректный ввод, повторите ввод:")
            command = input("Введите пункт меню: ")
        match command:
            case "1":
                print_data()
            case "2":
                add_contact()
            case "3":
                search_contact()
            case "4":
                print('  ')
            case "5":
                print()
            case "6":
                del_contact()
            case "7":
                redact_contact()
        print()


def del_contact():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        key = input('Введите порядковый номер контакта, который хотите удалить: ')
        contacts_list = file.read().rstrip().splitlines()
        for element in range(len(contacts_list)):
            if key == str(contacts_list[element][0]):
                file = open('phonebook.txt', 'r', encoding="UTF-8")
                content = file.read()
                lines = content.splitlines()
                del lines[element]
                new_content = '\n'.join(lines)
                new_file = open('phonebook.txt', 'w', encoding="UTF-8")
                new_file.write(new_content + '\n')
                new_file.close()
                file.close()
                print('Контакт', contacts_list[element], 'удален!')
            else:
                print('Контакта с таким порядковым номер не существует!', '\n')


def redact_contact():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        contacts_list = file.read().rstrip().splitlines()
        key = input('Введите порядковый номер контакта, для внесения изменений: ')
        while int(key) > len(contacts_list):
            print("Некорректный ввод, повторите ввод:")
            key = input('Введите порядковый номер контакта, для внесения изменений: ')
    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace("\n", " ").split()
        if key in lst_contact[0]:
            print(lst_contact)
            par_red = input('Варианты редактирование контакты:\n '
                            '1. Фамилия.\n'
                            '2. Имя\n'
                            '3. Отчество\n'
                            '4. Номер телефона\n'
                            '5. Адрес\n')
            while par_red not in ("1", "2", "3", "4", "5",):
                print("Некорректный ввод, повторите ввод:")
                par_red = input('Варианты редактирование контакты:\n ')
            new_data_red = input('Введите новые данные контакта:')
            lst_contact[int(key)] = lst_contact[int(key)].replace(lst_contact[int(par_red)], new_data_red)
            for i in range(len(lst_contact)):
                contacts_list[i] = lst_contact[i]
            lines = ''.join(contacts_list)
            print(lines.count(' '))
            lines.replace(' ', '\n')
            print(lines)



if __name__ == "__main__":
    interface()
