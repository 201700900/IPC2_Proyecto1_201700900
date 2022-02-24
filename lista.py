class Node:
    def __init__(self, Value):
        self.Value = Value
        self.Next = None

    def __str__(self):
        return str(self.Value)

    def __repr__(self):
        return self.Value
    
    def __iter__(self):
         return self.Value

class LinkedList: 
    
    def __init__(self):
        self.First = None
        self.Size = 0

    def __iter__(self):
        node = self.First
        while node is not None:
            yield node.Value
            node = node.Next

    def __repr__(self):
        node = self.First
        nodes = []
        while node is not None:
            nodes.append(node.Value)
            node = node.Next
        nodes.append("None")
        return " -> ".join(nodes) 
       
    def __len__(self):
        return self.Size

    def __str__(self):
        String = "["
        Current = self.First
        for i in range(len(self)):
            String += str(Current)
            if i != len(self) - 1:
                 String += str(", ")
            Current = Current.Next
        String += "]"
        
        return String
    
    def __setitem__(self, indice, dato):
        if indice >= 0 and indice < self.Size:
            actual = self.First

            for _ in range(indice):
                actual = actual.Next
            
            actual.Value = dato
        else:
            return False
            #raise Exception('Índice no válido. Está por fuera del rango.')

   
    def __getitem__(self, index):
        if index >= 0 and index < self.Size:
            actual = self.First
            for i in range(index):
                actual = actual.Next
            return actual.Value
        else:
            return False
            #raise Exception('Índice no válido. Está por fuera del rango.')

    def Append(self, Value): 
        MyNode = Node(Value)
        if self.Size == 0:
            self.First = MyNode
        
        else:
            Current = self.First
            while Current. Next != None:
                 Current = Current.Next
            Current.Next = MyNode
        self.Size += 1
        
        return MyNode
    
    def Remove(self, Value):
        if self.Size == 0:
            return False
        
        else:
            Current = self.First
            try:
                 while Current.Next.Value != Value:
                     Current = Current.Next
                 DeletedNode = Current.Next
                 Current.Next = DeletedNode.Next
            
            except AttributeError:
                 return False
        
        self.Size -= 1
        return DeletedNode

    def Buscar(self, Value):
        if self.Size == 0:
            return False
        else:
            Current = self.First
            try:
                 while Current.Next.Value != Value:
                     Current = Current.Next
                 return Current.Next
            except AttributeError:
                 return False

        
        
        

    def bubbsort(self):
        for i in range(self.Size-1):#for controlli
            Current = self.First
            nxt=Current.Next
            prev = None
        while nxt:#Comparisons in passes
            if Current.Value > nxt.Value:
                if prev == None:
                    prev = Current.Next
                    nxt = nxt.Next
                    prev.Next = Current
                    Current.Value = nxt
                    self.First = prev
                else:
                    temp = nxt
                    nxt = nxt.Next
                    prev.Next = Current.Next
                    prev = temp
                    temp.link = Current
                    Current.Next = nxt
            else:
            
                prev = Current
                Current = nxt
                nxt = nxt.Next
        i += 1

# x=0
# y=0
# c = LinkedList()
# f = LinkedList()
# c.Append('1')
# c.Append('2')
# c.Append('3')
# c.Append('4')
# f.Append(c)
# c = LinkedList()
# c.Append('5')
# c.Append('6')
# c.Append('7')
# c.Append('8')
# f.Append(c)
# print(f)
# print(f[0][0])
# f[0][0] = 'W'
# print(f[0][0])
# print(f)
# print(f)
# print(f[x][y])
# print(f[x][y])
# f[x+1][y+1] = 'A'
# f[x+1][y+2] = 'B'
# f[0][0]='Z'
# print(f)

