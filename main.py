import pandas as pd


def total_participating_participants():

    """
    Total de participantes participantes.
    :return: class 'numpy.int64'
    """
    dt = pd.read_excel('data/Athletes.xlsx')
    return dt.describe()['Name']['count']


def total_male_participants():
    """
    Total de participantes homens.
    :return: lass 'numpy.int64
    """
    dt = pd.read_excel('data/EntriesGender.xlsx')
    return dt['Male'].sum()


def total_female_participants():
    """
    Total de participantes mulheres.
    :return:class 'numpy.int64
    """
    dp = pd.read_excel('data/EntriesGender.xlsx')
    return dp['Female'].sum()


def total_participants_by_sport():
    """
    Total de participantes por esporte.
    :return: pandas.core.series.Series
    """
    dt = pd.read_excel('data/Athletes.xlsx')
    return dt['Discipline'].value_counts()


def total_medals_by_country():
    """
    Total de medalhas por país.
    :return:class 'pandas.core.frame.DataFrame'
    """
    dt = pd.read_excel('data/Medals.xlsx')
    dt['total'] = dt['Gold'] + dt['Silver'] + dt['Bronze']
    return dt[['Team/NOC', 'total']]


def ranking_by_total_medals():
    """
    Ranking por medalhas totais.
    :return:class 'pandas.core.frame.DataFrame'
    """
    df = pd.read_excel('data/Medals.xlsx')
    df.set_index('Rank', inplace=True)
    df['total'] = df['Gold'] + df['Silver'] + df['Bronze']
    return df.sort_values('total', ascending=False, inplace=True)


def country_with_the_most_gold_medals():
    """
    País com mais medalhas de ouro.

    :return:class 'pandas.core.frame.DataFrame'
    """
    dt = pd.read_excel('data/Medals.xlsx')
    dt.set_index('Team/NOC', inplace=True)
    columns = ['Rank', 'Silver', 'Bronze']
    dt.drop(columns, inplace=True, axis=1)
    return dt.describe()['Gold']['max']


def country_with_the_most_silver_medals():
    """
    País com mais medalhas de prata.
    :return:class 'pandas.core.frame.DataFrame
    """
    dt = pd.read_excel('data/Medals.xlsx')
    dt.set_index('Team/NOC', inplace=True)
    columns = ['Rank', 'Gold', 'Bronze']
    dt.drop(columns, inplace=True, axis=1)
    return dt.describe()['Silver']['max']


def country_with_the_most_bronze_medals():
    """
    País com mais medalhas de bronze.
    :return:class 'pandas.core.frame.DataFrame
    """
    dt = pd.read_excel('data/Medals.xlsx')
    dt.set_index('Team/NOC', inplace=True)
    columns = ['Rank', 'Gold', 'Silver']
    dt.drop(columns, inplace=True, axis=1)
    return dt.describe()['Bronze']['max']


def Country_with_the_fewest_gold_medals():
    """
    País com menos medalhas de ouro
    :return:class 'pandas.core.frame.DataFrame'
    """
    dt = pd.read_excel('data/Medals.xlsx')
    dt.set_index('Team/NOC', inplace=True)
    columns = ['Rank', 'Silver', 'Bronze']
    dt.drop(columns, inplace=True, axis=1)
    return dt.describe()['Gold']['min']


def country_with_the_fewest_silver_medals():
    """
    País com menos medalhas de prata.
    :return:class 'pandas.core.frame.DataFrame'
    """
    dt = pd.read_excel('data/Medals.xlsx')
    dt.set_index('Team/NOC', inplace=True)
    columns = ['Rank', 'Gold', 'Bronze']
    dt.drop(columns, inplace=True, axis=1)
    return dt.describe()['Silver']['min']


def country_with_the_fewest_bronze_medals():
    """
    País com menos medalhas de bronze.
    :return:class 'pandas.core.frame.DataFrame'
    """
    dt = pd.read_excel('data/Medals.xlsx')
    dt.set_index('Team/NOC', inplace=True)
    columns = ['Rank', 'Gold', 'Silver']
    dt.drop(columns, inplace=True, axis=1)
    return dt.describe()['Bronze']['min']



def list_with_participating_sports():
    """
    Lista com esportes participantes.
    :return:class 'pandas.core.frame.DataFrame'
    """
    df = pd.read_excel('data/Athletes.xlsx')
    return df['Discipline'].value_counts()


def men_and_women_sport_list():
    """
     Lista de esportes com mais homens que mulheres.
	:return:class 'pandas.core.frame.DataFrame'
	"""
    df = pd.read_excel('data/EntriesGender.xlsx')
    return df.set_index('Discipline', inplace=True)


def number_of_coaches_per_country():
    """
    Quantidade de treinadores por país
    País com a maior quantidade de treinadores
    :return: <class 'pandas.core.series.Series'>
    """
    df = pd.read_excel('data/Coaches.xlsx')
    df.drop(['Discipline'], inplace=True, axis=1)
    return df['NOC'].value_counts()


def number_of_coaches_per_sport():
    """
    Quantidade de treinadores por esporte
    :return:<class 'pandas.core.series.Series'>
    """
    df = pd.read_excel('data/Coaches.xlsx')
    df.drop(['NOC'], inplace=True, axis=1)
    return df['Discipline'].value_counts()



