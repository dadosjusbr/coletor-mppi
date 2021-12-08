import json
import unittest

from google.protobuf.json_format import MessageToDict

from data import load
from parser import parse


class TestParser(unittest.TestCase):
    def test_jan_2018(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open('src/output_test/expected/expected_01_2018.json', 'r') as fp:
            expected = json.load(fp)

        files = ['src/output_test/sheets/membros-ativos-contracheque-01-2018.ods']
                 
        dados = load(files, '2018', '01', 'src/output_test')
        result_data = parse(dados, 'mppi/01/2018', '01', '2018')
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected, result_to_dict)


    def test_jul_2018(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open('src/output_test/expected/expected_07_2018.json', 'r') as fp:
            expected = json.load(fp)

        files = ['src/output_test/sheets/membros-ativos-contracheque-07-2018.ods']
                 
        dados = load(files, '2018', '07', 'src/output_test')
        result_data = parse(dados, 'mppi/07/2018', '07', '2018')
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        
        self.assertEqual(expected, result_to_dict)


    def test_jan_2019(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open('src/output_test/expected/expected_01_2019.json', 'r') as fp:
            expected = json.load(fp)

        files = ['src/output_test/sheets/membros-ativos-contracheque-01-2019.ods']

        dados = load(files, '2019', '01', 'src/output_test')
        result_data = parse(dados, 'mppi/1/2019', '01', '2019')
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)

        self.assertEqual(expected, result_to_dict)


    def test_jul_2019(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open('src/output_test/expected/expected_07_2019.json', 'r') as fp:
            expected = json.load(fp)

        files = ['src/output_test/sheets/membros-ativos-contracheque-07-2019.ods',
                 'src/output_test/sheets/membros-ativos-verbas-indenizatorias-07-2019.ods']

        dados = load(files, '2019', '07', 'src/output_test')
        result_data = parse(dados, 'mppi/7/2019', '07', '2019')
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        
        self.assertEqual(expected, result_to_dict)
        

    def test_jan_2020(self):
        self.maxDiff = None
        # Json com a saida esperada
        with open('src/output_test/expected/expected_01_2020.json', 'r') as fp:
            expected = json.load(fp)

        files = ['src/output_test/sheets/membros-ativos-contracheque-01-2020.ods',
                 'src/output_test/sheets/membros-ativos-verbas-indenizatorias-01-2020.ods',]

        dados = load(files, '2020', '01', 'src/output_test')
        result_data = parse(dados, 'mppi/1/2020', '01', '2020')
        # Converto o resultado do parser, em dict
        result_to_dict = MessageToDict(result_data)
        
        self.assertEqual(expected, result_to_dict)


if __name__ == '__main__':
    unittest.main()