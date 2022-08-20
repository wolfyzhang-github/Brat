#!/usr/bin/python
import getopt
import sys

inputfile = ''
outputfile = ''


def readfile(filename):
    txt = []
    file = open(filename)
    data = file.readlines()
    for eachline in data:
        data1 = eachline.split('|')[0]
        if ':' in data1:
            data1 = data1.split(':')[1].lstrip().rstrip()
            txt.append(data1)
    file.close()
    return txt


def write(txt):
    file = open(outputfile, "w")
    i = 0
    for eachline in txt:
        for eachchar in eachline:
            file.write(eachchar)
            i = i + 1
            if i % 2 == 0:
                # file.write(' ')
                i = 0
        # file.write('\n')
    file.close()


def main(argv):
    global outputfile, inputfile
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('assembler.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('assembler.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    txt = readfile(inputfile)
    write(txt)
    print('input：', inputfile)
    print('output：', outputfile)


# execute main only if called as a script
if __name__ == "__main__":
    main(sys.argv[1:])
