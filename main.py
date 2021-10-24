import pandas as pd


def total_participants_by_sport():
    """
    Total de participantes por esporte.
    :return: pandas.core.series.Series
    """
    dt = pd.read_excel('data/Athletes.xlsx')
    return dt['Discipline'].value_counts()
