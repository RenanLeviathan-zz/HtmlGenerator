#-*- coding: utf-8 -*-
"""
Programa para gerar tags html
Autor: Renan Duarte
"""
from tag import Tag
from csv_reader import *
r = Reader()
ano = input("Ano:")
nome = input("Arquivo de entrada:")
data = r.get_data(nome)
output = input("Arquivo de saída:")
arq = open(output,'w')
for d in data:
	t = Tag(d[0],d[1],d[2],ano)
	arq.write(t.get_html())
arq.close()
