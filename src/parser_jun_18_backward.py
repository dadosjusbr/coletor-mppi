import parser


def parse_employees_jun18_backward(file_name):
    rows = parser.read_data(file_name).to_numpy()
    begin_row = parser.get_begin_row(rows)
    end_row = parser.get_end_row(rows, begin_row)
    employees = {}
    curr_row = 0
    for row in rows:
        if curr_row < begin_row:
            curr_row += 1
            continue

        nome = row[0]
        cargo_efetivo = row[1]
        lotacao = row[2]
        if parser.isNaN(lotacao):
            lotacao = "Não informado"
        remuneracao_cargo_efetivo = parser.format_value(
            row[3]
        )  # Remuneração do Cargo Efetivo/Proventos/Bolsa Estágio
        outras_verbas_remuneratorias = parser.format_value(row[4])
        confianca_comissao = parser.format_value(
            row[5]
        )  # Função de Confiança ou Cargo em Comissão
        grat_natalina = parser.format_value(row[6])  # Gratificação Natalina
        ferias = parser.format_value(row[7])
        permanencia = parser.format_value(row[8])  # Abono de Permanência
        previdencia = parser.format_value(row[10])  # Contribuição Previdenciária
        imp_renda = parser.format_value(row[11])  # Imposto de Renda
        teto_constitucional = parser.format_value(
            row[12]
        )  # Retenção por Teto Constitucional
        indenizacoes = parser.format_value(row[15])
        outras_remuneracoes_temporarias = parser.format_value(
            row[16]
        )  # Outras Remunerações Retroativas/Temporárias
        total_desconto = previdencia + imp_renda + teto_constitucional
        total_gratificacoes = (
            grat_natalina
            + ferias
            + permanencia
            + confianca_comissao
            + outras_remuneracoes_temporarias
        )
        total_bruto = (
            remuneracao_cargo_efetivo
            + outras_verbas_remuneratorias
            + total_gratificacoes
            + indenizacoes
            
        )

        employees[nome] = {
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
                "perks": {
                    "total": indenizacoes,
                },
                "other": {  # Gratificações
                    "total": round(total_gratificacoes, 2),
                    "trust_position": confianca_comissao,
                    "others_total": round(grat_natalina + ferias + permanencia + outras_remuneracoes_temporarias, 2),
                    "others": {
                        "Gratificação Natalina": grat_natalina,
                        "Férias (1/3 constitucional)": ferias,
                        "Abono de Permanência": permanencia,
                        "Outras Remunerações Retroativas/Temporárias": outras_remuneracoes_temporarias,
                    },
                },
            },
            "discounts": {  # Discounts Object. Using abs to garantee numbers are positivo (spreadsheet have negative discounts).
                "total": round(total_desconto, 2),
                "prev_contribution": previdencia,
                # Retenção por teto constitucional
                "ceil_retention": teto_constitucional,
                "income_tax": imp_renda,
            },
        }

        curr_row += 1
        if curr_row > end_row:
            break
    return employees
