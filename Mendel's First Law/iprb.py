from tkinter import filedialog
import math

def openfilename():
    path = filedialog.askopenfilename()
    return path

def inherit_dom(filename):
    #homozygous dominant (AA) = HD
    #heterozygous (Aa) = HE
    #homozygous recessive (aa) = HR
    #AA x __ = 100% chance of dominant allele
    #Aa x Aa = 75% chance of dominant allele
    #Aa x aa = 50% chance of dominant allele
    #aa x aa = 0% chance of dominant allele
    #easier to calculate chance of NO dominant allele then subtract probability from 1
    f = open(filename).read()
    values = f.split(" ")
    file = list(map(int, values))
    dom = file[0]
    het = file[1]
    rec = file[2]
    n_combos = math.comb(dom, 2) + math.comb(het, 2) + math.comb(rec, 2) + dom*het + het*rec + dom*rec
    HE_HE = 0.25 #chance of no dominant allele
    HE_HR = 0.5 #chance of no dominant allele
    HR_HR = 1 #chance of no dominant allele
    probability = 1 - (math.comb(het, 2)*HE_HE/n_combos + het*rec*HE_HR/n_combos + math.comb(rec, 2)*HR_HR/n_combos)
    output = open("iprb.txt", "w")
    output.write(str(probability))

file = openfilename()
inherit_dom(file)