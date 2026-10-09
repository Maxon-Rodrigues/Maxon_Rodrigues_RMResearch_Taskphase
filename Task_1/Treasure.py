#"
table = [["34","21","32","41","25"],
         ["14","42","43","14","31"],
         ["54","45","52","42","23"],
         ["33","15","51","31","35"],
         ["21","52","33","13","23"]]
'''
table = [[],[],[],[],[]]
for row in range(5):
    for col in range(5):
        print("Enter the value of (",row+1,", ",col+1,"):",sep = "", end = " ")
        cell_val = input()
        table[row].append(cell_val)
'''
print("Your table entered is: ")
for row in table:
    print("\t".join(row))
win = False
while not win:
    i_v = input("Enter the initial cell you want to start from: ")
    iteration = [i_v]
    c_v = i_v
    looping = False
    while not looping:
        c_v = table[int(c_v[0])-1][int(c_v[1])-1]
        if c_v in iteration:
            if iteration[-1] == c_v:
                for i in iteration:
                    print("(", i[0], ", ", i[1], ")", sep="", end="\t")
                print()
                print("Treasure Found in ","(", c_v[0], ", ", c_v[1], ")", sep="")
                looping = True
                win = True
            else:
                print("Treasure isn't Found")
                for i in iteration:
                    print("(",i[0],", ",i[1],")", sep = "", end = "\t")
                print("(", c_v[0], ", ", c_v[1], ")",sep = "")
                input("Enter to continue:")
                looping = True
                win=False
        else:
            iteration.append(c_v)

