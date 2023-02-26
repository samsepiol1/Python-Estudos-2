class Balde:
    def __init__(self,c):
        self.cap=c
        self.vol=0
        self.der=0
        self.cheio=False
    def deposita(self,v):
        self.vol+=v
        if self.vol>self.cap:
            self.cheio=True
            self.der=self.vol-self.cap
            self.vol=self.cap
        return self.vol
    def __repr__(self):
        if self.vol==self.cap:
            return "*%2d*" % self.vol
        else:
            return "[%2d]"%self.vol
if __name__ == "__main__":
    balde=Balde(10)
    d1=balde.deposita(3)
    d2=balde.deposita(4)
    print(balde)
    d3=balde.deposita(5)
    print(balde)
    print(d1,d2,d3)