import parser


def parse_employees(file_name):
    rows = parser.read_data(file_name).to_numpy()
    begin_row = parser.get_begin_row(rows)
    end_row = parser.get_end_row(rows, begin_row)
    employees = {}
    curr_row = 0
    for row in rows:
        if curr_row < begin_row:
            curr_row += 1
            continue

        matricula = str(row[1])
        # As planilhas possuem algumas caracteristicas que dificultaram o parser, como por exemplo:
        # linhas vazias entre as as informações dos membros;
        # presença de cabeçalho em cada página;
        # presença de rodapé em cada página.
        # Para contorna essas dificuldade no parseameno dos dados, foram criadas algumas condiçõe para que o parser ocorra apenas nas linhas que contem informações dos membro.
        if not parser.isNaN(matricula) and matricula != "nan":
            if "Membros" not in str(matricula) and "Matrícula" not in matricula:
                nome = row[3]
                cargo_efetivo = row[5]
                lotacao = row[7]
                if parser.isNaN(lotacao):
                    lotacao = "Não informado"
                remuneracao_cargo_efetivo = parser.format_value(row[9])
                outras_verbas_remuneratorias = parser.format_value(row[10])
                confianca_comissao = parser.format_value(
                    row[11]
                )  # Função de Confiança ou Cargo em Comissão
                grat_natalina = parser.format_value(row[12])  # Gratificação Natalina
                ferias = parser.format_value(row[13])
                permanencia = parser.format_value(row[14])  # Abono de Permanência
                previdencia = parser.format_value(
                    row[18]
                )  # Contribuição Previdenciária
                imp_renda = parser.format_value(row[19])  # Imposto de Renda
                teto_constitucional = parser.format_value(
                    row[20]
                )  # Retenção por Teto Constitucional
                total_desconto = previdencia + imp_renda + teto_constitucional
                total_gratificacoes = (
                    grat_natalina + ferias + permanencia + confianca_comissao
                )
                total_bruto = (
                    remuneracao_cargo_efetivo
                    + outras_verbas_remuneratorias
                    + total_gratificacoes
                )

                employees[matricula] = {
                    "reg": matricula,
                    "name": nome,
                    "role": cargo_efetivo,
                    "type": "membro",
                    "workplace": lotacao,
                    "active": True,
                    "income": {
                        "total": round(total_bruto, 2),
                        # REMUNERAÇÃO BÁSICA = Remuneração Cargo Efetivo + Outras Verbas Remuneratórias, Legais ou Judiciais
                        "wage": round(
                            remuneracao_cargo_efetivo + outras_verbas_remuneratorias, 2
                        ),
                        "other": {  # Gratificações
                            "total": round(total_gratificacoes, 2),
                            "trust_position": confianca_comissao,
                            "others_total": round(
                                grat_natalina + ferias + permanencia, 2
                            ),
                            "others": {
                                "Gratificação Natalina": grat_natalina,
                                "Férias (1/3 constitucional)": ferias,
                                "Abono de Permanência": permanencia,
                            },
                        },
                    },
                    "discounts": {  # Discounts Object. Using abs to garantee numbers are positivo (spreadsheet have negative discounts).
                        "total": round(abs(total_desconto), 2),
                        "prev_contribution": abs(previdencia),
                        # Retenção por teto constitucional
                        "ceil_retention": abs(teto_constitucional),
                        "income_tax": abs(imp_renda),
                    },
                }

        curr_row += 1
        if curr_row > end_row:
            break

    return employees
