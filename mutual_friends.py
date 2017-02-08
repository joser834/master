import itertools
import sys

for line in sys.stdin:
lista = line.strip()
lista = line.split("\t")
elemento = int(lista[0])

if len(lista)>=2:
amigos = lista[1].split(",")
amigos = sorted(map(int, friends))

for usuario in amigos:
lista_dos = tuple(sorted([elemento, amigos]))
lista_dos = ','.join(map(str,pair))
print lista_dos,"\t",1

for lista_dos in itertools.combinations(amigos,2):
lista_dos = ','.join(map(str,pair))
print lista_dos,"\t",0
