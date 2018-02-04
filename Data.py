import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# antall trekte lapper med kryss på
lapper = pd.read_csv('lapper.csv', index_col=0, comment='#')

# prosentandel nordmenn som har kontakt med innvandrere
kontakt = pd.read_csv('kontakt.csv', index_col=0, comment='#')

# prosentandel nordmenn som har positiv holdning til innvandrere
holdning = pd.read_csv('holdning.csv', index_col=0, comment='#')


# Tegner en graf/figur til en pdf-fil
def draw_graph(data, pdf, param_dict=None):
    if param_dict is None:
        param_dict = {}

    fig, ax = plt.subplots(2)
    data.plot(ax=ax[0], **param_dict)

    plt.rcParams.update({'legend.fontsize': 6})

    ax[1].axis('off')

    gjennomsnitt = [round(data.mean()[0], 2)]
    median = [data.median()[0]]
    modus = data.mode().values
    variasjonsbredde = data.max() - data.min()
    varians = data.var()
    standardavvik = round(data.std(), 2)

    ax[1].table(
        rowLabels=['gjennomsnitt', 'median', 'modus', 'variasjonsbredde', 'varians', 'standardavvik'],
        cellText=[gjennomsnitt, median, modus, variasjonsbredde, varians, standardavvik],
        colLabels=None,
        loc="center",
        bbox=(0.2, -0.2, 0.8, 1),
        cellLoc='left')

    pdf.savefig()
    plt.close()


def main():
    with PdfPages('rapport.pdf') as pdf:
        draw_graph(lapper, pdf, {'kind': 'bar'})
        draw_graph(kontakt, pdf)
        draw_graph(holdning, pdf)

        print("PDF SAVED!")


if __name__ == '__main__':
    main()
