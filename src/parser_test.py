import os
import parser
import unittest


class TestParser(unittest.TestCase):
    def test_membros_ativos_jan18(self):
        self.maxDiff = None

        expected = {
            "reg": "",
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


if __name__ == "__main__":
    unittest.main()
