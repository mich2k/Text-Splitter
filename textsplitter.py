
from pathlib import Path
import pathlib
import tempfile

def main():
    print("Remember to add file extension   (.log, .txt..) ")
    src_filename = input("file name: ")    # custom input
    # src_filename = "your_text_file.log"  # hard coding
    fr = open(src_filename, "r")
    ch = input(
        "Would you like to exclude whitespaces\\whitelines?\nSuggested 'y'\n[y\\n]    ")
    if(not(ch == 'y' or ch == 'n')):
        print("Error")
        return
    path = str(pathlib.Path().parent.absolute()) + "/" + src_filename
    noext_filename = Path(path).resolve().stem
    ext = str(pathlib.Path(src_filename).suffix)
    if(ch == 'y'):
        ftmp = tempfile.TemporaryFile(mode='w+')
    k = totlines = 0
    cont = 1
    for line in fr:
        if(ch == 'y' and not(line.isspace())):
            ftmp.write(line)
            totlines += 1
            continue
        elif(ch == 'n'):
            totlines += 1
    ftmp.seek(0,0)
    for l in ftmp:
        print(l)
    print("Found " + str(totlines) + " lines.")
    part = int(input("In how many partitions do you want to split the file: "))
    if(part > totlines):
        print("Error")
        return
    val = int(totlines/part)
    fr.seek(0, 0)
    while (cont <= part):
        f = open(noext_filename + "-part-" + str(cont) + ext, "w")
        while(k <= val*cont):
            line = str(fr.readline())
            if not line:
                break
            f.write(line)
            k += 1
        f.close()
        cont += 1
    fr.close()
    if(ch == 'y'):
        ftmp.close()

if(__name__ == "__main__"):
    main()
