import time
def isPal(k):
    tmp=str(k)
    xt="".join(reversed(tmp)) 
    if tmp!=xt:
        return False    
    return True

def Palindrome(N):
    start=1
    end=pow(10,N)-1
    count=0
    f=open("new.txt","w")
    f.write("Palindromes Upto 10 Million \n\t\t\t\t --created by Abhishek Kale \n\n")
    sT=time.time()
    for i in range(start,end):
        if isPal(i):
            print(i)
            f.write(str(i)+" seconds\n")
    eT=time.time()
    tstr="Execution Time : "+str(eT-sT)+"\n"
    f.write(tstr)
    f.write("\nEOF")
    f.close()        
Palindrome(8)