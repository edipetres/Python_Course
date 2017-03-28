import os
import csv
import pprint
import webget
from urllib.parse import urlparse


kk_data_url = 'http://data.kk.dk/dataset/76ecf368-bf2d' \
    '-46a2-bcf8-adaf37662528/resource/9286af17' \
              '-f74e-46c9-a428-9fb707542189/download/' \
              'befkbhalderstatkode.csv'


def download(url):
    webget.download(url)
    f_name = os.path.basename(urlparse(url).path)
    f_name = os.path.join('.', f_name)
    return f_name


def read_data(filename):
    data = []
    
    with open(filename) as f:
        reader = csv.reader(f)
        _ = next(reader)
        
        for row in reader:
            data.append(row)
        
    return data


def csv_to_dict(data):
    data_dict = {}
    
    for row in data:
        # AAR,BYDEL,ALDER,STATKODE,PERSONER
        # header from CSV file
        year, neigh, age, code, amount = row
        
        year, neigh, age, code, amount = (int(year), int(neigh), 
                                          int(age), int(code), int(amount))

        if data_dict:
            if year in data_dict.keys():
                if neigh in data_dict[year].keys():
                    if age in data_dict[year][neigh].keys():
                        if code in data_dict[year][neigh][age].keys():
                            print('Error!')
                            raise Exception('No well formed CSV file.')
                        else:
                            data_dict[year][neigh][age][code] = amount    
                    else:
                        data_dict[year][neigh][age] = {code: amount}
                else:
                    data_dict[year][neigh] = {age: {code: amount}}
            else:
                data_dict[year] = {neigh: {age: {code: amount}}}
        else:
            data_dict = {year: {neigh: {age: {code: amount}}}}
        
    return data_dict


def write_data(data_dict):
    with open('./kkdata.py', 'w') as out_file:
        out_file.write('STATISTICS =' + pprint.pformat(data_dict))


filename = download(kk_data_url)
data = read_data(filename)
data_dict = csv_to_dict(data)
write_data(data_dict)