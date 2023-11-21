import pandas as pd
import cv2
import matplotlib.pyplot as plt
import numpy as np

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


#7Task
def filter_whm(df:pd.DataFrame, class_mark: int,max_height: int,  max_width: int):
    return df[(df['Mark'] == class_mark) & (df['Height'] <= max_height) & (df['Width'] <= max_width)]


#8Task
def df_group(df: pd.DataFrame, class_name: int):
    df = filter_by_class(df, class_name)
    img_pixels = []
    for item in df['AbsPath']:
        img = cv2.imread(item)
        img_pixels.append(img.size)
    df['pixels'] = img_pixels
    df.groupby('pixels').count()
    print(df.pixels.describe())
    

#9Task
def create_histogram(df: pd.DataFrame, class_name:int):
    df = filter_by_class(df, class_name)
    df = df.sample()
    for item in df['AbsPath']:
        path = item
    img = cv2.imread(path)
    array = []
    for number in range(0, 3):
        hist = cv2.calcHist([img], [number], None, [256], [0, 256])
        array.append(hist)
    return array

#10Task
def histogram(df: pd.DataFrame, class_mark: int):
    hist = create_histogram(df, class_mark)
    plt.plot(hist[0], color='b')
    plt.plot(hist[1], color='g')
    plt.plot(hist[2], color='r')
    plt.title('Image Histogram For Blue, Green, Red Channels')
    plt.xlabel("Intensity")
    plt.ylabel("Number of pixels")
    plt.show()


if __name__ == '__main__':
    print(filter_by_class(df, 1))
    print(filter_whm(df,0, 427, 300))
    df_group(df, 1)
    histogram(df, 1)
