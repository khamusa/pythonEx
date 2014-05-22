"""
Similarly to the ls-l example please implement:

The cat command, i.e., a command that given a list of files prints their content on the terminal 
(man cat to get more info)
The chmod command, i.e., a command that permits to change the access mode of a given group of files 
(man chmod to get more info)
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

perms = {
   # group
   0 : {
      0: 0,
      1: stat.S_IXGRP,
      2: stat.S_IWGRP,
      4: stat.S_IRGRP,
      5: stat.S_IXGRP | stat.S_IRGRP,
      6: stat.S_IWGRP | stat.S_IRGRP,
      7: stat.S_IXGRP | stat.S_IRGRP | stat.S_IWGRP 
   },
   # user
   1 : {
      0: 0,
      1: stat.S_IXUSR,
      2: stat.S_IWUSR,
      4: stat.S_IRUSR,
      5: stat.S_IXUSR | stat.S_IRUSR,
      6: stat.S_IWUSR | stat.S_IRUSR,
      7: stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR 
   } ,
   # other
   2 : {
      0: 0,
      1: stat.S_IXOTH,
      2: stat.S_IWOTH,
      4: stat.S_IROTH,
      5: stat.S_IXOTH | stat.S_IROTH,
      6: stat.S_IWOTH | stat.S_IROTH,
      7: stat.S_IXOTH | stat.S_IROTH | stat.S_IWOTH 
   }
}

# Add symbolic keys too, to the perms hash, referencing other already existing objects
for perm_category in perms.keys():
   perms[perm_category]["r"] = perms[perm_category][4]
   perms[perm_category]["w"] = perms[perm_category][2]
   perms[perm_category]["x"] = perms[perm_category][1]

perms["g"] = perms[0]
perms["u"] = perms[1]
perms["o"] = perms[2]


# Handle a numeric permission string (ex. 777) - No validation is performed
def chmod_numerical(filename, perm_string):
   final_privs = 0
   for guo_index, perm_number in enumerate(perm_string):
      final_privs |= perms[guo_index][int(perm_number)]

   os.chmod(filename, final_privs)

# Handle a symbolic permssion string - No validation is performed
def chmod_symbolic(filename, perm_string):
   guos, operation, assigned_perms = re.split("(=|\+|-)", perm_string)

   to_assign = 0
   # cycle on every category letter "g", "u", "o" - before the operator
   for guo in guos:
      category = perms[guo]
      
      for char in assigned_perms:
         to_assign |= category[ char ]

   # Decide how to_assign will be related to the current file permissions
   current_file_perms = os.stat(filename).st_mode
   if( "+" == operation ):
      to_assign |= current_file_perms # OR (just add)
   elif ( "-" == operation ):
      to_assign = current_file_perms & ~to_assign # to_assign & !current_file_perms

   os.chmod(filename, to_assign)

# Main function, entry point - No validation is performed
def chmod(filename, perm_string):
   if(perm_string.isdigit()):
      chmod_numerical(filename, perm_string)
   else:
      chmod_symbolic(filename, perm_string)

if __name__ == '__main__':
   cat(argv[1])
   chmod(argv[1], argv[2])