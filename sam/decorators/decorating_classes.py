

def MakePirate(*args, **kargs):
   print("Creating a decorator parameterized by", args, "and ", kargs)

   def MakePirateIn(aClass):
      class PirateNess:
         def __init__(self, *args, **keyargs):
            # Self is a PirateNess instance
            # args won't contain a reference to the instance being decorated
            # instead, it will contain the arguments passeds
            print("Initiating pirateness:", self, args, keyargs)
            print("This pirate uses enclosing scopes args", args, kargs)
            self.wrapped = aClass(*args, **keyargs)    
            self.fetches = 0

         def __getattr__(self, attrname):
            print('Piratessss!!! ' + attrname, "- self is", self)
            print("This pirate knows the following about the outer world ", args, kargs)
            self.fetches += 1
            if(attrname == 'sail'):
               if("Pirate" not in self.wrapped.__class__.__name__):
                  raise RuntimeError("Only pirates can sail on these seas!")
            return getattr(self.wrapped, attrname)
        
      return PirateNess
   return MakePirateIn

@MakePirate(1, 2, 3, weapon="hook", leg="log")
class APirate:
   def sail(self):
      print("I'm now sailing")


# 2 - equivalent:
dec = MakePirate(5, 6, 7, weapon="legbone", leg=None)
@dec
class APirate2:
   def sail(self):
      print("I'm another pirate, now sailing!")

# 3 - equivalent:
@None or MakePirate(1, not='a pirate')
class SimpleMortal:
   def sail(self):
      print("I'm a simple mortal trying to sail!")


p = APirate()
p2 = APirate2()
p3 = SimpleMortal()
print(p)
print(p.wrapped)
p.sail()
p2.sail()
p3.sail()