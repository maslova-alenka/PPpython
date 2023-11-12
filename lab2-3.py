import os
import shutil
import csv
import random
  
def main():

    if os.path.isdir('dataset3'):
        shutil.rmtree('dataset3')

    old_path = os.path.relpath('dataset2')
    new_path = os.path.relpath('dataset3')
    shutil.copytree(old_path, new_path)
    
    old=os.listdir(new_path)
    
    old_rel_paths = [os.path.join(old_path, name) for name in old]
    
    rand_num=random.sample(range(0,10001), len(old))
    
    new_name=[f'{num}.jpg' for num in rand_num]
    
    new_rel_paths = [os.path.join(new_path, name) for name in new_name]
    
    for old_names, new_names in zip(old_rel_paths, new_rel_paths):
        os.replace(old_names, new_names)
        
    new_full_paths = [os.path.join(os.path.abspath('dataset3'), name) for name in new_name]
    
    
    
    with open('paths3.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        for full_path, rel_path, old_rel_path in zip(new_full_paths, new_rel_paths,old_rel_paths):
            if 'cat' in old_rel_path:
                class_name ='cat'
            else:
                class_name= 'dog'  
            writer.writerow([full_path, rel_path, class_name])
    
    
    
    
    
if __name__ == "__main__":
    main()