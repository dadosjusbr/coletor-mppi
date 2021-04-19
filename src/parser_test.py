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


if __name__ == "__main__":
    unittest.main()
