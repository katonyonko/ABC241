import io
import sys

_INPUT = """\
6
5 3
2 1 6 3 1
10 1000000000000
260522 914575 436426 979445 648772 690081 933447 190629 703497 47202
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  next=[(i+A[i])%N for i in range(N)]
  loop=[]
  looked=set()
  now=0
  while now not in looked:
    loop.append(now)
    looked.add(now)
    now=next[now]
  idx=loop.index(now)
  ll=len(loop)-idx
  ans=0
  init=min(K, idx)
  l=(K-init)//ll
  r=(K-init)%ll
  for i in range(init):
    ans+=A[loop[i]]
  ans+=l*sum([A[loop[i]] for i in range(idx,len(loop))])
  ans+=sum([A[loop[i]] for i in range(idx,idx+r)])
  print(ans)