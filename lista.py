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
# print(len(f))
# for y in range(0, len(f)):
#     print("y = "+str(y))
#     print("len = "+str(len(f[y])))
#     for x in range(0, len(f[y])):
#         print("x = "+str(x))