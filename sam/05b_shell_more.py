"""
The more command, i.e., a command that given a file prints its content 30 rows at a time and way a 
keystroke after every 30 rows to print the next 30.
"""
import sys
def more(filename):
   with open(filename, encoding = 'utf-8') as a_file:
      for index, line in enumerate(a_file):
         print("{0:>5}  {1}".format(index, line), end = '')
         if((index + 1) % 27 == 0):
            print("[ Press enter to display more lines, q to quit ]")
            if(sys.stdin.read(1) == "q"):
               break

if __name__ == '__main__':
   more(sys.argv[1])
