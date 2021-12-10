import requests
import pathlib
import sys
import os

base_url = "https://www.mppi.mp.br/internet/wp-content/uploads//"

def convert_month(month):
    months = {
        "01": "janeiro",
        "02": "fevereiro",
        "03": "maro",
        "04": "abril",
        "05": "maio",
        "06": "junho",
        "07": "julho",
        "08": "agosto",
        "09": "setembro",
        "10": "outubro",
        "11": "novembro",
        "12": "dezembro",
    }
    return months[month]


def cod_2018(month):
    cod = {
        "01": "03",
        "02": "03",
        "03": "05",
        "04": "06",
        "05": "06",
        "06": "08",
        "07": "09",
        "08": "10",
        "09": "11",
        "10": "12",
        "11": "01",
        "12": "01",
    }
    return cod[month]


def cod_2019(month):
    cod = {
        "01": "03",
        "02": "04",
        "03": "05",
        "04": "05",
        "05": "07",
        "06": "08",
        "07": "09",
        "08": "10",
        "09": "11",
        "10": "12",
        "11": "12",
        "12": "01",
    }
    return cod[month]


def cod_2020(month):
    cod = {
        "01": "03",
        "02": "04",
        "03": "05",
        "04": "07",
        "05": "07",
        "06": "08",
        "07": "09",
        "08": "10",
        "09": "11",
        "10": "12",
        "11": "12",
        "12": "01",
    }
    return cod[month]


def cod_2021(month):
    cod = {
        "01": "02",
        "02": "03",
        "03": "04",
        "04": "05",
        "05": "06",
        "06": "07",
        "07": "08",
        "08": "10",
        "09": "10",
        "10": "12",
        "11": "",
        "12": "",
    }

    return cod[month]

def cod_2021_indemmit(month):
    cod = {
        "01": "02",
        "02": "03",
        "03": "05",
        "04": "05",
        "05": "06",
        "06": "07",
        "07": "08",
        "08": "10",
        "09": "10",
        "10": "12",
        "11": "",
        "12": "",
    }

    return cod[month]
        
