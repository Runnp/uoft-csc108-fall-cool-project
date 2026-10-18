""""
=======================phase1.py========================
Assalomu Aleykum!
Inspiration: ECO101 Principles of Microeconomics.
---------------------------------------------------------
Problem: How Uzbekistan's Economy Developed Between 1997 And 2025 In International Market?
Sub-Questions:
1. How has the value of Uzbekistan’s exports evolved during the given period?
2. How has Uzbekistan’s spending on imported goods and services changed?
3. How much more or less foreign direct investment has Uzbekistan attracted?
Problem Decomposition Functions:
1. read_data - read and open csv file
2. calculate_investment_value - count investment value
3. calculate_export_value - calculate export value of domestic goods and services
4. calculate_import_value - calculate import value of goods and services produced abroad
5. run_analysis - print a clear answer to research questions with outputs from functions above
My diagram represents inputs, outputs, descriptions in more detail. Refer to Diagram Uzbekistan Economy.jpg
---------------------------------------------------------
Dataset: World_Bank_Data_Uzbekistan.csv
Link: https://data.worldbank.org/country/uzbekistan
Note: The dataset comes in archive with three files:
* Metadata_Country_API_UZB_DS2_en_csv_v2_385286.csv
* API_UZB_DS2_en_csv_v2_385286.csv - IMPORTANT: We are using this file ONLY
* Metadata_Indicator_API_UZB_DS2_en_csv_v2_385286.csv
We have real data only in API_UZB_DS2_en_csv_v2_385286.csv, which I renamed into World_Bank_Data_Uzbekistan.csv
From other two files, Metadata_Indicator_API_UZB_DS2_en_csv_v2_385286.csv includes explanations and meanings of every
indicator codes inside our World_Bank_Data_Uzbekistan.csv. However, I put the needed indicators inside this program:
IMPORTANT:
NE.EXP.GNFS.CD - Exports of goods and services
NE.IMP.GNFS.CD - Imports of goods and services
BX.KLT.DINV.CD.WD - Foreign direct investment, net inflows
Notice: These values are calculated in USD currency and are not inflation-adjusted.
---------------------------------------------------------
Disclaimer: No AI was used in writing, designing, and programing this project.
The progress can be seen in my GitHub repository for this course, if necessary.
https://github.com/runnp/uoft-csc108-fall-cool-project.git
---------------------------------------------------------
Programmed by Nurmuhammad Mirzaahmadov for CSC108 Phase 1
=======================Thanks you========================
"""

import csv
csv_file = "/Users/runnp/PycharmProjects/uoft-csc108-fall-cool-project/World_Bank_Data_Uzbekistan.csv"

def read_data(csv_file: str, indicator_code: str) -> tuple:
    """
    Returns years and values for the given indicator.
    Skip missing years and empty values.
    >>> years, values = read_data(csv_file, "NE.EXP.GNFS.CD")
    >>> len(years) == len(values)
    True
    >>> years, values = read_data(csv_file, "NE.IMP.GNFS.CD")
    >>> len(years) == len(values)
    True
    >>> years, values = read_data(csv_file, "BX.KLT.DINV.CD.WD")
    >>> len(years) == len(values)
    True
    >>> years[0] >= 1997
    True
    >>> years[-1] <= 2025
    True
    """
    years = []
    values = []
    with open(csv_file, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)

        for i in range(4):
            next(reader)

        header = next(reader)

        for row in reader:
            if row[3] == indicator_code:
                for i in range(4, len(header)):
                    year = header[i]
                    value = row[i]
                    if year.isdigit():
                        if 1997 <= int(year) <= 2025:
                            if value != "":
                                years.append(int(year))
                                values.append(float(value))
    return years, values

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)