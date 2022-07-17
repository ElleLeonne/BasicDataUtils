# import required module
import os
import re

convo_list = []
directory = 'txt files'

for filename in os.listdir(directory): #for each file in folder
    with open(directory+"/"+filename, newline = '', encoding="latin1") as adataset: #open that file
        for line in adataset: #then for each line in that folder
            line = line.split('\t') #split on tab whitespace
            for a in line:
                convo_list.append(a.rstrip()) #then append it (without trailing whitespace) to master list

with open('output.txt', mode='w+', encoding='utf-8') as myfile: #write to output file, line by line
    for i in convo_list:
        myfile.write(i+'\n')