import pprint
import matplotlib.pyplot as plt
import re
import csv

def extrNum (str):
    nums = re.findall(r'\b\d+\b', str)
    if (nums):
        return nums[0]
    else:
        return 0

with open("geri-data.csv") as f:
    lines = f.readlines()
    
    # get header values with indexes
    for key, value in enumerate(lines[0].split(";")):
        print(key, value)

    services = {}
    header_row = lines[0].split(';')
    conc_header_row = lines[0].split(";")[16:23]

    for index, line in enumerate(lines):
        values = line.split(";")
        conc_values = values[16:23]
        
        for index, val in enumerate(conc_values):
            print(index,val)
            if (index < 7):
                if (conc_header_row[index] not in services.keys()):
                    #print("Assignee: "+ str(services[conc_header_row[index]]) + " assigned: " + str(val))
                    services[conc_header_row[index]] = int(val)
                else:
                    print("Assignee: "+ str(services[conc_header_row[index]]) + " assigned: " + str(val))
                    services[conc_header_row[index]] += int(val)
            
    pprint.pprint(services)
    



'''
    for index in range(len(list_earnings)):
        print(str(list_earnings[index]) + "\t" + str(list_interestInShowroom[index]))

    plt.scatter(list_interestInShowroom, list_earnings, s=10)

    plt.show()
'''
