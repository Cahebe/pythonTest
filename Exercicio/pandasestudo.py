import pandas as pd
import numpy as np
import faker

print('-------------------------------------------------')
print('------PD.SERIES------')  # criação de séries
serie_dados = pd.Series([10, 20, 30, 40, 50])
print(serie_dados)
serie_dados_float = pd.Series([10.02, 20.32, 30.71, 40.43, 50.11])
print(serie_dados_float)
print('-------------------------------------------------')
array_inteiros = np.array([10, 20, 30, 40, 50])
indices = np.array(['A', 'B', 'C', 'D', 'E'])
serie_dados = pd.Series(array_inteiros, indices)
print(serie_dados)
print('-------------------------------------------------')
print('------INDEX------')  # método para mudar os valores do indice
serie_dados.index = np.array(['Z', 'X', 'V', 'Y', 'W'])
print(serie_dados)
print('-------------------------------------------------')
print('------DICT------')  # usando dicionario para criar uma série no Pandas
dicionario = {'João': 10, 'Alice': 5, 'Gustavo': 6, 'Pedro': 9}
dict_serie_dados = pd.Series(dicionario)
print(dict_serie_dados)
print('-------------------------------------------------')
print('------FATIAMENTO/SLICING------')
print(serie_dados[0:2])
print('------SUBVARIAVEL------')
serie_dados_apenas_3_items = serie_dados[0:3]
print(serie_dados_apenas_3_items)
print('-------------------------------------------------')
print('------COPY------')
serie_dados_copy = serie_dados.copy()
print(serie_dados_copy)
print('-------------------------------------------------')
print('------CONVERSÃO------')
serie_dados_convert = serie_dados_float.astype(int)
print(serie_dados_convert)
print('-------------------------------------------------')
print('------CONCATENAÇÃO------')
dados_novos = {'Gustavo': 20, 'Alana': 30}
serie_dados_novos = pd.Series(dados_novos)
serie_dados_concatenation = pd.concat([dict_serie_dados, serie_dados_novos])
print(serie_dados_concatenation)
print('-------------------------------------------------')
print('------ILOC------')  # acessa elementos por indice
dataset = pd.read_csv('census.csv')
serie_age = dataset['age']
print(serie_age)
print('-------------------------------------------------')
print('------HEAD------')  # 5 primeiros registros (por padrão)
print(serie_age.head())
print('-------------------------------------------------')
print(serie_age.head(10))  # é possivel informar quantos valores serão retornados
print('-------------------------------------------------')
print('------TAIL------')  # 5 ultimos registros (por padrão)
print(serie_age.tail())
print('-------------------------------------------------')
print('------ILOC------')  # seleciona linhas/colunas a partir do indice
print(serie_age.iloc[0])
print('-------------------------------------------------')
print('------ILOC - INTERVALOS------')
print(serie_age.iloc[0:3])
print('-------------------------------------------------')
print('------ILOC - INDICES------')
print(serie_age.iloc[[0, 2, 4]])
print('-------------------------------------------------')
print('------pessoas com mais de 50 anos------')
lista_idade_50_mais = []
for i in serie_age.items():
    if i[1] > 50:  # i na posição 1 é a idade da pessoa - na posição 0 é o indice
        lista_idade_50_mais.append(i[0])  # adicionando os indices na lista
print(serie_age.iloc[lista_idade_50_mais])
print('-------------------------------------------------')
print('------LOC------')  # acessa elementos por string
fake = faker.Faker()  # utilizando a biblioteca 'Faker' para criar dados fake
indices_nome = []
for _ in range(32561):  # qtd igual a 'serie_age' para ser compativel
    indices_nome.append(fake.name())

print(serie_age.size)  # testando qual o tamanho da 'serie_age'
serie_age_name = pd.Series(np.array(dataset['age']), index=indices_nome)
print(serie_age_name)
print('------DESCOMENTA A PROXIMA LINHA------')
# print(serie_age_name.loc["Donald Young"])  # pesquisando por indice
serie_age_name2 = serie_age_name.drop_duplicates()
print(serie_age_name2.size)
serie_age_name3 = serie_age_name2.copy()
print('-------------------------------------------------')
print('------RESET_INDEX------')  # reseta o indice
print(serie_age_name3.reset_index(drop=True, inplace=True))
# inplace = modifica o objeto original
print('-------------------------------------------------')
print('------SORT_VALUES()------')  # ordena a serie por valores
print(serie_age_name.sort_values())  # ascending=False = descrescente
print('-------------------------------------------------')
print(serie_age_name.sort_values().iloc[0:11])  # 10 primeiros registros
print('-------------------------------------------------')
print('------SORT_INDEX()------')
print(serie_age_name.sort_index())  # ordena a serie por indice
print('-------------------------------------------------')
print('------VALUE_COUNTS()------')  # faz a contagem dos valores
# exemplo: existem 52 pessoas com idade 30
print(serie_age_name.value_counts())  # normalize=True = porcentagem
# bins='n° inteiro' = agrupa em intervalos
print('-------------------------------------------------')
print('------APICANDO FILTROS------')
indices_pais = []
for _ in range(32561):
    indices_pais.append(fake.country())  # criação do indice com nomes de paises

