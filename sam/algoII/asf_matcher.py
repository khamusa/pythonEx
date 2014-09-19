

class ASF:

   def __init__(self, alfabeto, pattern):
      self._delta = {}
      self._pattern = pattern
      self._alfabeto = alfabeto
      m = len(pattern)
      for q in range(0, m + 1): 
         self._delta[q] = {}
         for char in alfabeto:
            k = min(m, q + 1)

            print("Q = {}, K = {}".format(q, k) )
            while not (pattern[0:q]+char).endswith(pattern[0 : k]):
               print(pattern[0:q]+char, "non termina con ",(pattern[0 : k]), \
                  " --- k =", k)
               k -= 1

            print(pattern[0:q]+char, "termina con ",(pattern[0 : k]), " -- k =", k)
            self._delta[q][char] = k

   def find_matches(self, text):
      q = 0
      m = len(self._pattern)
      for i, char in enumerate(text):
         q = self._delta[q].get(char, 0)

         if(q == m):
            yield i - m + 1

asf = ASF("abcdefghijk", "ababaca")
for stato in range(0, len(asf._pattern)):
   assert( asf._delta[stato][asf._pattern[stato]] == stato + 1 )

   for char in asf._alfabeto:
      if char != asf._pattern[stato]:
         assert(asf._delta[stato][char] <= stato)


text = "aaaaaababacafdhkfijjkssaababacad"
g = asf.find_matches(text)

for result in g:
   print(result, text[result:result+len(asf._pattern)])