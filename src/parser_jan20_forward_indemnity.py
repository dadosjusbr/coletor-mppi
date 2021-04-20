import parser


def update_employee_indemnity(file_name, employees):
    rows = parser.read_data(file_name).to_numpy()
    begin_row = parser.get_begin_row(rows)
    end_row = parser.get_end_row(rows, begin_row)
    curr_row = 0
    for row in rows:
        if curr_row < begin_row:
            curr_row += 1
            continue

        matricula = str(row[1])
        if matricula in employees.keys():
            alimentacao = parser.format_value(row[6])
            saude = parser.format_value(row[7])
            abono_pecuniario = parser.format_value(row[8])
            indenizacao_por_cumulacao = parser.format_value(row[9])
            complemento_por_entrancia = parser.format_value(row[10])
            total_indenizacoes = alimentacao + saude + abono_pecuniario
            total_gratificacoes = indenizacao_por_cumulacao + complemento_por_entrancia
            emp = employees[matricula]

            emp["income"].update(
                {
                    "total": round(
                        emp["income"]["total"]
                        + total_indenizacoes
                        + total_gratificacoes,
                        2,
                    ),
                }
            )
            emp["income"].update(
                {
                    "perks": {
                        "total": round(total_indenizacoes, 2),
                        "food": alimentacao,
                        "health": saude,
                        "vacation_pecuniary": abono_pecuniario,
                    }
                }
            )
            emp["income"]["other"]["others"].update(
                {
                    "INDENIZAÇÃO POR CUMULAÇÃO": indenizacao_por_cumulacao,
                    "COMPLEMENTO POR ENTRÂNCIA": complemento_por_entrancia,
                }
            )

            emp["income"]["other"].update(
                {
                    "others_total": round(
                        emp["income"]["other"]["others_total"] + total_gratificacoes, 2
                    ),
                    "total": round(
                        emp["income"]["other"]["total"] + total_gratificacoes, 2
                    ),
                }
            )
            employees[matricula] = emp

            curr_row += 1
            if curr_row > end_row:
                break
    return employees
