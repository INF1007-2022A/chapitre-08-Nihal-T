#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def comparaisonfichier(file1,file2):
    with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
        for count,line in enumerate (f1):
            line2 = f2.readline()
            if line == line2:
                print("les deux fichiers sont pareil")
            else:
                print(f"la ligne{count+1} est différente dans les deux fichiers")

def tripleespaces(file):
    with open(file,encoding="utf-8")as f1:
        for lignes in f1.readlines():
            for ligne in lignes:
                for i in ligne:
                    if i == ' ':
                        f1.read().replace(' ','   ')
    return f1

def gradetoletters(file1,file2):
    with open(file1, encoding="utf-8")as f1:
        notes = f1.readlines()
    with open(file2,"w",encoding="utf-8") as f2:
        for note in notes:
            for key, value in PERCENTAGE_TO_LETTER.items():
                if value[0] <= int(note) < value[1]:
                    f2.write(int(note)+" "+key)

#5:
def lestenombre(filetxt):
    with open(filetxt) as f1:
        listenumbres = []
        for line in f1.readlines():
            for word in line:
                if word.isnumeric():
                    listenumbres.append(int(word))
    return listenumbres

#6
def exercice6(file1, file2):
    with open (file1, encoding="utf-8") as f1, open(file2,"w", encoding="utf-8")as f2:
        for count, line in enumerate(f1):
            if count %2!=0:
                f2.write(line)
    return f2
        

    



    pass


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
