import os
import csv

from typing import List 

def get_full_paths(class_name: str)->List[str]:
    dataset_dir = 'dataset'
    full_path = os.path.abspath(dataset_dir)
    class_path = os.path.join(full_path, class_name)
    image_names = os.listdir(class_path)
    image_full_paths = [os.path.join(class_path, name) for name in image_names]
    return image_full_paths

def get_relative_paths(class_name: str)->List[str]:
    dataset_dir = 'dataset'
    rel_path = os.path.relpath(dataset_dir)
    class_path = os.path.join(rel_path, class_name)
    image_names = os.listdir(class_path)
    image_rel_paths = [os.path.join(class_path, name) for name in image_names]
    return image_rel_paths

def main():
    class_cat="cat"
    class_dog="dog"
    
    cat_full_paths = get_full_paths(class_cat)
    cat_rel_paths = get_relative_paths(class_cat)
    dog_full_paths = get_full_paths(class_dog)
    dog_rel_paths = get_relative_paths(class_dog)
    
    with open('paths.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        for full_path, rel_path in zip(cat_full_paths, cat_rel_paths):
            writer.writerow([full_path, rel_path, class_cat])
        for full_path, rel_path in zip(dog_full_paths, dog_rel_paths):
            writer.writerow([full_path, rel_path, class_dog])

if __name__ == "__main__":
    main()