# Generate endpoints able to download
def links_remuneration(month, year):
    month = month.zfill(2)  # Deixa o mês com dois digitos
    links_type = {}
    link = ""
    if year == "2018":
        if month in ["01", "02", "03", "04", "05", "06"]:

            link = (
                base_url
                + year
                + "/"
                + cod_2018(month)
                + "/"
                + "financeiro%20membros%20ativos%20"
                + convert_month(month)
                + "%20"
                + year
                + ".ods"
            )
        elif month == "07":
            link = (
                base_url
                + year
                + "/"
                + cod_2018(month)
                + "/"
                + "membros_ativos_"
                + month
                + "_"
                + year
                + ".ods"
            )
        elif month == "08":
            link = (
                base_url
                + year
                + "/"
                + cod_2018(month)
                + "/membros_ativos-"
                + convert_month(month)
                + "%20de%20"
                + year
                + "-retificado"
                + ".ods"
            )
        elif month == "09":
            link = (
                base_url
                + year
                + "/"
                + cod_2018(month)
                + "/membros_ativos%20-%20"
                + convert_month(month)
                + "%20-%20"
                + year
                + ".ods"
            )
        elif month == "10":
            link = (
                base_url
                + year
                + "/"
                + cod_2018(month)
                + "/membros_ativos-"
                + convert_month(month)
                + "%20de%20"
                + year
                + ".ods"
            )
        elif month == "11":
            link = (
                base_url
                + "2019/"
                + cod_2018(month)
                + "/membros_ativos_"
                + convert_month(month)
                + "%20"
                + year
                + ".ods"
            )

        elif month == "12":
            link = (
                base_url
                + "2019/"
                + cod_2018(month)
                + "/membros_ativos_dez_"
                + year
                + ".ods"
            )
    elif year == "2019":
        if month in ["01", "02"]:
            link = (
                base_url
                + year
                + "/"
                + cod_2019(month)
                + "/membros_ativos_"
                + convert_month(month)[0:3]
                + "_"
                + year[2:]
                + ".ods"
            )
        elif month in ["03", "06"]:
            link = (
                base_url
                + year
                + "/"
                + cod_2019(month)
                + "/membros%20ativos_"
                + month
                + "_"
                + year[2:]
                + ".ods"
            )
        elif month in ["04", "05", "08", "09", "11"]:
            link = (
                base_url
                + year
                + "/"
                + cod_2019(month)
                + "/membros_ativos_"
                + month
                + "_"
                + year[2:]
                + ".ods"
            )
        elif month == "07":
            link = (
                base_url
                + year
                + "/"
                + cod_2019(month)
                + "/geral_membros_ativos_"
                + month
                + "_"
                + year
                + ".ods"
            )
        elif month == "10":
            link = (
                base_url
                + year
                + "/"
                + cod_2019(month)
                + "/membros_ativos_"
                + month
                + "_"
                + year
                + "-retificada.ods"
            )
        elif month == "12":
            link = (
                base_url
                + "2020/"
                + cod_2019(month)
                + "/membros_ativos_"
                + month
                + "_"
                + year[2:]
                + ".ods"
            )
    elif year == "2020":
        if month in ["01", "02", "03", "04", "05", "06"]:
            link = (
                base_url
                + year
                + "/"
                + cod_2020(month)
                + "/membros_ativos_"
                + month
                + "_"
                + year
                + ".ods"
            )
        elif month == "07":
            link = (
                base_url
                + year
                + "/"
                + cod_2020(month)
                + "/Remuneracao-de-todos-os-membros-ativos-%E2%80%93-"
                + convert_month(month)
                + "-"
                + year
                + ".ods"
            )
        elif month in ["08", "09", "10", "11"]:
            link = (
                base_url
                + year
                + "/"
                + cod_2020(month)
                + "/Remuneracao-de-todos-os-membros-ativos-%E2%80%93-"
                + convert_month(month)
                + "-%E2%80%93-"
                + year
                + ".ods"
            )
        elif month == "12":
            link = (
                base_url
                + "2021/"
                + cod_2020(month)
                + "/Remuneracao-de-todos-os-membros-ativos-%E2%80%93-"
                + convert_month(month)
                + "-%E2%80%93-"
                + year
                + ".ods"
            )
    elif year == "2021":
        if month in ["01", "02", "03", "04", "05", "06", "07", "08", "09"]:
            mon = "marco" if convert_month(month) == "maro" else convert_month(month)
            link = (
                base_url
                + year
                + "/"
                + cod_2021(month)
                + "/Remuneracao-de-todos-os-membros-ativos-%E2%80%93-"
                + mon
                + "-%E2%80%93-"
                + year
                + ".ods"
            )
    links_type["Membros ativos"] = link
    return links_type


