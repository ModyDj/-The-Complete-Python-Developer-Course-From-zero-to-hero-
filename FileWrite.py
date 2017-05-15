def main():
    # Write to file
    out = open("text.txt", "a")
    for i in range(5):
        inputToFile = input("Enter String to write to file:")
        out.write("\n name is {}".format(inputToFile))
    out.close()


if __name__ == '__main__':main()
