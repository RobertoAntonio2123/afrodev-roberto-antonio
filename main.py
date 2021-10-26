import sys
import untitled
import graphic
from tables import *
import pandas as pd
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow
from tables import *

class final_result(QMainWindow,untitled.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
 #link dos botões
        self.totalAtleta.clicked.connect(self.x1)
        self.totalPaticipates.clicked.connect(self.x2)
        self.totalFeminino.clicked.connect(self.x3)
        self.totalMedalha.clicked.connect(self.x4)
        self.totalMedalhapa.clicked.connect(self.x5)
        self.ranking.clicked.connect(self.x6)
        self.paisMais.clicked.connect(self.x7)
        self.paisMenos.clicked.connect(self.x8)
        self.quantiEsport.clicked.connect(self.x9)
        self.timePais.clicked.connect(self.x10)
        self.totalTreina.clicked.connect(self.x11)
        self.quantidadeTime.clicked.connect(self.x12)
        self.totalAtletaa.clicked.connect(self.x13)

        # Botão dos graficos

        self.grafico1.clicked.connect(self.x14)
        self.grafico2.clicked.connect(self.x15)

    def x14(self):
        graphic.grafico_com_mais_medalhas()

    def x15(self):
        graphic.grafico_com_total_de_participacao_dos_dois_sexo()

# botão
    def x1(self):
        self.labelRetorno.setText(
            str(total_participating_participants())
        )

    def x2(self):
        self.labelRetorno.setText(
            str(total_male_participants())
        )

    def x3(self):
        self.labelRetorno.setText(
            str(total_female_participants())
        )

    def x4(self):
        self.labelRetorno.setText(
            str(total_participants_by_sport())
        )

    def x5(self):
        self.labelRetorno.setText(
            str(total_medals_by_country())
        )

    def x6(self):
        self.labelRetorno.setText(
            str(ranking_by_total_medals())
        )

    def x7(self):
        self.labelRetorno.setText(
            str(The_countries_that_will_have_the_most_medals())
        )

    def x8(self):
        self.labelRetorno.setText(
            str(country_with_fewer_medals())
        )

    def x9(self):
        self.labelRetorno.setText(
            str(list_with_participating_sports())
        )

    def x11(self):
        self.labelRetorno.setText(
            str(number_of_coaches_per_sport())
        )

    def x12(self):
        self.labelRetorno.setText(
            str(how_wany_times_per_sport_each_country_has())
        )

    def x13(self):
        self.labelRetorno.setText(
            str(Type_of_sport_for_male_and_female())
        )

    def x10(self):
        self.labelRetorno.setText(
            str(number_of_coaches_per_country())
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera = final_result()
    gera.show()
    qt.exec_()
