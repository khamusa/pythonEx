def identity_matrix(n,m):
  return [ [ 1 if j==i else 0 for i in range(0,n) ] for j in range(0,m)  ]

def square_matrix(n):
  return [[ (x+(n*j))**2 for x in range(1,n+1) ] for j in range(0,n) ]

def traspose(matrix):
  m = len(matrix)
  n = len(matrix[0])
  return [[row[i] for row in matrix] for i in range(len(matrix)+1)]



print(identity_matrix(3,3))
print(square_matrix(3))
print(traspose( [[1,2,3],[4,5,6]] ))



