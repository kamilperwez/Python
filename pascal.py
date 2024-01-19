#PASCAL TRIANGLE
def fac(n):
    dp=[0 for x in range(n+1)]
    dp[0]=1
    if n >=1:
        dp[1]=1
    for i in range(n-1):
        dp[i+2]=(i+2)*dp[i+1]
    return dp[n]
def row(r,c):
    n=fac(r)
    d=fac(c)*fac(r-c)
    return int(n/d)
def mainPascal(nRows):
    for i in range(nRows+1):
        for j in range(i+1):
            print(row(i,j)," ",end="")
        print()
        
def pascal2ndApproach(numRows):
    lit=[[1]*i for i in range(1,numRows+1)]
    for i in range(1,numRows+1):
        c=1
        for j in range(1,i+1):
            lit[i-1][j-1]=c
            c=int(c*(i-j)/j)
    return lit 
    
print("Hello")
mainPascal(10)
print("\n\n2nd Approach ")
print(pascal2ndApproach(10))