x=10 #Global Variable
def show():
    global x
    print(x)

def main():
    global x
    x=10 # Local Variable
    print("x= {}".format(x))
    show()



if __name__ == '__main__':main()


print("----------")

def op(x): return (x*2)

print (op(10))
print (op(5))
op1 = lambda x:x*2
print (op1(10))