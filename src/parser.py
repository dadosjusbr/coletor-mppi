# coding: utf8
import sys
import os

from coleta import coleta_pb2 as Coleta

from headers_keys import (CONTRACHEQUE_JUL_AUG_SEPT_DEC_18,
                          CONTRACHEQUE_JUL19_FORWARD,
                          CONTRACHEQUE_JUN_18_BACKWARD,
                          CONTRACHEQUE_OCT_NOV_18_JAN_TO_JUN19,
                          INDENIZACOES_JAN20_FORWARD,
                          INDENIZACOES_JUL_TO_DEZ_19, HEADERS)
import number


def parse_employees(fn, chave_coleta, categoria):
    employees = {}
    counter = 1
    for row in fn:
        matricula = row[1]
        name = row[3]
        function = "-" if number.is_nan(row[5]) else row[5]
        if categoria == CONTRACHEQUE_JUN_18_BACKWARD:
            name = row[0]
            function = "-" if number.is_nan(row[1]) else row[1]

        if name == "TOTAL GERAL":
            break
        if not number.is_nan(name) and not number.is_nan(matricula) and name != "0" and name != "Nome":
            membro = Coleta.ContraCheque()
            membro.id_contra_cheque = chave_coleta + "/" + str(counter)
            membro.chave_coleta = chave_coleta
            membro.nome = name
            if categoria != CONTRACHEQUE_JUN_18_BACKWARD:
                membro.matricula = matricula
            membro.funcao = function
            membro.tipo = Coleta.ContraCheque.Tipo.Value("MEMBRO")
            membro.ativo = True
            
            membro.remuneracoes.CopyFrom(
                cria_remuneracao(row, categoria)
            )
          
            if categoria == CONTRACHEQUE_JUN_18_BACKWARD:
                employees[name] = membro
            else:
                employees[matricula] = membro
            counter += 1
            
    return employees


def cria_remuneracao(row, categoria):
    remu_array = Coleta.Remuneracoes()
    items = list(HEADERS[categoria].items())
    for i in range(len(items)):
        key, value = items[i][0], items[i][1]
        remuneracao = Coleta.Remuneracao()
        remuneracao.natureza = Coleta.Remuneracao.Natureza.Value("R")
        remuneracao.categoria = categoria
        remuneracao.item = key
        # Caso o valor seja negativo, ele vai transformar em positivo:
        remuneracao.valor = float(abs(number.format_value(row[value])))

        if categoria == CONTRACHEQUE_JUL_AUG_SEPT_DEC_18 and value in [16, 17, 18]:
            remuneracao.valor = remuneracao.valor * (-1)
            remuneracao.natureza = Coleta.Remuneracao.Natureza.Value("D")
        elif categoria == CONTRACHEQUE_JUL19_FORWARD and value in [18, 19, 20]:
            remuneracao.valor = remuneracao.valor * (-1)
            remuneracao.natureza = Coleta.Remuneracao.Natureza.Value("D")
        elif categoria == CONTRACHEQUE_JUN_18_BACKWARD and value in [10, 11, 12]:
            remuneracao.valor = remuneracao.valor * (-1)
            remuneracao.natureza = Coleta.Remuneracao.Natureza.Value("D")
        elif categoria == CONTRACHEQUE_OCT_NOV_18_JAN_TO_JUN19 and value in [16, 17, 18]:
            remuneracao.valor = remuneracao.valor * (-1)
            remuneracao.natureza = Coleta.Remuneracao.Natureza.Value("D")
        else: 
            remuneracao.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("O")

        if (
            categoria == CONTRACHEQUE_JUL_AUG_SEPT_DEC_18
            or categoria == CONTRACHEQUE_JUL19_FORWARD
            or categoria == CONTRACHEQUE_OCT_NOV_18_JAN_TO_JUN19
        ) and value in [9]:
            remuneracao.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("B")
        elif categoria == CONTRACHEQUE_JUN_18_BACKWARD and value in [3]:
            remuneracao.tipo_receita = Coleta.Remuneracao.TipoReceita.Value("B")

        remu_array.remuneracao.append(remuneracao)

    return remu_array


def update_employees(fn, employees, categoria):
    for row in fn:
        matricula = row[0] if categoria == INDENIZACOES_JUL_TO_DEZ_19 else row[1]
        if matricula in employees.keys():
            emp = employees[matricula]
            remu = cria_remuneracao(row, categoria)
            emp.remuneracoes.MergeFrom(remu)
            employees[matricula] = emp
    return employees


def parse(data, chave_coleta, month, year):
    employees = {}
    folha = Coleta.FolhaDePagamento()

    # Puts all parsed employees in the big map
    if year == "2018":
        if month in ["01", "02", "03", "04", "05", "06"]:
            employees.update(parse_employees(data.contracheque, chave_coleta, CONTRACHEQUE_JUN_18_BACKWARD))
            
        elif month in ["07", "08", "09", "12"]:
            employees.update(parse_employees(data.contracheque, chave_coleta, CONTRACHEQUE_JUL_AUG_SEPT_DEC_18))
        elif month in ["10", "11"]:
            employees.update(parse_employees(data.contracheque, chave_coleta, CONTRACHEQUE_OCT_NOV_18_JAN_TO_JUN19))

    elif year == "2019":
        if month in ["01", "02", "03", "04", "05", "06"]:
            employees.update(parse_employees(data.contracheque, chave_coleta, CONTRACHEQUE_OCT_NOV_18_JAN_TO_JUN19))
        else:
            employees.update(parse_employees(data.contracheque, chave_coleta, CONTRACHEQUE_JUL19_FORWARD))
    else:
        employees.update(parse_employees(data.contracheque, chave_coleta, CONTRACHEQUE_JUL19_FORWARD))

    try:
        if year != "2018":
            if year == "2019" and month in ["07", "08", "09", "10", "11", "12"]:
                update_employees(data.indenizatorias, employees, INDENIZACOES_JUL_TO_DEZ_19)
            elif (year != "2019"):
                update_employees(data.indenizatorias, employees, INDENIZACOES_JAN20_FORWARD)
    except KeyError as e:
        sys.stderr.write(
            "Registro inválido ao processar verbas indenizatórias: {}".format(e)
        )
        sys.exit(1)

    for i in employees.values():
        folha.contra_cheque.append(i)
    return folha
