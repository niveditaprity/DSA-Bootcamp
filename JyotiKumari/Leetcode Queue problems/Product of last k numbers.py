class ProductOfNumbers:

    def __init__(self):
        self.pro = []

    def add(self, num: int) -> None:
        if(num==0):
            self.pro.clear()
        elif(len(self.pro)==0):
            self.pro.append(num)
        else:
            self.pro.append(self.pro[-1]*num)

    def getProduct(self, k: int) -> int:
        n = len(self.pro)
        if k==n:
            return self.pro[-1]
        elif(k>n):
            return 0
        else:
            return self.pro[-1]//self.pro[n-k-1]