"""
Your module description
"""

import re

#ouvrir le fichier en lecture
newfile = open ('preproinsulin-seq.txt','r')
#récupérer le contenu du fichier
preproinsulin = newfile.read()
#supprimer les caractères ORIGIN , 1 , 61 , // , les espaces et les chariots de retour
""" Méthode 1
x = ''.join(filter(str.isalnum, preproinsulin))
y = re.sub("ORIGIN", "", x)
z = re.sub("\d", "", y) """

""" Méthode 2 """

z = re.sub(r'\d{1,2}|ORIGIN|\s|\/\/',"",preproinsulin)

print(z) 
#ouvrir le dernier fichier et y écrire le résultat 
file = open ('preproinsulin-seq-clean.txt','w')
file.write(z)
#fermer le fichier de travail
newfile.close()
#vérifier la longueur de la chaine
print(len(z))
#extraire des caractères 1 à 24
zn = z[0:24]
print(zn)
#écriture sur le fichier
fileIsinsulin = open ('lsinsulin-seq-clean.txt','w')
fileIsinsulin.write(zn)
fileIsinsulin.close()
#extraire les caratères 25-54 et écrire sur le fichier binsulin
bn = z[24:54]
print(bn)
print(len(bn))
bInsulin = open ('binsulin-seq-clean.txt','w')
bInsulin.write(bn)
bInsulin.close()
#extraire les caratères 55-89 et écrire sur le fichier cinsulin
cn = z[54:89]
print(cn)
print(len(cn))
cInsulin = open ('cinsulin-seq-clean.txt','w')
cInsulin.write(cn)
cInsulin.close()
#extraire les caratères 90-110 et écrire sur le fichier ainsulin
an = z[89:110]
print(an)
print(len(an))
aInsulin = open ('ainsulin-seq-clean.txt','w')
aInsulin.write(an)
aInsulin.close()