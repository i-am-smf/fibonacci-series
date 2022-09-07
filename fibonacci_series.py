class fibonocci:

    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.r = 0
        self.l1 = []
        self.l2 = []
        self.n3 = 0

    def fib1(self,r):
        self.n1,self.n3=1,1
        self.l1.append(1)
        for i in range(r-1):
            self.l1.append(self.n1)
            n4,n5=self.n1,self.n3
            n6=n4+n5
            self.n3=n4
            self.n1=n6

        ans=self.l1
        return ans

    def fib2(self,sv,ev):

        self.n1,self.n2=sv,ev
        
        if self.n1 > self.n2:
            self.n3=self.n1
            self.n1=self.n2
            self.n2=self.n3

        elif self.n1==self.n2:
            a="Invalid Inputs"
            return a

        if self.n1==0:
            self.l2.append(self.n1)
            self.l2.append(1)
            self.n1=1
            self.n3=1

        if self.n1==1:
            self.n3=1
        
        while self.n1<=self.n2:
            self.l2.append(self.n1)
            n4,n5=self.n1,self.n3
            n6=n4+n5
            self.n3=n4
            self.n1=n6

        ans=self.l2
        return ans


f=fibonocci()

print(f.fib1(10))

print(f.fib2(10,1))
