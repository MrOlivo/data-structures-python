class Arbol():
    def __init__(self, dato = None):
        self.dato = dato
        self.left = None
        self.right = None
        
    def insert(self, valor):
        if self.dato == None:
            self.dato = valor
        elif valor <= self.dato:
            if self.left == None:
                self.left = Arbol(valor)
            else:
                self.left.insert(valor)
        else:
            if self.right == None:
                self.right = Arbol(valor)
            else:
                self.right.insert(valor)

    def inorder(self):
        if not (self.left == None): self.left.inorder()
        print(self.dato, end=" ")
        if not (self.right == None): self.right.inorder()

    def preorder(self):
        print(self.dato, end=" ")
        if not (self.left == None): self.left.preorder()
        if not (self.right == None): self.right.preorder()

    def postorder(self):
        if not (self.left == None): self.left.postorder()
        if not (self.right == None): self.right.postorder()
        print(self.dato, end=" ")

