"""
A matrix can be represented as a list of lists (rows and columns).

Use the comprehensions to describe the identity matrix 
(the one with all 0s but the 1s on the diagonal) of given size.

Use the comprehensions to describe a square matrix filled with the first n*n integers.

Write a function to transpose a generic matrix independently of the size and content.
Write a function to multiply two matrices non necessarily square matrix.
"""

# Auxiliary functions
def n_rows(m): return len(m)
def n_cols(m): return len(m[0])

def pm(matrix):
   '''print matrix in a more friendly way'''
   print("---" * len(matrix[0])) 
   for i in matrix:
      print(i)
   print("---" * len(matrix[0])) 

def identity(size):
   def num(x, y): return (x == y and 1) or 0
   return [ [num(x, y) for x in range(0, size)] for y in range(0,size) ]

def square(size, fill = 0):
   return [ [fill for x in range(0, size)] for y in range(0,size) ]

def transpose(a):
   return   [
               [  a[col][row]
                  for col in range(0, n_rows(a))
               ]
               for row in range(0, n_cols(a))
            ]

def multiply(a, b):
   '''Assumes a and b are well formed matrixes as list of lists'''
   def build_sum(row, col):
      result = 0
      for i in range(0, n_rows(a)):
         result += a[row][i] * b[i][col]
      return result

   return   [ 
               [ 
                  build_sum(row, col) 
                  for col in range(0, n_cols(b))
               ]         
               for row in range(0, n_rows(a))
            ]

a = [    
      [1, 2, 3],
      [0, 1, 2]
   ]

b = [    
      [1, 0],
      [2, 1],
      [0, 0]
   ]

print(" Identity(3):")
pm(identity(3))
print(" Squares 1 and 0")
pm(square(3, 1))
pm(square(5))
print(" Multiply:")
pm(a)
print(" per ")
pm(b)
print(" result:")
pm(multiply(a, b))

print(" Transpose:")
pm(a)
pm(transpose(a))