import pandas as pd
import matplotlib.pyplot as plt


def grafico_com_mais_medalhas():
    df = pd.read_excel('data/Medals.xlsx')
    df.set_index('Rank', inplace=True)
    df['total'] = df['Gold'] + df['Silver'] + df['Bronze']
    df = df.loc[1:15, ['Team/NOC', 'Gold', 'Silver', 'Bronze', 'total']]

    plt.title("Paises que Ganharão Mais Medalhas ")
    plt.pie(df["Gold"], labels=df["Team/NOC"])
    plt.show()


def grafico_com_total_de_participacao_dos_dois_sexo():
    df = pd.read_excel('data/popularsports.xlsx')
    df = df.loc[1:10, ['Discipline', 'Male', 'Female']]

    plt.title("As Modalidades Que Possuem Mais Prática Dos Dois Sexso ")
    plt.pie(df["Male"], labels=df["Discipline"])
    plt.show()