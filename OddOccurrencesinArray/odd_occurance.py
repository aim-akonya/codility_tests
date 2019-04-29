def solution(A):
    if len(A)==1:
        return A[0]
    A.sort()
    i=0
    try:
        while (i<len(A) and A[i]==A[i+1]):
            i+=2
        return A[i]
    except:
        while (i<len(A)-1 and A[i]==A[i+1]):
            i+=2
        return A[i]
    pass
