import math

def powerSum(X, N):
    return evalu(X,N,0,0)


def evalu(X,N,i,S):
    if ( X == S ):
        return 1
    if (X < S):
        return 0
    sum = 0
    for k in range(i+1,int(math.pow(X,1/N)) + 1):
        sum = sum + evalu(X,N,k,S+(k**N))
    return sum

print(powerSum(100,2))
