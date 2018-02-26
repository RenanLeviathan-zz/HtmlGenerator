#-*- coding: utf-8 -*-
"""
Programa para gerar tags html
Autor: Renan Duarte
"""
from sys import *
from tag import Tag
from csv_reader import *
r = Reader()
print("Uso:\n hg.py [ano] [conselho] [nome] [saida]\nEx.: hg.py 1978 consepe 1978.csv 1978.txt\n")
ano=""
cons=""
nome=""
output=""
if len(argv)>1:
    ano = argv[1]
    cons = argv[2]
    nome = argv[3]
    output = argv[4]
else:
    ano = input("Ano:")
    cons=input("Conselho:")
    nome = input("Arquivo de entrada:")
    output = input("Arquivo de saída:")
data = r.get_data(nome)
arq = open(output,'w')
arq.write('''
<tr>
             <td>&nbsp;</td>
             <td colspan="2" class="text2">{}</td>
           </tr>
'''.format(ano))
for d in data:
	t = Tag(cons,d[0],d[1],d[2],ano)
	arq.write(t.get_html())
arq.close()