

f = open("reading_files.py", "r")
print("I've read the file {name} ({encoding}), now I must close it!".format(
   name=f.name,
   encoding=f.encoding))
f.close()

""" Available open modes:
   'r' when the file will only be read
   'w' for only writing (an existing file with the same name will be erased)
   'a' opens the file for appending
         - any data written to the file is automatically added to the end. 
   'r+' opens the file for both reading and writing. 
   'b' appended to the mode opens the file in binary mode: now the data is read
      and written in the form of bytes objects. 
      This mode should be used for all files that don’t contain text.

   The mode argument is optional; 'r' will be assumed if it’s omitted.
"""

with open("reading_files.py", "r") as f:
   print("Using with .... as ...: syntax I don't have to worry about closing files!\n")
   print(" ~~~~Inception! ~~~~ \n"+f.read())

with open("reading_files.py", "r") as f:
   print("Using with .... as ...: syntax I don't have to worry about closing files!\n")
   print("""As you can see the read method reads the whole file. 
            The problem is that you may actually consume the whole
            computer memory by doing this, and it is your problem!
            That's why the read method accepts a second parameter, which
            allows you to specify how many bytes you wanna read. 
            Let's read 300 bytes line at a time! Inception, part 2:""")

   r = f.read(300)
   while r:
      print("\nReading: ")
      print(r)
      r = f.read(300)

print("""
Remember that reading from UTF-8 files a speific amount of bytes might 
cause problems regarding character alignment! The best is to use readline:\n""")

with open("reading_files.py", "r") as f:
   for line in f: # This automatically calls readline() at every iteration
      print("Line:", line)

   print("""
I've read the file {name} ({encoding}, mode {mode}),
and it will be automatically closed!
   writable: {writable}
   closed: {closed}""".format(
      name=f.name,
      encoding=f.encoding,
      mode=f.mode,
      writable=f.writable(),
      closed=f.closed
   ))