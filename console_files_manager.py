"""
1. Создать новый проект ""Консольный файловый менеджер"
2. В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.
Так же можно добавить любой дополнительный функционал по желанию.

Описание пунктов:
- создать папку
после выбора пользователь вводит название папки, создаем её в рабочей директории;
- удалить (файл/папку)
после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть;
- копировать (файл/папку)
после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;
- просмотр содержимого рабочей директории
вывод всех объектов в рабочей папке;
- посмотреть только папки
вывод только папок которые находятся в рабочей папке;
- посмотреть только файлы
вывод только файлов которые находятся в рабочей папке;
- просмотр информации об операционной системе
вывести информацию об операционной системе (можно использовать пример из 1-го урока);
- создатель программы
вывод информации о создателе программы;
- играть в викторину
запуск игры викторина из предыдущего дз;
- мой банковский счет
запуск программы для работы с банковским счетом из предыдущего дз (задание учебное, после выхода из программы управлением счетом в главной программе сумму и историю покупок можно не запоминать);
- смена рабочей директории (*необязательный пункт)
усложненное задание пользователь вводит полный /home/user/... или относительный user/my/... путь. Меняем рабочую директорию на ту что ввели и работаем уже в ней;
- выход
выход из программы.
Так же можно добавить любой другой интересный или полезный функционал по своему желанию
После выполнения какого либо из пунктов снова возвращаемся в меню, пока пользователь не выберет выход
3. Выложите проект на github:
4. Можно сдать задание в виде pull request:
5. Посмотреть разбор дз по функциям, если требуется, то сделать работу надо ошибками.1. Создать новый проект ""Консольный файловый менеджер"
"""
import datetime


def delimiter(char="*", qua=10, end_char=''):
    """
    Функция для печати разделителя
    :param char: символ разделителя
    :param qua: длина строки (кол-во символов)
    :param end_char: последний символ (для переноса каретки)
    :return: None
    """
    print(char * qua, end_char)


def current_time_op():
    """
    Функция для получения даты и времени выоплнения операции
    Необходима библиотека datetime
    :return:
    """
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


def history_add(history_dict, operation_description):
    """
    Функция для добавления данных операции в историю
    :param history_dict: переменная для хранения истории (dict)
    :param operation_description: данные операции (list)
    :return: 2023-10-05 18:03:05
    """
    history_dict.update({current_time_op(): operation_description})


def balance_change(op, balance, input_num, history):
    """
    Функция для изменения баланска
    :param op: вид операции
    :param balance: переменная для хранения баланса (float)
    :param input_num: число на которое изменится баланс
    :param history: переменная для хранения история операций (dict)
    :return:
    """
    if op == "+":
        delimiter()
        # Операция + запись в историю
        balance += input_num
        history_add(history, ["пополнение счета", input_num, balance])
        # Вывод на экран
        print(f"\nCчёт успешно пополнен на {input_num} р.")
        print(f"Ваш баланс: {balance} р.")
        delimiter("*", 10, "\n")
        return balance
    elif op == "-":
        delimiter()
        # Проверка баланса на лачие срадств для совершения покупки
        if balance > input_num:
            # Операция + запись в историю
            balance -= float(input_num)
            history_add(history, ["покупка", input_num, balance])
            # Вывод на экран
            print(f"\nСовершена покупка на {input_num} р.")
            print(f"Ваш баланс: {balance} р.")
            delimiter("*", 10, "\n")
            return balance
        else:
            # Запись в историю
            history_add(history, ["отказ в операции", input_num, balance])
            # Вывод на экран
            print(f"\nНедостаточно средств!")
            print(f"Ваш баланс: {balance} р.")
            delimiter("*", 10, "\n")
            return balance


def history_print(histori_dict):
    """
    Функция для вывода на экран истории операций
    :param histori_dict:
    :return: None
    """
    delimiter()
    delimiter()

    for timestamp, operation in histori_dict.items():
        print(f"Дата и время: {timestamp}")
        print(f"Операция: {operation[0]}")
        print(f"Сумма: {operation[1]} р.")
        print(f"Баланс: {operation[2]} р.\n")

    delimiter()
    delimiter("*", 10, "\n")


# Общий баланс и история операций
user_balance = 0.0
user_history = {}

# Основное меню
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход \n')

    choice = input('Выберите пункт меню: ')
    # Пополнение баланса
    if choice == '1':
        replenishment = float(input("Введите сумму для пополнения счета: "))
        user_balance = balance_change("+", user_balance, replenishment, user_history)
    # Списание
    elif choice == '2':
        write_off = float(input("Введите сумму для списания: "))
        user_balance = balance_change("-", user_balance, write_off, user_history)
    # История операций
    elif choice == '3':
        history_print(user_history)
    # Выход
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')