from tkinter import filedialog

def openfilename():
    path = filedialog.askopenfilename()
    return path

def hamming_dist(filename):
    file = open(filename).readlines()
    i = 0
    count = 0
    while (i < len(file[0])):
        if (file[0][i] != file[1][i]):
            count+=1
        i+=1
    output = open("hamm_output.txt", "w")
    output.write(str(count))

file = openfilename()
hamming_dist(file)