""""
=======================phase1.py========================
Assalomu Aleykum!
Inspiration: ECO101 Principles of Microeconomics.
---------------------------------------------------------
Problem: How Uzbekistan's Economy Developed Between 1997
And 2025 In International Market?
Sub-Questions:
1. How has the value of Uzbekistan’s exports evolved
during the given period?
2. How has Uzbekistan’s spending on imported goods and
services changed?
3. How much more or less foreign direct investment has
Uzbekistan attracted?

Problem Decomposition Functions:
1. read_data - read and open csv file
2. calculate_investment_value - count investment value
3. calculate_export_value - calculate export value of domestic
goods and services
4. calculate_import_value - calculate import value of goods
and services produced abroad
5. run_analysis - print a clear answer to research questions with
outputs from functions above
My diagram represents inputs, outputs, descriptions in more detail.
Refer to decomp_image.png
---------------------------------------------------------
Dataset: World_Bank_Data_Uzbekistan.csv
Source: World Bank Open Data
Link: https://data.worldbank.org/country/uzbekistan
Note: The dataset comes in archive with three files:
* Metadata_Country_API_UZB_DS2_en_csv_v2_385286.csv
* API_UZB_DS2_en_csv_v2_385286.csv
* Metadata_Indicator_API_UZB_DS2_en_csv_v2_385286.csv
IMPORTANT: We have real data only in API_UZB_DS2_en_csv_v2_385286.csv
that I renamed into World_Bank_Data_Uzbekistan.csv for clearness.

From other two files, Metadata_Indicator_API_UZB_DS2_en_csv_v2_385286.csv
includes explanations and meanings of every indicator codes inside our
World_Bank_Data_Uzbekistan.csv.

However, I put the needed indicators inside this program:
IMPORTANT:
NE.EXP.GNFS.CD - Exports of goods and services
NE.IMP.GNFS.CD - Imports of goods and services
BX.KLT.DINV.CD.WD - Foreign direct investment, net inflows
Notice: These values are calculated in USD currency, not inflation-adjusted.
---------------------------------------------------------
Programmed by Nurmuhammad Mirzaahmadov for CSC108 Phase 1
=======================Thank you=========================
"""

import csv
CSV_FILE = (
    "/Users/runnp/PycharmProjects/uoft-csc108-fall-cool-project/"
    "World_Bank_Data_Uzbekistan.csv"
)
INVESTMENT_CODE = "BX.KLT.DINV.CD.WD"
EXPORT_CODE = "NE.EXP.GNFS.CD"
IMPORT_CODE = "NE.IMP.GNFS.CD"


def read_data(filename: str, indicator_code: str) -> tuple:
    """
    Returns years and values for the given indicator.
    Skip missing years and empty values.
    >>> years, values = read_data(CSV_FILE, "NE.EXP.GNFS.CD")
    >>> len(years) == len(values)
    True
    """
    years = []
    values = []
    selected_row = []

    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)

        for i in range(4):
            next(reader)

        header = next(reader)

        for row in reader:
            if row[3] == indicator_code:
                selected_row = row
                break

    for i in range(4, len(header)):
        year = header[i]
        value = selected_row[i]
        if (year.isdigit() and 1997 <= int(year) <= 2025
                and value != ""):
            years.append(int(year))
            values.append(float(value))
    return years, values


