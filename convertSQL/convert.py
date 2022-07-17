import os
import re
import sqlite3

directory = 'source'

conn = sqlite3.connect('output.db')
c = conn.cursor()

#c.execute("""CREATE TABLE chat (
#            name text,
#            dialogue text
#            )""")


for filename in os.listdir(directory): #for each file in folder
    with open(directory+"/"+filename, newline = '', encoding="latin1") as adataset: #open that file
        for line in adataset: #then for each line in that folder
            line = line.split(': ', 1) #split on first colon+space
            c.execute("INSERT INTO chat (name,dialogue) VALUES (?,?)", (line[0], line[1]))

conn.commit()
conn.close()


        
