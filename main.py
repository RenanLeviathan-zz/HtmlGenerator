#-*- coding: utf-8 -*-
"""
Programa para gerar tags html
Autor: Renan Duarte
"""
from tag import Tag
from csv_reader import *
r = Reader()
ano = input("Ano:")
cons=input("Conselho:")
nome = input("Arquivo de entrada:")
data = r.get_data(nome)
output = input("Arquivo de saída:")
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