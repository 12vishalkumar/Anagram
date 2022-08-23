import math
import os
import random
import re
import sys
# Complete the 'anagram' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
def anagram(s):
    # Write your code here
    N = len(s)
    if(N%2==0):
        n = N//2
        s1 = s[:n]
        s2 = s[n:]
        c = 0
        for i in s1:
            if i in s2:
                p = s2.find(i)
                s2 = s2[:p] + s2[p+1:]
            else:
                c += 1
        return c      
    else:
        return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = anagram(s)
        fptr.write(str(result) + '\n')
    fptr.close()