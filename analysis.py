import pandas as pd
import cv2
import os

#1,2 task
df = pd.read_csv('paths.csv', delimiter=',', usecols = (0, 2), names = ('AbsPath', 'Name'))
print(df.tail(5))


#3task
df["Mark"] = df["Name"].apply(lambda x: 0 if x == "cat" else 1)
print(df.head(5))


#4task
df["Height"] = df["AbsPath"].apply(lambda path: cv2.imread(path).shape[0])
df["Width"] = df["AbsPath"].apply(lambda path: cv2.imread(path).shape[1])
df["Depth"] = df["AbsPath"].apply(lambda path: cv2.imread(path).shape[2])
print(df.head(5))


#5task
print(df[df['Mark'] == 0]['Height'].describe())

print(df[df['Mark'] == 1]['Height'].describe())

print(df[df['Mark'] == 0]['Height'].describe())

print(df[df['Mark'] == 1]['Height'].describe())

print(df[df['Mark'] == 0]['Height'].describe())

print(df[df['Mark'] == 1]['Height'].describe())


#6Task
def filter_by_class(df: pd.DataFrame, class_mark: int):
    return df[df['Mark'] == class_mark]


if __name__ == '__main__':
    print(filter_by_class(df, 1))