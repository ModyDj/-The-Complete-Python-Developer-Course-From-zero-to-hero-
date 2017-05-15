def Display():
    print("Hello")
    print("Welcome to Python")

def sum(n1, n2):
    z= n1 + n2
    print("sum ={}".format(z))
    return z


def main():
    Display()
    #Result = sum(10, 12)
    sum(10, 12)
    #print("sum ={}".format(Result))
    #Result = sum(12, 133)
    sum(12, 133)
    #print("sum ={}".format(Result))
    #Result = sum(140, 122)
    sum(140, 122)
    #print("sum ={}".format(Result))
if __name__ == '__main__':main()
