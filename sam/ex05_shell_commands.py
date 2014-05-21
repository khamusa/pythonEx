"""
Similarly to the ls-l example please implement:

The cat command, i.e., a command that given a list of files prints their content on the terminal 
(man cat to get more info)
The chmod command, i.e., a command that permits to change the access mode of a given group of files 
(man chmod to get more info)

The more command, i.e., a command that given a file prints its content 30 rows at a time and way a 
keystroke after every 30 rows to print the next 30.
"""

from sys import argv
import os, stat, re
def cat(filename):
   with open(filename, encoding = 'utf-8') as fil:
      for a_line in fil:
         print(a_line, end = '')


"""
CHMOD ALLOWED VALUES
stat.S_ISUID: Set user ID on execution
stat.S_ISGID: Set group ID on execution
stat.S_ENFMT: Record locking enforced
stat.S_ISVTX: Save text image after execution

stat.S_IREAD: Read by owner
stat.S_IWRITE: Write by owner
stat.S_IEXEC: Execute by owner

stat.S_IRWXU: Read, write, and execute by owner

stat.S_IRUSR: Read by owner
stat.S_IWUSR: Write by owner
stat.S_IXUSR: Execute by owner

stat.S_IRWXG: Read, write, and execute by group
stat.S_IRGRP: Read by group
stat.S_IWGRP: Write by group
stat.S_IXGRP: Execute by group

stat.S_IRWXO: Read, write, and execute by others
stat.S_IROTH: Read by others
stat.S_IWOTH: Write by others
stat.S_IXOTH: Execute by others

LINUX PERMISSION BITS
A numeric mode is from one to four octal digits (0-7), derived by adding up the bits with 
values 4, 2, and 1.  Omitted digits  are  assumed  to  be  leading
zeros.  The first digit selects the set user ID (4) and set group ID (2) and restricted 
deletion or sticky (1) attributes.  The second digit selects permis‐
sions for the user who owns the file: read (4), write (2), and execute (1); the third selects 
permissions for other users in the file's group, with the same
values; and the fourth for other users not in the file's group, with the same values.

GUO
4 = read
2 = write
1 = execute
"""

perms = [
   # group
   [
      (1, stat.S_IRGRP),
      (2, stat.S_IWGRP),
      (4, stat.S_IXGRP)
   ],
   # user
   [
      (1, stat.S_IRUSR),
      (2, stat.S_IWUSR),
      (4, stat.S_IXUSR)
   ],
   # other
   [
      (1, stat.S_IROTH),
      (2, stat.S_IWOTH),
      (4, stat.S_IXOTH)
   ]
]

def chmod_numerical(filename, perm_string):
   index = 0 #cycle through group, user, other
   final_privs = 0
   for perm_number in perm_string:
      perm_number = int(perm_number)

      for number, stat in perms[index]:
         if((number & perm_number) != 0):
            print("Aggiungo {} - {} - {}".format(index, number, perm_number))
            final_privs |= stat
      index += 1
   os.chmod(filename, final_privs)

def chmod_symbolic(filename, perm_string):
   # perm string will be on the format [guo][+=-][rwx]
   # sembra funzionare, manca estendere al caso in cui nei caratteri
   # guo vengano passati piu caratteri (per ora funziona solo con uno)
   symbolic_perm_cat = {
      "g": perms[0],
      "u": perms[1],
      "o": perms[2]
   }

   symbolic_perm = {
      "r" : 0,
      "w" : 1,
      "x" : 2
   }

   guo, operation, assigned_perms = re.split("(=|\+|-)", perm_string)
   category = symbolic_perm_cat[guo]

   to_assign = 0
   for char in assigned_perms:
      to_assign |= category[ symbolic_perm[char] ][1]

   current_file_perms = os.stat(filename).st_mode

   if( "+" in operation ):
      to_assign |= current_file_perms # OR (just add)
   elif ( "-" in operation ):
      to_assign ^= current_file_perms # XOR

   os.chmod(filename, to_assign)


def chmod(filename, perm_string):
   if(perm_string.isdigit()):
      chmod_numerical(filename, perm_string)
   else:
      chmod_symbolic(filename, perm_string)

if __name__ == '__main__':
   cat(argv[1])
   chmod(argv[1], argv[2])