def links_other_funds(month, year):
    link = ""
    month = month.zfill(2)  # Deixa o mês com dois digitos
    links_type = {}
    if year == "2019":
        if month == "07":
            link = (
                base_url
                + year
                + "/"
                + cod_2019(month)
                + "/indenizatorias_membros_"
                + month
                + "_"
                + year
                + ".ods"
            )
            links_type["Membros ativos"] = link
        elif month == "08":
            link = (
                base_url
                + year
                + "/"
                + cod_2019(month)
                + "/indenizatorias_membros_"
                + month
                + "_"
                + year[2:]
                + ".ods"
            )
            links_type["Membros ativos"] = link
        elif month in ["09", "10", "11"]:
            link = (
                base_url
                + year
                + "/"
                + cod_2019(month)
                + "/verbas_indenizatorias_membros_"
                + month
                + "_"
                + year[2:]
                + ".ods"
            )
            links_type["Membros ativos"] = link
        elif month == "12":
            link = (
                base_url
                + "2020/"
                + cod_2019(month)
                + "/verbas_indenizatorias_membros_"
                + month
                + "_"
                + year[2:]
                + ".ods"
            )
            links_type["Membros ativos"] = link

    elif year == "2020":
        if month in ["01", "02", "03", "04", "05"]:
            link = (
                base_url
                + year
                + "/"
                + cod_2020(month)
                + "/verbas_indenizatorias_membros_"
                + month
                + "_"
                + year
                + ".ods"
            )
            links_type["Membros ativos"] = link
        elif month == "06":
            link = (
                base_url
                + year
                + "/"
                + cod_2020(month)
                + "/Verbas-Indenizat%C3%B3rias-e-Outras-Remunera%C3%A7%C3%B5es-Tempor%C3%A1rias-%E2%80%93-Membros-%E2%80%93-Junho-de-2020"
                + ".ods"
            )
            links_type["Membros ativos"] = link

        elif month in ["07", "08", "09", "10", "11"]:
            link = (
                base_url
                + year
                + "/"
                + cod_2020(month)
                + "/Verbas-Indenizatorias-e-Outras-Remuneracoes-Temporarias-%E2%80%93-Membros-%E2%80%93-"
                + convert_month(month)
                + "-de-"
                + year
                + ".ods"
            )
            links_type["Membros ativos"] = link
        elif month == "12":
            link = (
                base_url
                + "2021/"
                + cod_2020(month)
                + "/Verbas-Indenizatorias-e-Outras-Remuneracoes-Temporarias-%E2%80%93-Membros-%E2%80%93-"
                + convert_month(month)
                + "-de-"
                + year
                + ".ods"
            )
            links_type["Membros ativos"] = link
    elif year == "2021":
        if month in ["01", "02", "03", "04", "05", "06", "07", "08"]:
            mon = "marco" if convert_month(month) == "maro" else convert_month(month)
            link = (
                base_url
                + year
                + "/"
                + cod_2021_indemmit(month)
                + "/Verbas-Indenizatorias-e-Outras-Remuneracoes-Temporarias-%E2%80%93-Membros-%E2%80%93-"
                + mon
                + "-de-"
                + year
                + ".ods"
            )
            links_type["Membros ativos"] = link

        elif month in ["09"]:
            link = (
                base_url 
                + year
                + "/"
                + cod_2021(month)
                + "/VERBAS1.ods"
            )
            links_type["Membros ativos"] = link

    return links_type


def download(url, file_path):
    try:
        response = requests.get(url, allow_redirects=True)
        with open(file_path, "wb") as file:
            file.write(response.content)
        file.close()
    except Exception as excep:
        sys.stderr.write(
            f"Não foi possível fazer o download do arquivo: {file_path}. O seguinte erro foi gerado: {excep}"
        )
        sys.exit(1)


# Crawl retrieves payment files from MPDFT.
def crawl(year, month, output_path):
    urls_remuneration = links_remuneration(month, year)
    urls_other_funds = links_other_funds(month, year)
    files = []
    for element in urls_remuneration:
        pathlib.Path(output_path).mkdir(exist_ok=True)
        file_name = f"membros-ativos-contracheque-{month.zfill(2)}-{year}.ods"
        file_path = output_path + "/" + file_name
        if urls_remuneration[element] == "":
            sys.stderr.write(f"Não existe planilha para {month}/{year}")
            sys.exit(4)
        download(urls_remuneration[element], file_path)
        files.append(file_path)

    for element in urls_other_funds:
        pathlib.Path(output_path).mkdir(exist_ok=True)
        file_name_indemnity = f"membros-ativos-verbas-indenizatorias-{month.zfill(2)}-{year}.ods"
        file_path_indemnity = output_path + "/" + file_name_indemnity
        download(urls_other_funds[element], file_path_indemnity)
        files.append(file_path_indemnity)

    return files
