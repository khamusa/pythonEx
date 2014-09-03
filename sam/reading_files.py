

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

"""
Okay, we've been consuming a lot of literature lately, now let's start writing some!
"""

import json
poem = ("Subi", ("no pé de manga\n"), "Só para te ver\n", ("Logo", "que", "te", "vi"), "eu", "desci")
print("Let's save the following poem:", poem)

"""
First, we open a new file in writing mode 'w'
"""
with open("literature.masterpiece", 'w') as f:
   """
   Now we convert our complicated poem in json poetry and write it
   """
   f.write(json.dumps(poem))

"""
Now let's read our poem
"""
with open("literature.masterpiece", 'r') as f:
   jsonpoem = f.read()

print(json.loads(jsonpoem))

"""
Note that we've used the 's' version of the methods dump and load
There is also the non-'s' version:
   - json.dump(to_save_object, fileobject) - serializes the object and saves it
      to fileobject (representing an open file in reading mode)
   - json.load(fileobject) - reads from an open file in reading mode.

   Example:
"""

with open("literature.masterpiece", 'r') as f:
   print(json.load(f))

"""
This simple serialization technique can handle lists and dictionaries, but 
serializing arbitrary class instances in JSON requires a bit of extra effort. 
The reference for the json module contains an explanation of this.

See also pickle - the pickle module
Contrary to JSON, pickle is a protocol which allows the serialization of 
arbitrarily complex Python objects. As such, it is specific to Python and 
cannot be used to communicate with applications written in other languages. 
It is also insecure by default: deserializing pickle data coming from an 
untrusted source can execute arbitrary code, if the data was crafted by a 
skilled attacker.
"""

