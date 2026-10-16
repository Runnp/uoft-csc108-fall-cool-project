""""
Uzbekistan's Economy in International Market:
Trends and Trade Balance Between 1997-2025

How did Uzbekistan’s international trade evolve as a share of GDP?

How did foreign direct investment vary relative to Uzbekistan's economy?

How did Uzbekistan’s inflation-adjusted GDP per person change?
"""

import csv
file = "/Users/runnp/PycharmProjects/uoft-csc108-fall-cool-project/World_Bank_Data_Uzbekistan.csv"

with open(file, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    csv_file.readline()
    for line in csv_reader:

