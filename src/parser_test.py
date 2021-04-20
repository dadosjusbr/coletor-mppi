import os
import parser
import unittest


class TestParser(unittest.TestCase):
    def test_membros_ativos_jan18(self):
        self.maxDiff = None

        expected = {
            "name": "ADRIANO FONTENELE SANTOS",
            "role": "PROMOTOR(A) DE JUSTICA",
            "type": "membro",
            "workplace": "1ª PROMOTORIA DE JUSTICA DE PIO IX",
            "active": True,
            "income": {
                "total": 43460.43,
                "wage": 27500.17,
                "perks": {"total": 5817.73},
                "other": {
                    "total": 10142.53,
                    "trust_position": 0.0,
                    "others_total": 10142.53,
                    "others": {
                        "Gratificação Natalina": 0.0,
                        "Férias (1/3 constitucional)": 9166.72,
                        "Abono de Permanência": 0.0,
                        "Outras Remunerações Retroativas/Temporárias": 975.81,
                    },
                },
            },
            "discounts": {
                "total": 12221.51,
                "prev_contribution": 3850.02,
                "ceil_retention": 0.0,
                "income_tax": 8371.49,
            },
        }

        files = ("./output_test/Membros ativos-01-2018.ods",)
        employees = parser.parse(files, "2018", "01")

        # Verificações
        self.assertEqual(1, len(employees))
        self.assertDictEqual(employees[0], expected)

    def test_membros_ativos_jul18(self):
        self.maxDiff = None

        expected = {
            "reg": "16213",
            "name": "CLAUDIA PESSOA MARQUES DA ROCHA SEABRA",
            "role": "12º PROMOTOR(A) DE JUSTICA DE TERESINA, CHEFE DE GABINETE",
            "type": "membro",
            "workplace": "12ª PROMOTORIA DE JUSTICA DE TERESINA, 12ª PROMOTORIA DE JUSTICA DE TERESINA, GABINETE DO PROCURADOR-GERAL, PROCURADORIA-GERAL DE JUSTICA",
            "active": True,
            "income": {
                "total": 40770.79,
                "wage": 28947.55,
                "perks": {"total": 6033.73},
                "other": {
                    "total": 5789.51,
                    "trust_position": 5789.51,
                    "others_total": 0.0,
                    "others": {
                        "Gratificação Natalina": 0.0,
                        "Férias (1/3 constitucional)": 0.0,
                        "Abono de Permanência": 0.0,
                    },
                },
            },
            "discounts": {
                "total": 12223.43,
                "prev_contribution": 4052.66,
                "ceil_retention": 974.06,
                "income_tax": 7196.71,
            },
        }

        files = ("./output_test/Membros ativos-07-2018.ods",)
        employees = parser.parse(files, "2018", "07")

        # Verificações
        self.assertEqual(1, len(employees))
        self.assertDictEqual(employees[0], expected)

    def test_membros_ativos_jan19(self):
        self.maxDiff = None

        expected = {
            "reg": "15939",
            "name": "ALIPIO DE SANTANA RIBEIRO",
            "role": "2º PROCURADOR(A) DE JUSTIÇA CRIMINAL",
            "type": "membro",
            "workplace": "2ª PROCURADORIA DE JUSTIÇA CRIMINAL, 2ª PROCURADORIA DE JUSTIÇA CRIMINAL",
            "active": True,
            "income": {
                "total": 48147.09,
                "wage": 40990.03,
                "perks": {"total": 1656.0},
                "other": {
                    "total": 5501.06,
                    "trust_position": 0.0,
                    "others_total": 5501.06,
                    "others": {
                        "Gratificação Natalina": 0.0,
                        "Férias (1/3 constitucional)": 0.0,
                        "Abono de Permanência": 5501.06,
                        "Outra Remunerações Temporárias": 0.0,
                    },
                },
            },
            "discounts": {
                "total": 17134.07,
                "prev_contribution": 5501.06,
                "ceil_retention": 1696.71,
                "income_tax": 9936.3,
            },
        }

        files = ("./output_test/Membros ativos-01-2019.ods",)
        employees = parser.parse(files, "2019", "01")

        # Verificações
        self.assertEqual(1, len(employees))
        self.assertDictEqual(employees[0], expected)

    def test_membros_ativos_jul19(self):
        self.maxDiff = None

        expected = {
            "reg": "10014",
            "name": "ADRIANO FONTENELE SANTOS",
            "role": "2º PROMOTOR(A) DE JUSTICA DE ESPERANTINA",
            "type": "membro",
            "workplace": "2ª PROMOTORIA DE JUSTICA DE ESPERANTINA, 2ª PROMOTORIA DE JUSTICA DE ESPERANTINA",
            "active": True,
            "income": {
                "total": 46755.83,
                "wage": 32004.65,
                "other": {
                    "total": 2026.96,
                    "trust_position": 0.0,
                    "others_total": 2026.96,
                    "others": {
                        "Gratificação Natalina": 0.0,
                        "Férias (1/3 constitucional)": 0.0,
                        "Abono de Permanência": 0.0,
                        "INDENIZAÇÃO POR CUMULAÇÃO": 2026.96,
                        "COMPLEMENTO POR ENTRÂNCIA": 0.0,
                    },
                },
                "perks": {
                    "total": 12724.22,
                    "food": 1656.0,
                    "health": 400.0,
                    "vacation_pecuniary": 10668.22,
                },
            },
            "discounts": {
                "total": 11128.25,
                "prev_contribution": 4480.65,
                "ceil_retention": 0.0,
                "income_tax": 6647.6,
            },
        }
        files = (
            "./output_test/Membros ativos-07-2019.ods",
            "./output_test/Membros ativos-Verbas Indenizatorias-07-2019.ods",
        )
        employees = parser.parse(files, "2019", "07")

        # Verificações
        self.assertEqual(1, len(employees))
        self.assertDictEqual(employees[0], expected)


if __name__ == "__main__":
    unittest.main()
