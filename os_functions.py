import os
import shutil

current_directory = os.getcwd()


def new_folder():
    print(f"Папка будет создана в {current_directory}.")
    folder_name = str(input("Введите название папки: "))
    os.mkdir(folder_name)


def del_ff():
    print(f"Файл или пака должны находиться в {current_directory}.")
    name_del_ff = str(input("Введите название папки/файла: "))
    path_to_delete = os.path.join(current_directory, name_del_ff)
    desidion_user = input(f"Вы действительно хотите удалить {path_to_delete}? y/n: ")

    if desidion_user == 'y':
        try:
            if os.path.isfile(path_to_delete):
                os.remove(path_to_delete)
                print(f"Файл {current_directory} успешно удален.")
            elif os.path.isdir(path_to_delete):
                shutil.rmtree(path_to_delete)
                print(f"Папка {current_directory} успешно удалена.")
            else:
                print(f"{current_directory} не существует.")
        except Exception as e:
            print(f"Произошла ошибка при удалении: {str(e)}")
    else:
        print("Удаление отменено.")


def copy_ff():
    print(f"Текущее местоположение: {current_directory}.")
    name_copy_ff = str(input("Введите название папки/файла: "))
    path_to_copy_ff = os.path.join(current_directory, name_copy_ff)
    destination_copy = str(input("Введите каталог назначения: "))
    path_destination = os.path.join(destination_copy, name_copy_ff)


    if os.path.isfile(name_copy_ff):
        shutil.copy(path_to_copy_ff, path_destination)
        print(f"Файл {name_copy_ff} успешно скопирован в {path_destination}")
    elif os.path.isdir(name_copy_ff):
        shutil.copytree(path_to_copy_ff, path_destination)
        print(f"Папка {name_copy_ff} и её содержимое успешно скопированы в {path_destination}")
    else:
        print(f"{name_copy_ff} не существует или не является ни файлом, ни папкой.")


# def ls_dir_print():
#     files_and_folders = os.listdir()
#     for item in files_and_folders:
#         print(item)

def ls_only_dir_or_file_print(x='x'):
    contents = os.listdir(current_directory)

    for item in contents:
        full_path = os.path.join(current_directory, item)

        if (os.path.isdir(full_path) and (x == 'd' or x == 'x')) or (os.path.isfile(full_path) and (x == 'f' or x == 'x')):
            if os.path.isdir(full_path):
                print(f"Папка: {item}")
            elif os.path.isfile(full_path):
                print(f"Файл: {item}")

def next_work_dir():
    print(f"Текущее местоположение: {current_directory}.")
    new_directory = str(input("Введите путь: "))
    os.chdir(new_directory)

    new_current_directory = os.getcwd()
    print("Новая текущая рабочая директория:", new_current_directory)
