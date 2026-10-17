""""
=======================phase1.py========================
Inspiration: ECO101 Principles of Microeconomics

Problem: How Uzbekistan's Economy Developed Between 1997 And 2025 In International Market?
Sub-Questions:
            1. How has the value of Uzbekistan’s exports evolved during the given period?
            2. How has Uzbekistan’s spending on imported goods and services changed?
            3. How much more or less foreign direct investment has Uzbekistan attracted?

Dataset: World_Bank_Data_Uzbekistan.csv
https://data.worldbank.org/country/uzbekistan

Programmed by Nurmuhammad Mirzaahmadov for CSC108 Phase 1

Disclaimer: No AI was used in writing, researching, designing, coding, or making this project
All my progress can be seen in my GitHub repository if necessary
https://github.com/Runnp/uoft-csc108-fall-cool-project.git

"""

import csv
file = "/Users/runnp/PycharmProjects/uoft-csc108-fall-cool-project/World_Bank_Data_Uzbekistan.csv"
with open(file, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    csv_file.readline()
    for line in csv_reader:

