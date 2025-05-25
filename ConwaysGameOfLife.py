print("Name:T P Aswathi\nusn:1AY24AI109\nsec:O")
grid = [
  [0,1,0],
  [0,1,0],
  [0,1,0]
]

def neighbors(x,y):
  count = 0
  for i in range(x-1,x+2):
    for j in range(y-1,y+2):
      if 0 <= i < 3 and 0 <= j < 3 and (i,j) != (x,y):
        count += grid[i][j]
  return count

def step():
  new_grid = [[0]*3 for _ in range(3)]
  for i in range(3):
    for j in range(3):
      n = neighbors(i,j)
      if grid[i][j] == 1 and n in (2,3):
        new_grid[i][j] = 1
      elif grid[i][j] == 0 and n == 3:
        new_grid[i][j] = 1
  return new_grid

for _ in range(5):
  for row in grid:
    print(''.join(str(c) for c in row))
  print()
  grid = step()