serie_pais = pd.Series(np.array(dataset['age']), index=indices_pais)
# criação da serie
print('------FILTRO 1------')
print(serie_pais.loc[serie_pais > 50])  # aplicando filtro
print('------FILTRO 2------')
print(serie_pais.loc[(serie_pais > 50) & (serie_pais.index == "India")])
print('------ISIN/ ~ISIN------')  # isin = retorna True quando a condição for
# verdadeira -- ~isin = retorna True caso a condição NÃO for verdadeira
print(serie_pais.index.isin(["India", "Brazil"]))
print('-------------------------------------------------')
print(~serie_pais.index.isin(["India", "Brazil"]))
print('-------------------------------------------------')
print('------OPERAÇÕES MATEMATICAS------')
print(serie_pais + 2)  # Python puro
print(serie_pais.add(2))  # Pandas
# sub(2) = subtração
# mul(2) = multiplicação
# div(2) = divisão
print('-------------------------------------------------')
print('------OPERAÇÕES COM STRINGS------')
serie_pais_index = serie_pais.index.to_series()  # serie criada
serie_pais_index.reset_index(drop=True, inplace=True)  # resetando os indices
# para utilizar n°s ao invés do indice original
print('------STR.CONTAINS()------')  # verifica se contem a condição em algum
# elemento da serie
serie_pais_index.str.contains("bra")
print('------STR.UPPER()/LOWER------')  # MAISCULA/MINUSCULA
serie_pais_index.str.upper()
print('------STRIP------')  # corta da string a condição especificada
serie_pais_index.str.strip("bra")
print('------STR.SPLIT------')  # separa a string e cria uma nova coluna
serie_pais_index.str.split(" ")  # após o espaço em branco criará
# uma nova coluna - exemplo: 'Guiana Francesa' = 'Guiana' 'Francesa'
print('------ACESSAR POSIÇÃO ESPECIFICA DA STRING------')
print(serie_pais_index.str[0:5])  # seleciona do caracter 0 ao 4
print('-------------------------------------------------')
print('------AGRUPAMENTO NUMÉRICO------')
print('------SUM()------')
print(serie_pais.sum())
print('------MEAN()------')
print(serie_pais.loc["Brazil"].mean())
print('------MEDIAN()------')
print(serie_pais.median())
print('------COUNT()------')
print(serie_pais.count())
print('------STD()------')
print(serie_pais.std())  # desvio padrão
print('------VAR()------')  # variancia
print(serie_pais.var())
print('------QAUNTILE()------')  # quantil
print(serie_pais.quantile([0.25, 0.50, 0.75]))
print('-------------------------------------------------')
print('------AGRUPAMENTO CATEGÓRICO------')
print('------VALUE_COUNTS------')
print(serie_pais_index.value_counts())
print('------UNIQUE------')
print(serie_pais_index.unique())  # retorna os nomes unicos que estão na BD
print('------NUNIQUE------')
print(serie_pais_index.nunique())  # retorna a qtd de valores unicos
print('-------------------------------------------------')
print('------VALORES FALTANTES------')
serie_faltante = pd.Series([1, 2, 3, np.nan, 5, np.nan])
print('------ISNA------')  # retorna se existe ou não valores faltantes
print(serie_faltante.isna())
print(serie_faltante.isna().sum)  # retorna a qtd de valores faltantes
print(serie_faltante.value_counts(dropna=False))  # dropna = retira os
# valores faltantes
print('------FILLNA------')  # preenche os valores faltantes
print(serie_faltante.fillna(serie_faltante.mean()))
print('-------------------------------------------------')
serie_faltante_str = pd.Series(["Maçã", "Banana", "Arroz", "Arroz", np.nan, "Batata"])
print(serie_faltante_str.fillna(serie_faltante.mode().iloc[0]))
# mode retorna os valores mais frequente..é retornada uma nova serie..por isso
# utiliza-se a função iloc[0] para pegar o 1°(ou qlqer outro) valor
print('-------------------------------------------------')
print('------FUNÇÕES------')
print('------APPLY------')
print(serie_age.loc[serie_age < 18])


def corrige_idade(idade):
    if idade < 18:
        idade = 18
    else:
        return idade


serie_age = serie_age.apply(corrige_idade)  # utilizando a função criada
# para modificar as idades menores que 17 para 18
print(serie_age.loc[serie_age < 18])
serie_age = serie_age.apply(lambda x: 17 if x == 18 else x)  # utilizando
# lambda para voltar as idades normais: x recebe 17 se x for igual a 18,
# caso contrario retorne x
print(serie_age.loc[serie_age < 18])
print('------WHERE------')
serie_age_2 = serie_age.iloc[0:6]
print(serie_age_2.where(serie_age_2 < 40, 0))