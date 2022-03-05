import io
import sys

_INPUT = """\
6
8
........
........
.#.##.#.
........
........
........
........
........
6
######
######
######
######
######
######
10
..........
#..##.....
..........
..........
....#.....
....#.....
.#...#..#.
..........
..........
..........
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=[input() for _ in range(N)]
  ans='No'
  for i in range(N-5):
    for j in range(N):
      if [S[i+k][j] for k in range(6)].count('#')>=4:
        ans='Yes'
  for i in range(N):
    for j in range(N-5):
      if [S[i][j+k] for k in range(6)].count('#')>=4:
        ans='Yes'
  for i in range(N-5):
    for j in range(N-5):
      if [S[i+k][j+k] for k in range(6)].count('#')>=4:
        ans='Yes'
  for i in range(N-5):
    for j in range(5,N):
      if [S[i+k][j-k] for k in range(6)].count('#')>=4:
        ans='Yes'
  print(ans)