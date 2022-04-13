class Arbol():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, valor):
        if self.data == None:
            self.data = valor
        elif valor <= self.data:
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
        if not (self.left == None):
            self.left.inorder()
        print(self.data, end=" ")
        if not (self.right == None):
            self.right.inorder()

    def preorder(self):
        print(self.data, end=" ")
        if not (self.left == None):
            self.left.preorder()
        if not (self.right == None):
            self.right.preorder()

    def postorder(self):
        if not (self.left == None):
            self.left.postorder()
        if not (self.right == None):
            self.right.postorder()
        print(self.data, end=" ")
