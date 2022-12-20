O objetivo desse arquivo em Python é simular um processo de inserção de uma plataforma. Ele vai inserir o arquivo LTV_GA.csv (que roda com o modelo de ML) uma quantidade de linhas a cada cinco minutos.

Funções:

splitfile.py:
-Divide o arquivo fonte em diversos outros arquivos .csv baseado em um número de linhas.

demo2.py:
-Operações básicas do GCP (para consulta).

putfile.py:
-Vasculha uma pasta (que possui os arquivos source .csv gerados pelo "splitfile.py") e insere um arquivo a cada 5 minutos no Google Cloud Storage, simulando uma fonte de inserção de dados.

No BigQuery:
-Dataset e Tabelas criados.
-Três JOBs de carregamento atuam no BigQuery, verficando de maneira conjunta a cada cinco minutos se existe alguma alteração ou arquivo novo em um bucket específico (no caso, o que recebe os arquivos do programa python) e se houver essa alteração ou inserção, os dados são aplicados na tabela.