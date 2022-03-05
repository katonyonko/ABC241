from email.policy import default
import io
import sys

_INPUT = """\
6
7 8 7
3 4
5 6
1 4
2 1
2 8
4 5
5 7
6 2
6 6
4 6 2
3 2
3 5
4 5
2 5
1 10 1
1 5
1 1
1 7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #BFS
  from collections import deque
  def bfs(G,s):
    inf=10**30
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D[1]
  from collections import defaultdict
  H,W,N=map(int,input().split())
  sx,sy=map(int,input().split())
  gx,gy=map(int,input().split())
  v=[tuple(map(int,input().split())) for _ in range(N)]
  vv=set(v)
  vv.add((sx,sy))
  vv.add((gx,gy))
  d={(sx,sy):0, (gx,gy):1}
  now=2
  ddr=defaultdict(list)
  ddc=defaultdict(list)
  ddr[sx].append((sy,1))
  ddc[sy].append((sx,1))
  ddr[gx].append((gy,1))
  ddc[gy].append((gx,1))
  for i in range(N):
    ddr[v[i][0]].append((v[i][1],0))
    ddc[v[i][1]].append((v[i][0],0))
    for j,k in [[v[i][0]-1,v[i][1]],[v[i][0]+1,v[i][1]],[v[i][0],v[i][1]-1],[v[i][0],v[i][1]+1]]:
      if 1<=j<=H and 1<=k<=W and (j,k) not in vv and (j,k) not in d:
        ddr[j].append((k,1))
        ddc[k].append((j,1))
        d[(j,k)]=now
        now+=1
  G=[set() for _ in range(now)]
  for key in ddr:
    ddr[key].sort(key=lambda x:x[0])
    i=0
    while i <len(ddr[key]):
      if ddr[key][i][1]==0:
        p=(key,ddr[key][i][0]+1)
        i+=1
        if p in d:
          while i<len(ddr[key]) and ddr[key][i][1]==1:
            if ddr[key][i][0]!=p[1]:
              G[d[(key,ddr[key][i][0])]].add(d[p])
            i+=1
      else: i+=1
    i=len(ddr[key])-1
    while i >=0:
      if ddr[key][i][1]==0:
        p=(key,ddr[key][i][0]-1)
        i-=1
        if p in d:
          while i>=0 and ddr[key][i][1]==1:
            if ddr[key][i][0]!=p[1]:
              G[d[(key,ddr[key][i][0])]].add(d[p])
            i-=1
      else: i-=1

  for key in ddc:
    ddc[key].sort(key=lambda x:x[0])
    i=0
    while i <len(ddc[key]):
      if ddc[key][i][1]==0:
        p=(ddc[key][i][0]+1,key)
        i+=1
        if p in d:
          while i<len(ddc[key]) and ddc[key][i][1]==1:
            if ddc[key][i][0]!=p[0]:
              G[d[(ddc[key][i][0],key)]].add(d[p])
            i+=1
      else: i+=1
    i=len(ddc[key])-1
    while i >=0:
      if ddc[key][i][1]==0:
        p=(ddc[key][i][0]-1,key)
        i-=1
        if p in d:
          while i>=0 and ddc[key][i][1]==1:
            if ddc[key][i][0]!=p[0]:
              G[d[(ddc[key][i][0],key)]].add(d[p])
            i-=1
      else: i-=1

  ans=bfs(G,0)
  if ans<10**30:
    print(ans)
  else:
    print(-1)