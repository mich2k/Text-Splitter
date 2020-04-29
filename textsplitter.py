
#!/usr/bin/python3

from pathlib import Path
import pathlib
import tempfile

def print_mult(x, MAX):
    cont = 0
    arr = set()
    for i in range(2, x+1):
        if(x % i == 0):
            cont += 1
            arr.add(i)
            if(cont > MAX):
                break
    print(arr)
    return


def partitions(reading_stream, select, ftmp, totlines):
    # looking how many lines are
    for line in reading_stream:
        if(select == 'y' and not(line.isspace())):
            ftmp.write(line)
            totlines += 1
        elif(select == 'n'):
            totlines += 1
    if(select == 'y'):
        ftmp.seek(0, 0)
    MAX = 15  # maximum number of suggested partitions
    print("Found " + str(totlines) + " lines.")
    print("\nHere you are some suggested legit partition size\\s to use: ")
    print_mult(totlines, MAX)
    part = int(input("\nIn how many partitions do you want to split the file? "))
    if(part > totlines != 0):
        print("Error: partitions greater than totlines!")
        quit()
    if(totlines % part != 0):
        print("Error: partitions number has to be a multiple of your total file lines!")
        quit()
    return part, totlines


def inputf():
    print("Remember to add file extension   (.log, .txt..) ")
    src_filename = input("file name: ")
    reading_stream = open(src_filename, "r")
    select = input(
        "Would you like to exclude whitespaces\\whitelines?\nSuggested 'y'\n[y\\n]    ")
    if(not(select == 'y' or select == 'n')):
        print("Error")
        quit()
    path = str(pathlib.Path().parent.absolute()) + "/" + src_filename
    noext_filename = Path(path).resolve().stem
    ext = str(pathlib.Path(src_filename).suffix)
    if(select == 'y'):
        ftmp = tempfile.TemporaryFile(mode='w+')
        return select, reading_stream, noext_filename, ext, ftmp
    else:
        return select, reading_stream, noext_filename, ext, False


def main():
    select, reading_stream, noext_filename, ext, ftmp = inputf()
    part, totlines = partitions(reading_stream, select, ftmp, 0)
    val = int(totlines/part)
    k = 0
    cont = 1
    reading_stream.seek(0, 0)
    if(select == 'y'):
        ftmp.seek(0, 0)
    linestoprint = int(totlines / part)
    for cont in range(1, part+1):
        f = open(noext_filename + "-part-" + str(cont) + ext, "w")
        for k in range(linestoprint):
            if(select == 'n'):
                line = str(reading_stream.readline())
                f.write(line)
            else:
                line = str(ftmp.readline())
                f.write(line)
        f.close()
        k = 0
    reading_stream.close()
    if(select == 'y'):
        ftmp.close()
    return


if(__name__ == "__main__"):
    main()
