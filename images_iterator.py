import os
import csv

class Iterator:
    def __init__(self,class_name, dataset_name):
        self.dataset_name=dataset_name
        self.class_name =class_name
        self.data = os.listdir(os.path.join(dataset_name, self.class_name))
        self.counter=0
        self.limit=len(self.data)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.limit:
            next_path = os.path.join(self.dataset_name,self.class_name, self.data[self.counter])
            self.counter += 1
            return next_path
        else:
            return None
    

if __name__ == "__main__":
    cat=Iterator('cat','dataset')
    dog=Iterator('dog', 'dataset')
    
    print(next(cat))
    print(next(dog))
    print(next(cat))
    print(next(dog))
    print(next(cat))
    print(next(dog))