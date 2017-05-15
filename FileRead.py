def main():
    try:
        ReadFile = open("text.txt", "r")
        for line in ReadFile:
         print(line)
         ReadFile.close()
    except IOError:
       print("File not found")
if __name__ == '__main__': main()
