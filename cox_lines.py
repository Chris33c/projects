FileList = []

def OpenFile(filename):
    File = open(filename, 'r')
    File.readline()
    for line in File:
        line = line.strip()
        FileList.append(line)
    File.close()
def main():
    File = input("Enter a file name: ")
    OpenFile(File)
    while True:
        Line = input("Enter a line by number: ")
        print(FileList[Line])
        if Line > len(FileList):
            print("That line does not exist. Please try again.")
        elif Line == 0:
            break
main()        




