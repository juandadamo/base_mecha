# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:29:58 2015
Updated to Python 3
"""
import matplotlib.pyplot as plt
import numpy as np
import glob
import os, textwrap
from html.parser import HTMLParser
from matplotlib.backends.backend_pdf import PdfPages


dir_data = '/home/juan/Documents/personal/MazingerZ/'
plt.close('all')

types = ('*.png', '*.jpg')
files_grabbed = []
for files in types:
    files_grabbed.extend(glob.glob(os.path.join(dir_data, files)))

list_files = np.sort(files_grabbed)
nsize = 8
k = 0

h = HTMLParser()

listado = list_files[::2]
with PdfPages(f'{dir_data}/libro_mechas.pdf') as pdf:
  for i, file_i in enumerate(listado):

    fig1, ax1 = plt.subplots(1, 2, figsize=(11.69, 8.27))

    # Primer monstruo
    nombre_monstruo = os.path.basename(file_i)[3:-4].replace('_', ' ')
    A = plt.imread(file_i)

    txt_file = file_i[:-3] + 'txt'
    with open(txt_file, 'r', encoding='utf-8') as B:
        texto = B.readline()

    texto = texto.replace('<br />', '\n')

    # Limpiar etiquetas HTML
    texto = (texto.replace('<strong>', '')
                .replace('</strong>', '')
                .replace('<em>', '')
                .replace('</em>', ''))

    # Dividir por líneas y aplicar wrap a cada una
    lineas = texto.split('\n')
    lineas_wrapped = []
    for linea in lineas:
        lineas_wrapped.extend(textwrap.wrap(linea, width=42))
    texto_final = '\n'.join(lineas_wrapped)

    m, n, nc = A.shape

    ax1[0].imshow(A)
    ax1[0].set_axis_off()
    # texto_wrapped = '\n'.join(textwrap.wrap(texto, width=40))
    ax1[0].text(0, -m, texto_final, fontsize=14, ha='left', va='top',
                bbox={'edgecolor': 'black', 'facecolor': 'blue',
                      'alpha': 0.2, 'boxstyle': 'round,pad=0.3'})
    ax1[0].text(n/2, m, nombre_monstruo, fontsize=24, ha='center', va='top',wrap=True,
                bbox={'edgecolor': 'white', 'facecolor': 'blue', 'alpha': 0.2, 'boxstyle': 'round'})

    # Segundo monstruo
    file_j = list_files[2*i + 1]
    nombre_monstruo2 = os.path.basename(file_j)[3:-4].replace('_', ' ')
    A2 = plt.imread(file_j)

    txt_file2 = file_j[:-3] + 'txt'
    with open(txt_file2, 'r', encoding='utf-8') as B:
        texto2 = B.readline()

    texto2 = texto2.replace('<br />', '\n')

    # Limpiar etiquetas HTML
    texto2 = (texto2.replace('<strong>', '')
                .replace('</strong>', '')
                .replace('<em>', '')
                .replace('</em>', ''))

    # Dividir por líneas y aplicar wrap a cada una
    lineas = texto2.split('\n')
    lineas_wrapped = []
    for linea in lineas:
        lineas_wrapped.extend(textwrap.wrap(linea, width=42))
    texto2_final = '\n'.join(lineas_wrapped)

    # Mostrar


    m2, n2, nc2 = A2.shape

    ax1[1].imshow(A2)
    ax1[1].set_axis_off()
    texto_wrapped2 = '\n'.join(textwrap.wrap(texto2, width=40))
    # ax1[1].text(n2/2, 0, texto_wrapped2, fontsize=14, ha='center', va='bottom',wrap=True,
    #             bbox={'edgecolor': 'black', 'facecolor': 'blue', 'alpha': 0.2, 'boxstyle': 'round'})
    ax1[1].text(0, -m2, texto2_final, fontsize=14, ha='left', va='top',
                bbox={'edgecolor': 'black', 'facecolor': 'blue',
                      'alpha': 0.2, 'boxstyle': 'round,pad=0.3'})
    ax1[1].text(n2/2, m2, nombre_monstruo2, fontsize=24, ha='center', va='top',wrap=True,
                bbox={'edgecolor': 'white', 'facecolor': 'blue', 'alpha': 0.2, 'boxstyle': 'round'})



    #plt.show()  # o guardar figura
    # raise ValueError()
    pdf.savefig(fig1, bbox_inches='tight')
    # fig1.savefig(f'{dir_data}/libro/{i:02d}{nombre_monstruo}{nombre_monstruo2}.png')
    plt.close(fig1)
print("¡PDF creado!")
