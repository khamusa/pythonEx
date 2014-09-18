
from itertools import cycle
class fifo():
   def __init__(self, plist):
      self._plist = sorted(plist)
      print(self._plist)

   def __iter__(self):
      self._last = 0
      return iter(self._plist)

class round_robin():

   def __init__(self, plist):
      plist = cycle(plist)
      for i in range(20):
         print(next(plist))


   def __iter__(self):
      self._last = 0
      return iter(self._plist)

class process():
   def __init__(self, name, myquantum, priority = float("-inf")):
      self._name = name
      self._myquantum = self._curquantum = myquantum
      self._priority = priority
      self._pending = True if myquantum <= 0 else False

   def run(self, maxquantum = float("inf")):
      print(self._name, "will run for a", maxquantum)
      self._curquantum = int(maxquantum != float("inf") and max([self._curquantum - maxquantum, 0]))

      self._pending = self._curquantum <= 0         

      print(self._name, "current quantum is now", self._curquantum, "finished:", self._pending)

   def __lt__(self, other):
      return self._priority < other._priority

   def __repr__(self):
      return str(self)

   def __str__(self):
      return "{}({}/{}, {})".format(self._name, self._curquantum, \
                        self._myquantum, self._priority)

class scheduler():
   def __init__(self, plist, ordering):
      for p in plist:
         p.run(4)


   def scheduling(self): pass

if __name__ == "__main__":
   pl = [process("one", 10), process("two", 3, 5), process("three", 15), \
   process("four", 30, 5), process("five", 10), process("six", 6, 10), \
   process("seven", 10), process("eight", 25, 5)]
   print("fifo scheduling")
   s = scheduler(pl, fifo)
   s.scheduling()
   print("round-robin scheduling")
   s = scheduler(pl, round_robin)
   s.scheduling()
   f = fifo(pl)

   for p in f:
      p.run()
      print(p)

   rr = round_robin(pl)
