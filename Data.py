import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from PyPDF2 import PdfFileMerger

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
def draw_graph(data, pdf, title='', param_dict=None, table_data=None):
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

    # print('\n\n\n\n')
    # print('gjennomsnitt : ', gjennomsnitt)
    # print('median : ', median)
    # print('modus : ', modus)
    # print('variasjonsbredde : ', variasjonsbredde)
    # print('varians : ', varians)
    # print('standardavvik : ', standardavvik)

    ax[1].table(
        rowLabels=['gjennomsnitt', 'median', 'modus', 'variasjonsbredde', 'varians', 'standardavvik'],
        cellText=[gjennomsnitt, median, modus, variasjonsbredde, varians, standardavvik],
        colLabels=None,
        loc="center",
        cellLoc='left',
        colWidths=[0.6, 0.4],
        bbox=(0.2, -0.2, 0.8, 1))

    pdf.savefig()
    plt.close()


def main():
    with PdfPages('data.pdf') as pdf:
        draw_graph(nedbor, pdf, 'Datasett 1: Månedlig nedbør i Oslo januar måned')
        draw_graph(biler, pdf, 'Datasett 2: Andel elbiler av parkerte biler (totalt 100)', {'kind': 'pie', 'y': 'antall'}, biler.drop('vanlig bil'))
        draw_graph(sykler, pdf, 'Datasett 3: Antall registrerte sykler i løpet av 30 min', {'kind': 'bar'})
        draw_graph(joggetur, pdf, 'Datasett 4: Tiden det tar å jogge en runde')
        draw_graph(lapper, pdf, 'Datasett 5: Antall trekte lapper med kryss\n'
                                'Det ble trekt 10 lapper, av 100 der halvparten hadde kryss', {'kind': 'bar'})
        draw_graph(kontakt, pdf, 'Datasett 6a: Prosentandel nordmenn\n'
                                 'som hadde kontakt med innvandrere i nabolaget')
        draw_graph(holdning, pdf, 'Datasett 6b: Prosentandel nordmenn som hadde positiv holdning til\n'
                                  'at deres sønn/datter var sammen med innvandrer.')

        print("DATA SAVED!")

    pdfs = ['frontpage.pdf', 'data.pdf']
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(open(pdf, 'rb'))

    with open('rapport.pdf', 'wb') as fout:
        merger.write(fout)

        print("PDFS MERGED TO rapport.pdf")


if __name__ == '__main__':
    main()
