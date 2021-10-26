import pandas as pd


def total_participating_participants():

    """
    Total de participantes participantes.
    :return: class 'numpy.int64'
    """
    df = pd.read_excel('data/Athletes.xlsx')
    return df.describe()['Name']['count']


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
    return dt.set_index('Team/NOC','total' )


def ranking_by_total_medals():
    """
    Ranking por medalhas totais.
    :return:class 'pandas.core.frame.DataFrame'
    """
    df = pd.read_excel('data/Medals.xlsx')
    df.set_index('Rank', inplace=True)
    df['total'] = df['Gold'] + df['Silver'] + df['Bronze']
    return df.loc[1:3, ['Team/NOC', 'Gold', 'Silver', 'Bronze', 'total']]



def The_countries_that_will_have_the_most_medals():
    """
    Os paises que tiverão mais medalhas .

    :return:class 'pandas.core.frame.DataFrame'
    """
    df = pd.read_excel('data/Medals.xlsx')
    df.drop('Rank', inplace=True, axis=1)
    return df.sort_values('Gold', ascending=False, ignore_index=True)



def country_with_fewer_medals():
    """
    País com menos medalhas de medalhas
    :return:class 'pandas.core.frame.DataFrame'
    """
    df = pd.read_excel('data/Medals.xlsx')
    df.set_index('Team/NOC', inplace=True)
    df.drop('Rank', inplace=True, axis=1)
    return df.sort_values('Gold')


def list_with_participating_sports():
    """
    Lista com esportes participantes.
    :return:class 'pandas.core.frame.DataFrame'
    """
    df = pd.read_excel('data/Athletes.xlsx')
    return df['Discipline'].value_counts()


def number_of_coaches_per_sport():
    """
    Quantidade de treinadores por esporte
    :return:<class 'pandas.core.series.Series'>
    """
    df = pd.read_excel('data/Coaches.xlsx')
    df.drop(['NOC'], inplace=True, axis=1)
    return df['Discipline'].value_counts()


def how_wany_times_per_sport_each_country_has():
    """
    Quanto times por esporte cada país tem..
    :return:<class 'pandas.core.series.Series'>
    """
    df = pd.read_excel('data/Athletes.xlsx')
    df.drop(['Name'], inplace=True, axis=1)
    return df['NOC'].value_counts()

def Type_of_sport_for_male_and_female():
    """
    Tipo de esporte para masculino e feminino
    :return: <class 'pandas.core.series.Series'>
    """

    df = pd.read_excel('data/EntriesGender.xlsx')
    return df.sort_values('Male', ascending=False)

def number_of_coaches_per_country():
    """
    Quantidade de treinadores por país
    País com a maior quantidade de treinadores
    :return: <class 'pandas.core.series.Series'>
    """
    df = pd.read_excel('data/Coaches.xlsx')
    df.drop(['Discipline'], inplace=True, axis=1)
    return df['NOC'].value_counts()