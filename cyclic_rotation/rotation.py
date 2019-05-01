#python
#author : aim
#language: utf8

def solution(A, K):
    from collections import deque
    A=deque(A)
    A.rotate(K)
    return list(A)
