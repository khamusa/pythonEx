

def find_matches(testo, pattern):
   pi = 0 # pattern index
   for i in range(0, len(testo)):
      try:
         for pi in range(0, len(pattern) + 1):
            if(testo[i + pi] != pattern[pi]):
               break
      except IndexError:
         yield i

with open("../verylongfile", "r") as fp:
   text = fp.read()

import time
g = find_matches(text, "quicksort")

for result in g:
   print(result, text[result:result+len("quicksort")])