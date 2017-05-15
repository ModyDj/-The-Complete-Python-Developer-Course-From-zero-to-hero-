class Operations:
    def sum(self,n1,n2):
        return n1+n2
    def div(self,n1,n2):
        return n1/n2

class MultiOperations(Operations):
    def mul(self,n1,n2):
        return n1*n2
    def sum(self,n1,n2):
    #   return (n1+n2)*2
        return  super().sum(n1,n2)

def main():
    Mo = MultiOperations()
    print("The Multiply is {}".format(Mo.mul(3, 2)))
    print("The Sum is {}".format(Mo.sum(3, 2)))
    print("The Divide is {}".format(Mo.div(3, 2)))

if __name__ == '__main__':main()
