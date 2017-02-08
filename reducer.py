import itertools
import sys

numero = 10

def aniadir(usuario,uno,dos,bandera):
if bandera==1:
bandera=True
else:
bandera=False
if uno not in usuario:
usuario[uno]={}
usuario[uno][dos]=[1,False]
else:
if dos in usuario[uno]:
usuario[uno][dos][0]+=1
else:
usuario[uno][dos]=[1,False]
if bandera==True:
usuario[uno][dos][0]-=1
usuario[uno][dos][1]=True


usuarios = {}

for line in sys.stdin:
linea = line.strip()
linea = line.split("\t")
elemento = tuple(map(int,linea[0].strip().split(",")))
    bandera = int(linea[1])
    uno,dos = elemento
    addPair(usuarios,uno,dos,bandera)
    addPair(usuarios,uno,dos,bandera)

for uno in usuarios.keys():
    reco = []
    for dos in usuarios[uno].keys():
        n,bandera = users[uno][dos]
        if flag==False:
            reco.append((dos,n))
    reco = sorted(reco,key=lambda x: x[0])
    reco = sorted(reco,key=lambda x: x[1],reverse=True)
    if len(reco)>0:
        reco = list(map(str,zip(*reco)[0]))
        print uno,"\t",','.join(reco[:numero])
