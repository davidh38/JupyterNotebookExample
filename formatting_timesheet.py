
import os

with open('test.csv') as file:
    data = file.readlines()
    #data = data.replace(os.linesep, ',')
    for (index, item) in enumerate(data):
        print(index)
        if (index == 0):
           data[index] = item.replace(os.linesep, ',')
        if not(index % 7 == 6):
            data[index] = item.replace(os.linesep, ',')
    #print(data)
    data = ''.join(data)
    with open("Output.txt", "w") as text_file:
        text_file.write(data)
