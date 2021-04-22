import pandas as pd
from datetime import datetime
import math
import pathlib
import sys
import os
import parser_jun_18_backward
import parser_jul_aug_sept_dec_18
import parser_oct_nov_18_jan_to_jun19
import parser_jul19_forward
import parser_jul_to_dez_19_indemnity
import parser_jan20_forward_indemnity

# Read data downloaded from the crawler
def read_data(path):
    try:
        data = pd.read_excel(path, engine="odf")
        return data
    except Exception as excep:
        sys.stderr.write(
            "'Não foi possível ler o arquivo: "
            + path
            + ". O seguinte erro foi gerado: "
            + excep
        )
        os._exit(1)


# Strange way to check nan. Only I managed to make work
# Source: https://stackoverflow.com/a/944712/5822594
def isNaN(string):
    return string != string

def get_begin_row(rows):
    # Em algumas planilhas o campo row[0] é Nome e em outras é Matricula
    begin_string_case_1 = "Nome"
    begin_string_case_2 = "Matrícula"
    begin_row = 0
    for row in rows:
        begin_row += 1
        if row[0] in [begin_string_case_1, begin_string_case_2] or row[1] in [
            begin_string_case_1,
            begin_string_case_2,
        ]:
            break

    # We need to continue interate until wee a value that is not
    # whitespace. That happen due to the spreadsheet formatting.

    while isNaN(rows[begin_row][1]):
        begin_row += 1
    return begin_row


def get_end_row(rows, begin_row):
    end_string = "TOTAL"
    end_row = 0
    for row in rows:
        # First goes to begin_row.
        if end_row < begin_row:
            end_row += 1
            continue
        # Then keep moving until find a blank row.
        if end_string in str(row[0]) or end_string in str(
            row[1]
        ):  # Como existe planilhas com formato diferente, a palavra final pode alternar entre a coluna 0 e a coluna 1
            break
        end_row += 1
    end_row -= 1
    return end_row


def format_value(element):
    # A value was found with incorrect formatting. (3,045.99 instead of 3045.99)
    if isNaN(element):
        return 0.0
    if type(element) == str:
        if "." in element and "," in element:
            element = element.replace(".", "").replace(",", ".")
        elif "," in element:
            element = element.replace(",", ".")

    return float(element)


def parse(file_names, year, month):
    employees = {}
    for fn in file_names:
        if "Verbas Indenizatorias" not in fn:
            # Puts all parsed employees in the big map
            if year == "2018":
                if month in ["01", "02", "03", "04", "05", "06"]:
                    employees.update(
                        parser_jun_18_backward.parse_employees_jun18_backward(fn)
                    )
                elif month in ["07", "08", "09", "12"]:
                    employees.update(parser_jul_aug_sept_dec_18.parse_employees(fn))
                elif month in ["10", "11"]:
                    employees.update(parser_oct_nov_18_jan_to_jun19.parse_employees(fn))

            elif year == "2019":
                if month in ["01", "02", "03", "04", "05", "06"]:
                    employees.update(parser_oct_nov_18_jan_to_jun19.parse_employees(fn))
                else:
                    employees.update(parser_jul19_forward.parse_employees(fn))
            else:
                employees.update(parser_jul19_forward.parse_employees(fn))
    try:
        for fn in file_names:
            if "Verbas Indenizatorias" in fn:
                if year == "2019" and month in ["07", "08", "09", "10", "11", "12"]:
                    parser_jul_to_dez_19_indemnity.update_employee_indemnity(
                        fn, employees
                    )
                else:
                    parser_jan20_forward_indemnity.update_employee_indemnity(
                        fn, employees
                    )      
    except KeyError as e:
        sys.stderr.write(
            "Registro inválido ao processar verbas indenizatórias: {}".format(e)
        )
        os._exit(1)
    return list(employees.values())
