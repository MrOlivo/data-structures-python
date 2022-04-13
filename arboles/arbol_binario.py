class BinaryTree():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if self.data == None:
            self.data = value
        elif value <= self.data:
            if self.left == None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)

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
