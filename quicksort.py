
def quicksort(ls):
   if len(ls) < 2 : return ls
   else:
      return   quicksort([ smaller for smaller in ls[1:] if smaller <= ls[0] ]) + \
               [ls[0]] + \
               quicksort([ bigger for bigger in ls[1:] if bigger > ls[0] ])

if __name__ == '__main__':
   print(quicksort([]))
   print(quicksort([2, 4, 1, 3, 5, 8, 6, 7]))
   print(quicksort("pineapple"))
   print(''.join(quicksort('pineapple')))
