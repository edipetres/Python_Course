import webget
import os
import csv
import pprint

if(os.path.isfile("befkbhalderstatkode.csv")):
    print("File found.")
else:
    print("File not found; downloading...")
    url = "http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv"
    webget.download(url)

# 
def dictMaker(tempDict, values, index):
    keyToInsert = values[index]
    # Sort of a base case:
    if(index >= len(values) - 2):
        tempDict[keyToInsert] = values[index+1]
        return
    if(keyToInsert not in tempDict.keys()):
        tempDict[keyToInsert] = {}
        return tempDict[keyToInsert]
    else:
        return tempDict[keyToInsert]


dictn = {}
filename = "befkbhalderstatkode.csv"
# filename = "test.csv"
with open(filename) as data_file:
    reader = csv.reader(data_file)
    header_row = next(reader)
    for line in reader:
        workingDict = dictn
        for index in range(len(line) - 1):
            workingDict = dictMaker(workingDict, line, index)

# pprint.pprint(dictn)
print("keys: " + str(dictn.keys()))

with open('./kkdata.py', 'w') as out_file:
    out_file.write('STATISTICS = ' + pprint.pformat(dictn))
    print("Data saved to " + out_file.name)

# f = './befkbhalderstatkode.csv'
# reader = csv.reader(f)
# header_row = next(reader)
# for row in reader:
#     data.append(row)
#     assert kkdata.STATISTICS[row[0]][row[1]][row[2]][row[3]] == [row[4]]
