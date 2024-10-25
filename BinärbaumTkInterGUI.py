import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class Node:
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        # Links-Links-Fall
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        # Rechts-Rechts-Fall
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        # Links-Rechts-Fall
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Rechts-Links-Fall
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        res = []
        if root:
            res.append(root.key)
            res = res + self.preOrder(root.left)
            res = res + self.preOrder(root.right)
        return res

    def inOrder(self, root):
        res = []
        if root:
            res = self.inOrder(root.left)
            res.append(root.key)
            res = res + self.inOrder(root.right)
        return res

    def postOrder(self, root):
        res = []
        if root:
            res = self.postOrder(root.left)
            res = res + self.postOrder(root.right)
            res.append(root.key)
        return res

    def levelOrder(self, root):
        res = []
        if not root:
            return res
        queue = []
        queue.append(root)
        while queue:
            temp = queue.pop(0)
            res.append(temp.key)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return res
    
class AVLApp:
    def __init__(self, root):
        self.tree = AVLTree()
        self.root_node = None
        self.root = root
        self.root.title("AVL Baum Visualizer")
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.entry = tk.Entry(self.frame)
        self.entry.grid(row=0, column=0)
        self.addButton = tk.Button(self.frame, text="Hinzufügen", command=self.add)
        self.addButton.grid(row=0, column=1)
        self.preOrderButton = tk.Button(self.frame, text="Preorder Traversal", command=lambda: self.traverse('pre'))
        self.preOrderButton.grid(row=1, column=0)
        self.inOrderButton = tk.Button(self.frame, text="Inorder Traversal", command=lambda: self.traverse('in'))
        self.inOrderButton.grid(row=1, column=1)
        self.postOrderButton = tk.Button(self.frame, text="Postorder Traversal", command=lambda: self.traverse('post'))
        self.postOrderButton.grid(row=2, column=0)
        self.levelOrderButton = tk.Button(self.frame, text="Levelorder Traversal", command=lambda: self.traverse('level'))
        self.levelOrderButton.grid(row=2, column=1)
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()
        
        self.bg_image = Image.open("tree_background.jpg")  # Lade dein Bild
        self.bg_image = self.bg_image.resize((600, 400), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor=tk.NW)

    def add(self):
        try:
            key = int(self.entry.get())
            self.root_node = self.tree.insert(self.root_node, key)
            self.entry.delete(0, tk.END)
            self.draw_tree()
        except ValueError:
            messagebox.showerror("Ungültige Eingabe", "Bitte eine gültige ganze Zahl eingeben.")

    def draw_tree(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor=tk.NW)
        if self.root_node:
            self._draw_node(self.root_node, 300, 30, 150)

    def _draw_node(self, node, x, y, dx):
        if node.left:
            self.canvas.create_line(x, y, x - dx, y + 60)
            self._draw_node(node.left, x - dx, y + 60, dx // 2)
        if node.right:
            self.canvas.create_line(x, y, x + dx, y + 60)
            self._draw_node(node.right, x + dx, y + 60, dx // 2)
        self.canvas.create_oval(x-15, y-15, x+15, y+15, fill='lightgreen')
        self.canvas.create_text(x, y, text=str(node.key))

    def traverse(self, method):
        if not self.root_node:
            messagebox.showerror("Fehler", "Der Baum ist leer!")
            return
        if method == 'pre':
            traversal = self.tree.preOrder(self.root_node)
            description = "Preorder Traversal (Root -> Links -> Rechts):"
        elif method == 'in':
            traversal = self.tree.inOrder(self.root_node)
            description = "Inorder Traversal (Links -> Root -> Rechts):"
        elif method == 'post':
            traversal = self.tree.postOrder(self.root_node)
            description = "Postorder Traversal (Links -> Rechts -> Root):"
        elif method == 'level':
            traversal = self.tree.levelOrder(self.root_node)
            description = "Levelorder Traversal (Ebene für Ebene):"
        messagebox.showinfo("Traversal Ergebnis", f"{description}\n{traversal}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AVLApp(root)
    root.mainloop()
