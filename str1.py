import csv
import pandas


with open ("train.csv") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)


