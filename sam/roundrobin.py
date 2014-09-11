from itertools import *
def roundrobin2(*iterables):
   # roundrobin(’ABC’, ’D’, ’EF’) --> A D E B F C
   # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending)) # this is the key


list(roundrobin2("ABCDEF", "GH", "IJ", "K", "LMNO"))

# When we call islice, nexts is a cycle iterator that just stopped
# because of a StopIteration. This means that the last iterator considered
# is now depleted. When we decrease pending and make a slice over a cycle
# iterator, we remove exactly that last considered (depleted) iterator!
