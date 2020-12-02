# Indicadores Técnicos do Mercado Financeiro
# (Python >= 3.6)

Seja bem vindo ao nosso repositório.
O objetivo deste repositório é entregar duas ferramentas técnicas: a Média Móvel Exponencial (MME) e o Índice de Força Relativa (IRF) que serão gerados a partir de uma base de dados de um arquivo csv.

Resumo:<br />
1 - <a href="#ind_choose">Escolha dos indicadores</a><br />
2 - <a href="#data">A base de dados</a><br />
3 - <a href="#how_to_install">Como instalar o programa</a>
<br />
4 - <a href="#how_to_use">Como usar o programa</a><br />
5 - <a href="#comments">Comentários finais</a><br />



# <span id="ind_choose">1</span> - Escolha dos indicadores
- Os indicadores escolhidos foram a Média Móvel Exponencial e o Índice de Força Relativa
- A escolha dos indicadores foi feita tendo em mente a popularidade do indicador e a sua facilidade de uso, além de outras vantagens que serão apresentadas à seguir
- As médias móveis ajudam a visualizar as variações do preço de uma forma mais "suavizada". Elas são muito usadas para ter uma referência da tendência de mercado. Uma média móvel muito usada é a de 200 períodos
- A média móvel tem uma defasagem "natural" com relação aos movimentos do preço do mercado, uma vez que ela é calculada tendo por base preços passados. Tendo em vista esta defasagem a Média Móvel Exponencial veio para "tentar reduzir" essa defasagem
- Você pode aprender mais sobre a MME clicando neste link: https://www.bussoladoinvestidor.com.br/media-movel-exponencial/
- Com relação ao IFR ele ajuda a observar o enfraquecimento de uma tendência ou até mesmo o rompimento com a consecutiva criação de uma nova tendência
- Assim como a MME, o IFR é um indicador muito difundido e muito simples de usar. Para saber mais sobre o IFR clique neste link: https://www.bussoladoinvestidor.com.br/indice-de-forca-relativa/


# <span id="data">2</span> - A base de dados
- Para usar este aplicativo devemos baixar a base de dados que está contida no seguinte link: https://www.kaggle.com/mczielinski/bitcoin-historical-data/data
- O nome da base de dados usada no aplicativo é `bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv`, porém este repositório já vem com um pequeno recorte desse arquivo com o mesmo nome para que se possa fazer o primeiro teste do programa (intervalo de 01-01-2013 à 31-12-2013)
- É possivel mudar o nome do arquivo de dados no próprio programa (veja mais em <a href="#how_to_use">Como usar o programa</a><br />)

# <span id="how_to_install">3</span> - Como instalar o programa
- Todos os comando abaixo deverão ser executados no Terminal do Linux
- A versão do Python usada deverá ser >= 3.6
- É necessário ter o pacote venv instalado para criar um ambiente virtual
- É necessário ter o pacote pip instalado para instalar as dependências
# Comandos
- Para baixar o repositório digite `git clone https://github.com/mrc6/indicadores-tecnicos-mercado-financeiro.git`
- Entre na pasta do programa com o comando: `cd indicadores-tecnicos-mercado-financeiro`
- Crie um ambiente virtual para rodar o programa com o seguinte comando: `python3 -m venv .venv && source .venv/bin/activate`
- Instale as dependências com o comando: `python3 -m pip install -r requirements.txt`
- Entre na pasta principal do projeto com o comando: `cd project`
- Execute o programa com o comando: `python3 cli.py`
- Ao terminar de usar o programa, saia do ambiente virtual com o seguinte comando: `deactivate`

# <span id="how_to_use">4</span> Como usar o programa
- Como você pode ver a interação com o programa é feita pelo próprio terminal
- Antes de começar cole a base de dados que você fez o download no diretório `data`
- Como já tem um arquivo neste diretório com o mesmo nome você deve sobrescrevê-lo para que você tenha a base de dados atualizada
- A interação é dada por Menus

# Menu principal
- Neste menu existem as seguintes opções: 1 - Criar Relatorio MME + IFR, 2 - Mostrar Configurações dos Indicadores, 3 - Alterar Configurações dos Indicadores, 4 - Mudar Nome da Base de Dados, 9 - Sair
- Para acessar cada menu digite o número do menu e tecle `ENTER`

# Menu Criar Relatorio MME + IFR
- Neste menu você criará um arquivo `rel.csv`  no diretório `data` com os indicadores MME e IFR calculados sobre a base de dados com as configurações atuais
- Parâmetros de entrada: data inicial e data final dos dados a serem atualizados

# Menu Mostrar Configurações dos Indicadores
- Este menu mostra as configurações dos indicadores e o valor do preço usado para calcular o relatório do menu anterior
- O mesmo tipo de preço é aplicado nos dois indicadores técnicos

# Menu Alterar Configurações dos Indicadores
- Neste menu você pode alterar as configurações dos indicadores técnicos antes de criar o relatório do primeiro menu
- As configurações (ou parâmetros) que podem ser alterados são: Período da MME, Período da IRF e o Tipo de Preço a ser usado nos cálculos

# Menu Mudar Nome da Base de Dados
- Caso o nome do arquivo da base de dados mude, você deve configurar o nome do novo arquivo neste menu
- A base de dados deve ser um arquivo `.csv` que siga a mesma estrutura do arquivo de exemplo que já vem ao baixar esse repositório
- A base de dados deve ser salva no diretório `data`

# Menu Sair
- Termina a execução do programa

# <span id="comments">5</span> Comentários
- Ao longo deste projeto pude perceber como a linguagem Python é simples e poderosa para manipular dados e criar informações a partir desdes dados
- Existem bibliotecas específicas para essa manipulação como a `pandas` (https://pandas.pydata.org/) e frameworks como o `Jupyter` (https://jupyter.org/) onde é possível criar uma visualização dos dados e gráficos, mas o objetivo deste repositório é mostrar que é possível fazer a manipulção dos dados usando Python puro
- Foi um grande aprendizado fazer este programa o que só despertou ainda mais o meu interesse pela análise de dados e o Python
