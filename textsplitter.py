
#!/usr/bin/python3

from pathlib import Path
import pathlib
import tempfile

def print_mult(x, MAX):
    cont = 0
    arr=set()
    for i in range (2,x):
        if(x%i==0):
            cont+=1
            if(cont > MAX):
                break
            arr.add(i)
    print(arr)
    return

def partitions(reading_stream, ch, ftmp):
    # looking how many lines are
    for line in reading_stream:
        if(ch == 'y' and not(line.isspace())):
            ftmp.write(line)
            totlines += 1
        elif(ch == 'n'):
            totlines += 1
    ftmp.seek(0, 0)
    MAX = 15 #  maximum number of suggested partitions
    print("Found " + str(totlines) + " lines.")
    part = int(input("In how many partitions do you want to split the file? "))
    print("Here you are " + str(MAX) + " suggested legit partitions to use: ")
    if(part>totlines != 0):
        print("Error: partitions greater than totlines!")
        quit()
    if(totlines%part != 0):
        print("Error: partitions number has to be a multiple of your total file lines!")
        quit()
    return part, totlines

def inputf():
    print("Remember to add file extension   (.log, .txt..) ")
    src_filename = input("file name: ")
    reading_stream = open(src_filename, "r")
    ch = input(
        "Would you like to exclude whitespaces\\whitelines?\nSuggested 'y'\n[y\\n]    ")
    if(not(ch == 'y' or ch == 'n')):
        print("Error")
        quit()
    path = str(pathlib.Path().parent.absolute()) + "/" + src_filename
    noext_filename = Path(path).resolve().stem
    ext = str(pathlib.Path(src_filename).suffix)
    if(ch == 'y'):
        ftmp = tempfile.TemporaryFile(mode='w+')
    return ch, reading_stream, noext_filename, ext, ftmp

def main():
    ch, reading_stream, noext_filename, ext, ftmp = inputf()
    part, totlines = partitions(reading_stream, ch, ftmp)
    val = int(totlines/part)
    k = totlines = 0
    cont = 1
    reading_stream.seek(0, 0)
    ftmp.seek(0, 0)
    while (cont <= part):
        f = open(noext_filename + "-part-" + str(cont) + ext, "w")
        while(k < val):
            if(ch == 'n'):
                f.write(str(reading_stream.readline()))
            else:
                f.write(str(ftmp.readline()))
            k += 1
        f.close()
        cont += 1
        val *= cont
    reading_stream.close()
    if(ch == 'y'):
        ftmp.close()
    return


if(__name__ == "__main__"):
    main()
