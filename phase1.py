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
INVESTMENT_CODE = "BX.KLT.DINV.CD.WD"
EXPORT_CODE = "NE.EXP.GNFS.CD"
IMPORT_CODE = "NE.IMP.GNFS.CD"

def read_data(filename: str, indicator_code: str) -> tuple:
    """
    Returns years and values for the given indicator.
    Skip missing years and empty values.
    >>> years, values = read_data(csv_file, "NE.EXP.GNFS.CD")
    >>> len(years) == len(values)
    True
    """
    years = []
    values = []
    with open(filename, "r", encoding="utf-8-sig") as file:
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


def calculate_investment_value(years: list, investment_values: list, start_year: int, end_year: int) -> tuple:
    """
    Returns the change in investment values between two years.
    Precondition: start_year and end_year are integers.
    >>> calculate_investment_value([1997, 2025], [100.0, 500.0], 1997, 2025)
    (100.0, 500.0, 400.0)
    >>> calculate_investment_value([1997, 2000], [300.0, 200.0], 1997, 2000)
    (300.0, 200.0, -100.0)
    """
    start_index = years.index(start_year)
    end_index = years.index(end_year)

    start_value = investment_values[start_index]
    end_value = investment_values[end_index]

    change = end_value - start_value

    return start_value, end_value, change


def calculate_export_value(years: list, export_values: list, start_year: int, end_year: int) -> tuple:
    """
    Returns starting, ending, and change in export values between two years.
    Precondition: start_year and end_year are integers.
    """
    start_index = years.index(start_year)
    end_index = years.index(end_year)

    start_value = export_values[start_index]
    end_value = export_values[end_index]

    change_exports = end_value - start_value
    return start_value, end_value, change_exports


def calculate_import_value(years: list, export_values: list, start_year: int, end_year: int) -> tuple:
    """
    Returns starting, ending, and change in import values between two years.
    Precondition: start_year and end_year are integers.
    """
    start_index = years.index(start_year)
    end_index = years.index(end_year)

    start_value = export_values[start_index]
    end_value = export_values[end_index]

    change_imports = end_value - start_value
    return start_value, end_value, change_imports


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    investment_years, investments = read_data(csv_file, INVESTMENT_CODE)
    export_years, export_values = read_data(csv_file, EXPORT_CODE)
    import_years, import_values = read_data(csv_file, IMPORT_CODE)

    start_year = 1997
    end_year = 2025

    if start_year in investment_years and end_year in investment_years:
        print("Investment: ", calculate_investment_value(investment_years, investments, start_year, end_year))
    else:
        print("Missing from the investment data...")

    if start_year in export_years and end_year in export_years:
        print("Exporting: ", calculate_export_value(export_years, export_values, start_year, end_year))
    else:
        print("Missing from the investment data...")

    if start_year in import_years and end_year in import_years:
        print("Importing: ", calculate_import_value(import_years, import_values, start_year, end_year))
    else:
        print("Missing from the investment data...")