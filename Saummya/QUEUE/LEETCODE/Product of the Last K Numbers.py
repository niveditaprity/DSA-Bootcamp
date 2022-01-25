class ProductOfNumbers:

    def __init__(self):
        self.vec=[1]
        

    def add(self, num: int) -> None:
        if num==0:
            self.vec=[1]
        else:
            self.vec.append(self.vec[-1]*num)
        

    def getProduct(self, k: int) -> int:
        x=len(self.vec)-1
        if x-k<0:
            return 0
        return self.vec[x]//self.vec[x-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
