from tkinter import filedialog

def openfilename(): #toopen file via file dialog rather than path name
    path = filedialog.askopenfilename()
    return path

def rabbits_helper(ready, new, months, new_pairs):
    if (months == 0):
        return (ready + new)
    return (rabbits_helper(new + ready, ready * new_pairs, months-1, new_pairs))

def rabbits(filename):
    values = open(filename).read().split(" ")
    output = open("fib_output.txt", "w")
    answer = (rabbits_helper(0, 1, int(values[0])-1, int(values[1])))
    output.write(str(answer))

file = openfilename()
rabbits(file)