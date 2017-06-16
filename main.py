#-*- coding: utf-8 -*-
"""
Programa para gerar tags html
Autor: Renan Duarte
"""
from tag import Tag
from csv_reader import *
r = Reader()
data = r.get_data("tags.csv");
arq = open("texto.txt",'w')
for d in data:
	t = Tag(d[0],d[1],d[2])
	arq.write(t.get_html())
	
