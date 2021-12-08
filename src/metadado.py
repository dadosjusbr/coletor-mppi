from coleta import coleta_pb2 as Coleta


def captura(month, year):
    metadado = Coleta.Metadados()
    metadado.nao_requer_login = True
    metadado.nao_requer_captcha = True
    # URLS nada semâticas com códigos diferentes para cada mês
    metadado.acesso = Coleta.Metadados.FormaDeAcesso.RASPAGEM_DIFICULTADA
    metadado.extensao = Coleta.Metadados.Extensao.ODS
    metadado.estritamente_tabular = False

    metadado.tem_matricula = True
    if year == "2018" and month in ["01", "02", "03", "04", "05", "06"]:
        metadado.tem_matricula = False

    metadado.tem_lotacao = False
    metadado.tem_cargo = True
    metadado.receita_base = Coleta.Metadados.OpcoesDetalhamento.DETALHADO
    metadado.despesas = Coleta.Metadados.OpcoesDetalhamento.DETALHADO
    metadado.formato_consistente = True
    metadado.outras_receitas = Coleta.Metadados.OpcoesDetalhamento.DETALHADO
    # Nessas datas, ocorrem mudanças nos contracheques e também 
    # são adicionadas as planilhas de verbas indenizatórias.
    if (year == "2018" and month in ["07", "10", "12"]) \
        or (year == "2019" and month in ["01", "07"]) \
        or (year == "2020" and month in ["01"]):
        metadado.formato_consistente = False

    # Para esses anos, é apenas colocado o total, e não detalhado as verbas indenizatórias
    if year == "2018" or (year == "2019" and month in ["01", "02", "03", "04", "05", "06"]):
        metadado.outras_receitas = Coleta.Metadados.OpcoesDetalhamento.SUMARIZADO
        
    return metadado