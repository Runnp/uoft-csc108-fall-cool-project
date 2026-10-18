""""
=======================phase1.py========================
Assalomu Aleykum!
Inspiration: ECO101 Principles of Microeconomics.
--------------------------------------------------------
Dataset: World_Bank_Data_Uzbekistan.csv
Link: https://data.worldbank.org/country/uzbekistan
Note: The dataset comes in archive with three files:
* Metadata_Country_API_UZB_DS2_en_csv_v2_385286.csv
* API_UZB_DS2_en_csv_v2_385286.csv - IMPORTANT: We are using this file ONLY
* Metadata_Indicator_API_UZB_DS2_en_csv_v2_385286.csv

We have real data only in API_UZB_DS2_en_csv_v2_385286.csv, which I renamed into World_Bank_Data_Uzbekistan.csv
In other two files, Metadata_Indicator_API_UZB_DS2_en_csv_v2_385286.csv includes explanations and meanings of each
indicator code inside our World_Bank_Data_Uzbekistan.csv. However, I put those indicators inside this program:
IMPORTANT:
NE.EXP.GNFS.CD - Exports of goods and services
NE.IMP.GNFS.CD - Imports of goods and services
BX.KLT.DINV.CD.WD - Foreign direct investment, net inflows
Notice: These values are calculated in USD currency and are not inflation-adjusted.
--------------------------------------------------------
Problem: How Uzbekistan's Economy Developed Between 1997 And 2025 In International Market?
Sub-Questions:
1. How has the value of Uzbekistan’s exports evolved during the given period?
2. How has Uzbekistan’s spending on imported goods and services changed?
3. How much more or less foreign direct investment has Uzbekistan attracted?
--------------------------------------------------------

Programmed by Nurmuhammad Mirzaahmadov for CSC108 Phase 1
=======================Thanks you========================
"""

import csv
csv_file = "/Users/runnp/PycharmProjects/uoft-csc108-fall-cool-project/World_Bank_Data_Uzbekistan.csv"

