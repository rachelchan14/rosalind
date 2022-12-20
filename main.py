from tkinter import filedialog
from test import x

def openfilename():
    path = filedialog.askopenfilename()
    return path

def hypotenuse(filename):
    values = open(filename).read().split()
    return(int(values[0])**2 + int(values[1])**2)

def split(filename):
    file = open(filename)
    string = file.readline()
    numbers = file.readline().split()
    numbers = list(map(int, numbers))
    temp_str = ""
    temp_str+=(string[numbers[0]:numbers[1] + 1])
    temp_str+=(" ")
    temp_str+=(string[numbers[2]:numbers[3] + 1])
    return temp_str

def sum_odd(filename):
    numbers = open(filename).read().split()
    numbers = list(map(int, numbers))
    sum = 0
    for i in range(numbers[0], numbers[1] + 1):
        if (i % 2 == 1):
            sum+=i
    return sum

def even_lines(filename):
    all_lines = open(filename).readlines()
    for line in range(len(all_lines)):
        if line % 2 == 1:
            print(all_lines[line])

def dictionary(filename):
    words = open(filename).read().split()
    my_dict = {}
    # for word in words:
    #     if word in my_dict:
    #         my_dict[word] += 1
    #     else:
    #         my_dict[word] = 1
    # for key, value in my_dict.items():
    #     print (key, value)
    for word in words:
        my_dict[word] = my_dict.get(word, 0) + 1
        #get function = get(target key, value to designate key if not found in dictionary)
    for key, value in my_dict.items():
        print (key, value)

def countingDNAnucleotides(filename):
    nucleotides = open(filename).read()
    # my_dict = {}
    # for i in nucleotides:
    #     if (i == '\n'):
    #         continue
    #     my_dict[i] = my_dict.get(i, 0) + 1
    # ordered = sorted(my_dict.items())
    # dict(ordered)
    # for value in ordered:
    #     print (value[1], end = " ")
    print(nucleotides.count('A'), nucleotides.count('C'), nucleotides.count('G'), nucleotides.count('T')) #kind of like get but in non-dictionary version

def transcribe(filename):
    nucleotides = open(filename).read()
    return(nucleotides.replace('T','U'))

def reverse_complement(filename):
    original = open(filename).read()
    reverse = ""
    i = len(original) - 1
    while i >= 0:
        reverse += original[i]
        i-=1
    new_seq = ""
    for i in reverse:
        if (i == 'A'):
            new_seq += 'T'
        elif (i == 'T'):
            new_seq += 'A'
        elif (i == 'G'):
            new_seq += 'C'
        elif (i == 'C'):
            new_seq += 'G'
    return(new_seq)

def rabbits_helper(ready, new, months, new_pairs):
    if (months == 0):
        return (ready + new)
    return (rabbits_helper(new + ready, ready * new_pairs, months-1, new_pairs))

def rabbits(filename):
    values = open(filename).read().split(" ")
    return(rabbits_helper(0, 1, int(values[0])-1, int(values[1])))

def gc(filename):
    filelines = open(filename).readlines()
    max_gc = 0.0
    max_name = filelines[0][1:]
    line = 0
    while (line < len(filelines)):
        if (filelines[line][0] == '>'):
            name = filelines[line][1:]
            gc = 0
            length = 0
            line+=1
        while (line < len(filelines) and filelines[line][0] != '>'):
            gc = gc + filelines[line].count('G') + filelines[line].count('C')
            length += len(filelines[line]) - 1
            print(line, length, gc)
            line+=1
        gc_percent = 100.0*gc/(length)
        if (gc_percent > max_gc):
            max_gc = gc_percent
            max_name = name
    print (max_name,max_gc)

#file = openfilename()
#gc(file)
#print (x)
#print ("2 multiplied by 8: {}".format(2*8)) #curly braces are like placeholders and the format is for the actual value
#print ("125.6 divided by 7: {: .2f}".format (125.6/7)) #specify number of decimal places
# a = 18
# b = 3
# print ("a times b: %2i " %(a*b)) #% is a placeholder as well, length of placeholder followed by type (i for integer, s for string, f for float)
#genomic_dna = ['nucleic', 'plasmid', 'mitochondrial']
#print('+'.join(genomic_dna)) #prints each item in list with designated linker in between