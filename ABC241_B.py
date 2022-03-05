import io
import sys

_INPUT = """\
6
3 2
1 1 3
3 1
1 1
1000000000
1
5 2
1 2 3 4 5
5 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import defaultdict
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  d=defaultdict(int)
  for i in range(N):
    d[A[i]]+=1
  ans='Yes'
  for i in range(M):
    if B[i] in d and d[B[i]]>0:
      d[B[i]]-=1
    else:
      ans='No'
  print(ans)