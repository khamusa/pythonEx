import re
def count_frequencies(filetext):
  """ count words occurence for the file passed by parameter"""
  f = open(filetext,"r")
  count_frequencies_for_line(f,{},0)

def word_is_tracked(word,mem):
  """ check if word is still present in mem """
  return (word in mem)

def check_words(words,index,mem):

  if index>(len(words)-1):
    return mem

  if word_is_tracked(words[index],mem):
    mem[words[index]] = mem[words[index]]+1
  else:
    mem[words[index]] = 1

  return check_words(words,index+1,mem)


def count_frequencies_for_line(f,mem,counter):
  line = f.readline()
  if( not line == '' ):
    words = re.split("\W+",line) # suggerimento di samu: usare findall invece di split :)
    del words[-1] # remove last item
    counter += len(words)
    mem   = check_words(words,0,mem)
    count_frequencies_for_line(f,mem,counter)
  else:
    print( "{0} words founded".format(counter))
    print(mem)


count_frequencies("shortfile")
