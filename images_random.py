import os
import shutil
import csv
import random

def remove_directory(path):
    """
    Удаляет директорию по заданному пути.

    Parameters
        path (str): Путь к директории.
    Returns
        None
    """
    
    if os.path.isdir(path):
        shutil.rmtree(path)

def copy_directory(source_path, destination_path):
    """
    Копирует директорию из одного места в другое.

    Parameters
        source_path (str): Путь к исходной директории.
        destination_path (str): Путь к целевой директории.
    Returns
        None
    """
    
    old_path = os.path.relpath(source_path)
    new_path = os.path.relpath(destination_path)
    shutil.copytree(old_path, new_path)

def rename_files(directory_path):
    """
    Переименовывает файлы в директории.

    Parameters
        directory_path (str): Путь к директории.
    Returns
        tuple: Кортеж из трех списков: полных путей к новым файлам, относительных путей к новым файлам, относительных путей к старым файлам.
    """
    
    old_names = os.listdir(directory_path)
    old_rel_paths = [os.path.join(directory_path, name) for name in old_names]
    rand_num = random.sample(range(0,10001), len(old_names))
    new_names = [f'{num}.jpg' for num in rand_num]
    new_rel_paths = [os.path.join(directory_path, name) for name in new_names]
    for old_name, new_name in zip(old_rel_paths, new_rel_paths):
        os.replace(old_name, new_name)
    new_full_paths = [os.path.join(os.path.abspath(directory_path), name) for name in new_names]
    return new_full_paths, new_rel_paths, old_rel_paths

def create_csv_file(file_path, full_paths, rel_paths):
    """
    Создает CSV-файл с информацией о файлах в директории.

    Parameters
        file_path (str): Путь к CSV-файлу.
        full_paths (list): Список полных путей к файлам.
        rel_paths (list): Список относительных путей к файлам.
    Returns
        None
    """
    
    with open(file_path, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        for full_path, rel_path in zip(full_paths, rel_paths):
            if 'cat' in rel_path:
                class_name ='cat'
            else:
                class_name= 'dog'  
            writer.writerow([full_path, rel_path, class_name])


def main():
    source_directory = 'dataset2'
    destination_directory = 'dataset3'
    csv_file_path = 'paths3.csv'

    remove_directory(destination_directory)
    copy_directory(source_directory, destination_directory)
    full_paths, rel_paths, old_rel_paths = rename_files(destination_directory)
    create_csv_file(csv_file_path, full_paths, rel_paths)

if __name__ == "__main__":
    main()
  