import csv
import numpy as np

with open('data2.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile) 
    for row in csvreader:
    col_num = np.shape(numpy_array)[0]
    print(col_num)
    ratio = 0.5
    s = int(col_num * ratio)
    random_indices = np.random.choice(col_num, size=s, replace=False)
    random_rows = numpy_array[random_indices, :]
    print(np.shape(random_rows))

with open("data_condensed.csv", 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerows(random_rows) 


with open("data_condensed.csv", 'r') as csvfile: 
    numpy_array = np.loadtxt(csvfile, delimiter=",")
    print(np.shape(numpy_array))