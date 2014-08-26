def concat(*args, sep = '/'):
   return sep.join(args)


""" Argument unpacking: """
args = [0, 22, 2]
# wrong print(range(args))
print(list(range(*args)))

""" Dictionary unpacking """
args2 = { "nome": "Samuel", "sobrenome": "Gomes", "cor": "azul" }

def myname(idade, nome, sobrenome, cor):
   print(nome, sobrenome, "tem", idade, "anos, e gosta da cor", cor)

myname(28, **args2)


""" Lambda sorting, extracting key from tuples """
objects = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
objects.sort(key = lambda pair: pair[1], reverse=True)
print(objects)


""" Some very boring / interesting matrix calculi """

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# Transpose with comprehentions:
print([ [row[i] for row in matrix] for i in range(len(matrix[0])) ])

# Transpose 2, using zip, whattafuck!!! Amazing:
print(list(zip(*matrix)))