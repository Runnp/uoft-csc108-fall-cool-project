""""
=======================phase1.py========================
Assalomu Aleykum!
Inspiration: ECO101 Principles of Microeconomics
--------------------------------------------------------
Problem: How Uzbekistan's Economy Developed Between 1997 And 2025 In International Market?

Sub-Questions: 1. How has the value of Uzbekistan’s exports evolved during the given period?
2. How has Uzbekistan’s spending on imported goods and services changed?
3. How much more or less foreign direct investment has Uzbekistan attracted?
--------------------------------------------------------
Dataset: World_Bank_Data_Uzbekistan.csv
Link: https://data.worldbank.org/country/uzbekistan
Note: The dataset comes in archive with three files:
* Metadata_Country_API_UZB_DS2_en_csv_v2_385286.csv
* API_UZB_DS2_en_csv_v2_385286.csv
* Metadata_Indicator_API_UZB_DS2_en_csv_v2_385286.csv
--------------------------------------------------------
IMPORTANT: For this program to operate,
We need only API_UZB_DS2_en_csv_v2_385286.csv that I renamed into World_Bank_Data_Uzbekistan.csv
--------------------------------------------------------
IMPORTANT: From other two files,
Metadata_Indicator_API_UZB_DS2_en_csv_v2_385286.csv includes explanations and meanings of each indicator code
inside our World_Bank_Data_Uzbekistan.csv. However, I copied down those indicators inside this program,
so there is no need for them and for another .csv.
--------------------------------------------------------
Notice: The numerical values are calculated in USD currency and are not inflation-adjusted
--------------------------------------------------------
Disclaimer: No AI was used in writing, researching, designing, coding, and making this project
All my progress can be seen in my GitHub repository if necessary:
https://github.com/runnp/uoft-csc108-fall-cool-project.git
--------------------------------------------------------
Programmed by Nurmuhammad Mirzaahmadov for CSC108 Phase 1
=======================Thanks you========================
"""

import csv
csv_file = "/Users/runnp/PycharmProjects/uoft-csc108-fall-cool-project/World_Bank_Data_Uzbekistan.csv"

