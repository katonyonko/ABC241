import io
import sys

_INPUT = """\
6
9 0 1 2 3 4 5 6 7 8
4 8 8 8 0 8 8 8 8 8
0 0 0 0 0 0 0 0 0 0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A=list(map(int,input().split()))
  d={}
  for i in range(10):
    d[i]=A[i]
  ans=0
  for i in range(3):
    ans=d[ans]
  print(ans)