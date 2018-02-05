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

# Antall minutter brukt på joggetur, 5 intervaller totalt.
joggetur = pd.read_csv('joggetur.csv', index_col=0, comment='#')

# Nedbør (mm) i januar fra 1890 til 1994
nedbor = pd.read_csv('nedbor.csv', index_col=0, comment='#')

# Antall sykler observert på 30 min
sykler = pd.read_csv('sykler.csv', index_col=0, comment='#')

# Antall observerte elbiler (av totalt 100 biler)
biler = pd.read_csv('biler.csv', index_col=0, comment='#')


# Tegner en graf/figur til en pdf-fil
def draw_graph(data, pdf, param_dict=None, table_data=None, title=''):
    if param_dict is None:
        param_dict = {}

    if table_data is None:
        table_data = data

    fig, ax = plt.subplots(2)
    data.plot(ax=ax[0], **param_dict)

    fig.suptitle(title)
    plt.rcParams.update({'legend.fontsize': 6})

    ax[1].axis('off')

    gjennomsnitt = [round(table_data.mean()[0], 2)]
    median = [table_data.median()[0]]
    modus = table_data.mode().values
    modus = [[item for sublist in modus for item in sublist]]
    variasjonsbredde = round(table_data.max() - table_data.min(),2)
    varians = round(table_data.var(),2)
    standardavvik = round(table_data.std(), 2)
    print('\n\n\n\n')

    print('gjennomsnitt : ', gjennomsnitt)
    print('median : ', median)
    print('modus : ', modus)
    print('variasjonsbredde : ', variasjonsbredde)
    print('varians : ', varians)
    print('standardavvik : ', standardavvik)

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
        draw_graph(joggetur, pdf)
        draw_graph(nedbor, pdf)
        draw_graph(biler, pdf, {'kind': 'pie', 'y': 'antall'}, biler.drop('vanlig bil'))  # TODO: Lag kakediagram av denne.
        draw_graph(sykler, pdf, {'kind': 'bar'})

        print("PDF SAVED!")


if __name__ == '__main__':
    main()
