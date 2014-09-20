

class Graph:
   def __init__(self):
      self._v = []

   def add_node(self, node):
      self._v.append(node)

   def __str__(self):
      return "Vertices: {}\nEdges   : {}".format(self._v, self._e)

   def __repr__(self):
      return "ugue"

   def pretty_print(self):
      print("Vertices: ", self._v)
      for v in self._v:
         if not v.isleaf():
            print(v, ": ", v.edges())


class Node:
   def __init__(self, identifier, **kwargs):
      self._id = identifier
      self.__dict__.update(kwargs)
      self._edges = []

   def __str__(self):
      return "{} ({})".format(self._id, self.isleaf() and "L" or "I")

   def __repr__(self):
      return str(self)

   def __hash__(self):
        return hash(self._id)

   def __eq__(self, other):
        return self._id == other._id

   def add_edge(self, other, label):
      if (other, label) not in self._edges:
         self._edges.append( (other, label) )  

   def remove_edge(self, target):
      self._edges = [ (node, label) for (node, label) in self._edges if node != target]

   def isleaf(self): return not bool(self._edges)

   def edges(self):
      return self._edges

   def edge_starting_with(self, start_letter):
      for (node, label) in self._edges:
               if label.startswith(start_letter):
                  return (node, label)

      return (None, None)

class ST:
   def __init__(self, t):
      self.text = t
      self.graph = Graph()
      self._build()

   def _max_common_prefix(self, x, y):
         i = 0
         for cx, cy in zip(x, y):
            if(cx == cy):
               i += 1

         return i

   def _build(self):    
      graph = self.graph
      root = Node("root")
      graph.add_node(root)

      for i, c in enumerate(self.text):
         foglia = Node(i)
         graph.add_node(foglia)
         x = self.text[i:]
         v = root
         out = 0

         while out == 0:
            # Trovo un arco che incominci con la prima lettera del suffisso
            u, y = v.edge_starting_with(x[0])            

            if u:
               max_common = self._max_common_prefix(x, y)
               gamma = y[max_common:]  # y = alpha+gamma
               beta = x[max_common:]   # x = alpha+beta

               # y e' esaurito? Allora il prefisso x raggiunge un prossimo
               # nodo interno, la ricerca deve continuare da li
               # Ma non dobbiamo continuare a cercare per x, ma solo per
               # la sua porzione finale, che non abbiamo ancora esaurito,
               # cioè beta
               if not gamma: 
                  v = u
                  x = beta

               # Invece qua y non e' esaurito, e significa che il pattern x
               # finisce in qualche punto a metà della label che va dal nodo
               # corrente v al nodo y
               # Dobbiamo spezzare una tale label, aggiungere un nuovo nodo
               # a sua metà, e ripartire l'algoritmo da questo nuovo
               # nodo, però con out = 1. In questo modo si creerà il collegamento
               # con il nodo foglia corrispondente
               else:
                  # Creo un nuovo nodo z e lo aggiungo al grafo
                  z = Node("interno_"+str(i)) # Metto la i per identificare i nodi interni
                  graph.add_node(z)   

                  # Spezzo la label esistente, mettendo z in mezzo    
                  v.remove_edge(u)
                  v.add_edge(z, x[:max_common])
                  z.add_edge(u, gamma)

                  # Definisco nuove impostanzioni di esecuzione per i cicli
                  v = z
                  x = beta
                  out = 1
            else:
               out = 1

         v.add_edge(foglia, x)

      graph.pretty_print()

st = ST("xabxac$")

st = ST("abab$")
