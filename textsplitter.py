
from pathlib import Path
import pathlib


def main():
    print("Remember to add file extension   (.log, .txt..) ")
    src_filename = input("file name: ")    # custom input
    # src_filename = "your_text_file.log"  # hard coding
    fr = open(src_filename, "r")
    path = str(pathlib.Path().parent.absolute()) + "/" + src_filename
    noext_filename = Path(path).resolve().stem
    ext = str(pathlib.Path(src_filename).suffix)
    i = k = 0
    cont = 1
    for line in fr:
        i += 1
    print("Found " + str(i) + " lines.")
    part = int(input("In how many partitions do you want to split the file: "))
    val = int(i/part)
    fr.seek(0, 0)
    while (cont <= part):
        f = open(noext_filename + "-part-" + str(cont) + ext, "w")
        while(k < val*cont):
            line = str(fr.readline())
            if not line:
                break
            f.write(line)
            k += 1
        f.close()
        cont += 1


if(__name__ == "__main__"):
    main()
