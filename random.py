from datetime import datetime as dt       
class Random:
    now=dt.now()
    curr=now.strftime("%H:%M:%S")
    hrs=int(curr[:2])
    mts=int(curr[3:5])
    sec=int(curr[6:]) 
    
    def __init__(self,num=mts): 
        self.num=num
        self.cnt=0 
        n=126+(self.num%125)
        while(self.cnt<n): 
            self.util()
            self.cnt+=1 
    
    def util(self): 
        self.util1()
        self.util2()
        self.util3()
        self.util4()
        self.util5()
        self.util6()

    def util1(self):                   
        val=(self.num-5)*(self.num-7)
        self.num=val 
    
    def util2(self): 
        val=((self.num+3)*(self.num-6))-self.num     
        self.num=val 

    def util3(self): 
        val=(4*self.num)+7 
        self.num=val 
    
    def util4(self): 
        self.num=(3*self.num)-2 
    
    def util5(self): 
        self.num*=((self.num)//(self.hrs+self.cnt)) 

    def util6(self): 
        self.num=self.num%(self.cnt+self.hrs)
        if(self.num%2==0): 
            if(self.cnt%2==0): 
                self.num*=self.cnt
            else: 
                self.num*=self.sec 
        else: 
            if(self.cnt%2==0): 
                self.num+=self.cnt 
            else: 
                self.num+=self.sec 


try: 
    num=int(input("Enter any number if you want or else leave it : "))
    r=Random(num)
except EOFError: 
    r=Random() 
print(r.num)
