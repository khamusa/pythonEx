"""
Let's write a module (a pool of functions) that given a quite large text 
(over than 2000 words) 
counts how frequent each word occurs in the text.

The text is read from a file and it is a real text with punctuation 
(i.e., commas, semicolons, ...)
that should be counted.

Note that words with different case should be considered the same.
"""
import re

class FrequencyCounter:
	
   excluded_words = (
      'and', 'the', 'i', 'to', 'a', 'of',
      'my', 'that', 'is', 'in', 'you', 's', 'thou',
      'me', 'not', 'with', 'it', 'for', 'this', 'be',
      'o', 'd', 'as', 'her', 'his', 'he', 'she', 'it',
      'his', 'her', 'by', 'll', 'him', 'do'
   )
   
   def __init__(self, file_stream = None):
      self.cache = {} # empty dict

      if file_stream != None:
         self.from_file(file_stream)

   def from_file(self, file_stream):
      file_stream.seek(0)
      for line in file_stream:
         self.process_line(line)

   def sanitize_str(self, a_str):
      return a_str.lower()

   def process_line(self, a_line):
      ls = re.findall('\w+', self.sanitize_str(a_line))
      for word in ls:
         self.add_word(word)

   def add_word(self, a_word):
      if a_word in self.excluded_words:
         return False

      if a_word not in self.cache:
         self.cache[a_word] = 1
      else:
         self.cache[a_word] += 1

      return True

   def get_words(self):
      return self.cache.keys()

   def get_counts(self):
      return self.cache.items()

   def count_for(self, a_word):
      if a_word in self.cache:
         return self.cache[a_word]
      else:
         return 0

   def top_words(self, limit = 10):
      return sorted(self.get_words(), key = lambda w: self.count_for(w), reverse = True)[:limit + 1]

   def top_counts(self, limit = 10):
      return map( lambda w: (w, self.count_for(w)), self.top_words(limit) )

if __name__ == '__main__':
   a_short_file = open('../diego/shortfile', encoding = 'utf-8')
   short_counter = FrequencyCounter(a_short_file)
   print(short_counter.get_words())

   a_long_file = open('../diego/longfile', encoding = 'utf-8')
   long_counter = FrequencyCounter(a_long_file)
   print("Top words 10 for long text: ")
   print(list(long_counter.top_counts(20)))
