# Ministério Público do Piauí - Crawler

Este crawler tem como objetivo a recuperação de informações sobre folhas de pagamentos dos membros ativos do Ministério Público do Piauí, a partir de 2018. O site com as informações pode ser acessado [aqui](https://www.mppi.mp.br/internet/portal-da-transparencia/contracheque/).

O crawler está estruturado como uma CLI. É necessário passar os argumentos mês, ano e caminho para armazenar os arquivos via variáveis de ambiente (`MONTH`, `YEAR`, `OUTPUT_FOLDER`). E então, serão baixadas as planilhas, no formato ods. As mesmas são correpondentes a remuneração mensal e verbas indenizatórias dos Membros Ativos.


# Dicionário de dados

As planilhas referentes á remunerações possuem as seguintes colunas:

- **Matrícula (Number)**: Matrícula do funcionário
- **Nome (String)**: Nome completo do funcionário
- **Cargo (String)**: Cargo do funcionário dentro do MP
- **Lotação (String)**: Local (cidade, departamento, promotoria) em que o funcionário trabalha
- **Remuneração do cargo efetivo (Number)**: Vencimento, GAMPU, V.P.I, Adicionais de Qualificação, G.A.E e G.A.S, além de outras desta natureza. Soma de todas essas remunerações
- **Outras Verbas Remuneratórias, Legais ou  Judiciais (Number)**: V.P.N.I., Adicional por tempo de serviço, quintos, décimos e vantagens decorrentes de sentença judicial ou extensão administrativa
- **Função de confiança ou cargo em comissão (Number)**: Rubricas que representam a retribuição paga pelo exercício de função (servidor efetivo) ou remuneração de cargo em comissão (servidor sem vínculo ou requisitado)
- **Gratificação natalina (Number)**: Parcelas da Gratificação Natalina (13º) pagas no mês corrente, ou no caso de vacância ou exoneração do servidor
- **Férias - ⅓ Constitucional (Number)**: Adicional correspondente a 1/3 (um terço) da remuneração, pago ao servidor por ocasião das férias
- **Abono de permanência (Number)**: Valor equivalente ao da contribuição previdenciária, devido ao funcionário público que esteja em condição de aposentar-se, mas que optou por continuar em atividade (instituído pela Emenda Constitucional nº 41, de 16 de dezembro de 2003)
- **Total de Rendimentos Brutos (Number)**: Total dos rendimentos brutos pagos no mês.
- **Contribuição Previdenciária (Number)**: Contribuição Previdenciária.
- **Imposto de Renda (Number)**: Imposto de Renda Retido na Fonte.
- **Retenção por Teto Constitucional (Number)**: Valor deduzido da remuneração bruta, quando esta ultrapassa o teto constitucional, de acordo com a Resolução nº 09/2006 do CNMP.
- **Total de Descontos (Number)**: Soma dos descontos referidos nos itens 8, 9 e 10.
- **Total Líquido (Number)**: Rendimento obtido após o abatimento dos descontos referidos no item 11. O valor líquido efetivamente recebido pelo membro ou servidor pode ser inferior ao ora divulgado, porque não são considerados os descontos de caráter pessoal.
- **Indenizações (Number)**: Verbas referentes á indenizações recebidas pelo funcionario á titulo de Adicional noturno, Cumulações, Serviços extraordinários e substituição de função.
- **Outras Remunerações Temporárias (Number)**: Valores pagos a título de Auxílio-alimentação, Auxílio-cursos,Auxílio-Saúde, Auxílio-creche, Auxílio-moradia.


As planilhas referentes á verbas indenizatórias e remunerações temporárias possuem as seguintes colunas:
					
- **Abono Pecuniário (Number)**: Troca de alguns dias do período de férias pelo recebimento de um valor extra.
- **Auxílio alimentação (Number)**
- **Auxílio saúde (Number)**
-**Indenização por cumulação (Number)**
-**Complemento por entrância (Number)**


# Dificuldades na automação da coleta dos dados

    - Falta de padrão nas URLs:
        Como é formada a URL atualmente:
            - Base (parte fixa): https://www.mppi.mp.br/internet/wp-content/uploads//";
            - Ano: possívelmente o ano em que foi disponibilizada a planilha, visto que para as tabelas de dezembro e algumas de novembro esse atributo é igual ao ano posterior;
            - Código: campo composto por dois digitos, que altera de acordo com mês e ano;
            - Complemento: campo que identifica que a planilha é referente aos membros ativos, variando em vários meses a maneira como é escrito;
            - Mês: referencia o mês da planilha, alterando a forma como é escrito(Digíto ou por extenso);
            - Ano: referencia o ano da planilha, alterando a forma que é escrito (4 ou 2 dígitos).
        
        Ex: 
        Link para download da planilha de remuneração mensal de julho de 2020 - https://www.mppi.mp.br/internet/wp-content/uploads/2020/09/Remuneracao-de-todos-os-membros-ativos-%E2%80%93-julho-2020.ods

        Link para download da planilha de remuneração mensal de agosto de 2020: https://www.mppi.mp.br/internet/wp-content/uploads/2020/10/Remuneracao-de-todos-os-membros-ativos-%E2%80%93-agosto-%E2%80%93-2020.ods
    
    - Variação na formatação das planilhas:
        - Algumas planilhas disponibilizam os dados a partir da primeira coluna, em outras os dados commeçam na segunda coluna;
        - No ano de 2018 temos dois tipos de planilhas para as remunerações mensais (São distintas em relação a ordem dos variáveis e o campo matrícula se encontra apenas nas planilhas posteriores a junho de 2018);
        - Em 2019 temos dois tipos de planilha para remunerações mensais (a variação é apenas na ordem das variáveis). A planilha de verbas indenizatórias se mantem constante para todos os meses que foram disponibilizada;
        - Em 2020 a planilha de remunerações mensais não teve variação em relação as planilhas do segundo semestre de 2019. Apresentando uma nova ordem nas variáveis das planilhas de verbas indenizatórias, a qual se manteu constante durate todo o ano. 
            
# Como realizar a coleta automatica para meses que foram acrescidos no MPPI

    - Primeiramente é necessário identicar o código presente no link referente ao mês que desejo acrescentar (Formação do link explicada no campo anterior). Ao indentificar, preencher na classe src/utils.py o campo destinado ao mesmo. Ex.: A função cod2021(month) retorna um dicionario, no qual a chave é o mẽs e o valor é esse cógido

    - Na classe src/crawler.py é necessário verificar se a formação do link encontra-se em alguma condição já implementada ou se é necessário implementar mais uma condição (Lembre-se que é necessário verificar o link para remunerações mensais e para remuneraões de verbas indenizatória/temporárias).

## Como usar

  ### Executando sem Docker

 - É necessário ter instalado o [Python](https://www.python.org/downloads/release/python-385/) versão 3.8.5;
 
No Linux, distribuições Ubuntu/Mint:

```
sudo apt install python3 python3-pip
```

 - Utilize o PiP (foi utilizada a versão 20.3.3) para instalar as dependências que estão listadas no arquivo requirements.txt.
  
    ```sh
      $ cd coletores/mppi
      $ pip3 install -r requirements.txt
    ```

  - Após concluida a instalação das dependências utilize os seguintes comandos:  

   ```sh
      $ cd src
      $ MONTH=1 YEAR=2020 GIT_COMMIT=$(git rev-list -1 HEAD) python3 main.py
  ```