def calculate_investment_value(years: list, investment_values: list,
                               start_year: int, end_year: int) -> tuple:
    """
    Returns the change in investment values between two years.
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


def calculate_export_value(years: list, export_values: list, start_year: int,
                           end_year: int) -> tuple:
    """
    Returns starting, ending, and change in export values between two years.
    """
    start_index = years.index(start_year)
    end_index = years.index(end_year)

    start_value = export_values[start_index]
    end_value = export_values[end_index]

    change_exports = end_value - start_value
    return start_value, end_value, change_exports


def calculate_import_value(years: list, export_values: list,
                           start_year: int, end_year: int) -> tuple:
    """
    Returns starting, ending, and change in import values between two years.
    """
    start_index = years.index(start_year)
    end_index = years.index(end_year)

    start_value = export_values[start_index]
    end_value = export_values[end_index]

    change_imports = end_value - start_value
    return start_value, end_value, change_imports


def run_analysis(filename: str, start_year: int, end_year: int) -> None:
    """
    Renders Uzbekistan's change in economic data between two years.
    Visualizes the findings in text bar chart.
    Each block represents approximately $1 billion.
    Positive values below $1 billion are shown as one block.
    """
    investment_years, investments = read_data(filename, INVESTMENT_CODE)
    investment_result = calculate_investment_value(
        investment_years, investments, start_year, end_year
    )

    export_years, export_values = read_data(filename, EXPORT_CODE)
    export_result = calculate_export_value(export_years, export_values,
                                           start_year, end_year)

    import_years, import_values = read_data(filename, IMPORT_CODE)
    import_result = calculate_import_value(import_years, import_values,
                                           start_year, end_year)

    print("UZBEKISTAN'S ECONOMY IN INTERNATIONAL MARKET")
    print("Period:", start_year, "-", end_year)

    print("\nFOREIGN DIRECT INVESTMENT")
    print("Initial value: $", investment_result[0])
    print("Final value: $", investment_result[1])
    print(start_year, ":", "█" * max(1, int(investment_result[0]
                                            / 1_000_000_000)))
    print(end_year, ":", "█" * int(investment_result[1] / 1_000_000_000))
    print("Dollar change: $", investment_result[2])

    print("\nEXPORTS")
    print("Initial value: $", export_result[0])
    print("Final value: $", export_result[1])
    print(start_year, ":", "█" * int(export_result[0] / 1_000_000_000))
    print(end_year, ":", "█" * int(export_result[1] / 1_000_000_000))
    print("Dollar change: $", export_result[2])

    print("\nIMPORTS")
    print("Initial value: $", import_result[0])
    print("Final value: $", import_result[1])
    print(start_year, ":", "█" * int(import_result[0] / 1_000_000_000))
    print(end_year, ":", "█" * int(import_result[1] / 1_000_000_000))
    print("Dollar change: $", import_result[2])

    print("\nANSWERS TO RESEARCH QUESTIONS")
    print("How has the value of Uzbekistan’s exports evolved during the"
          " given period?")
    print("- Uzbekistan's exports of goods and services increased from",
          round(export_result[0] / 1_000_000_000, 2),
          "billion USD in", start_year, "to",
          round(export_result[1] / 1_000_000_000, 2),
          "billion USD in", str(end_year) + ".")
    print("This represents an increase of",
          round(export_result[2] / 1_000_000_000, 2), "billion USD.")
    print("By", end_year, "exports were approximately",
          round(export_result[1] / export_result[0], 1),
          "times their", start_year, "value.")

    print("\nHow has Uzbekistan’s spending on imported goods and services "
          "changed?")
    print("- Uzbekistan's spending on imported goods and services increased "
          "from",
          round(import_result[0] / 1_000_000_000, 2),
          "billion USD in", start_year, "to",
          round(import_result[1] / 1_000_000_000, 2),
          "billion USD in", str(end_year) + ".")
    print("This renders an increase of",
          round(import_result[2] / 1_000_000_000, 2),
          "billion USD.")
    print("By", end_year, "imports were approximately",
          round(import_result[1] / import_result[0], 1),
          "times their", start_year, "value.")

    print("\nHow much more or less foreign direct investment has Uzbekistan "
          "attracted?")
    print("- Uzbekistan's annual foreign direct investment net inflows"
          " increased from",
          round(investment_result[0] / 1_000_000, 2),
          "million USD in", start_year, "to",
          round(investment_result[1] / 1_000_000_000, 2),
          "billion USD in", str(end_year) + ".")
    print("This illustrates an increase of",
          round(investment_result[2] / 1_000_000_000, 2),
          "billion USD.")
    print("By", end_year, "foreign direct investment net inflows were "
                          "approximately",
          round(investment_result[1] / investment_result[0], 1),
          "times their", start_year, "value.")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_analysis(CSV_FILE, 1997, 2025)
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['csv'],
        'allowed-io': ['read_data', 'run_analysis'],
    })
