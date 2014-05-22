do_it = lambda f,x: f(x)
f1 = lambda x: print( "{0} yay f1!".format(x) )
f2 = lambda x: print( "{0} yay yay f2!".format(x) )
f3 = lambda x: print( "{0} yay yay yay f3!".format(x) )

list( map(lambda x:do_it(x,5),[f1,f2,f3]) )
