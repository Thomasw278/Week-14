class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data, self)
            else:
                self.left.insert(data)
        elif data >= self.data:
            if self.right is None:
                self.right = Node(data, self)
            else:
                self.right.insert(data)
        else:
            return False
        return True

    def operator(self):
        return self.data
    
    def left(self):
        return self.left
    
    def right(self):
        return self.right
    
    def parent(self):
        return self.parent
    
    def is_leaf(self):
        return self.right == None and self.left == None
    
    def is_parent(self):
        return self.parent == None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def add(self, data):
        if self.root is None:
            self.root = Node(data, None)
            self.size += 1
        else:
            if self.root.insert(data):
                self.size += 1

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    
    def get_root(self):
        return self.root

    def plus_minus(self):
    #Cara 1
        def helper(node):
            if node is None:
                return 0
            left_sum = helper(node.left)
            right_sum = helper(node.right)
            if node.data % 2 == 0:
                return left_sum + right_sum + node.data
            else:
                return left_sum + right_sum - node.data

        return helper(self.root)
    # #Cara 2
        hasil = 0
        liststack = [self.root]
        semuadata = list()
        while len(liststack) != 0:
            data1 = liststack.pop()
            if data1.right is not None:
                liststack.append(data1.right)
            if data1.left is not None:
                liststack.append(data1.left)
            semuadata.append(data1.data)
        for i in semuadata:
            if i % 2 == 1:
                hasil -= i
            else:
                hasil += i
        return (f"Hasil Plus Minus\n>> {hasil}\n")
    #Cara 3
        total = 0
        simpan = []
        hasil = self.root
        while hasil is not None or simpan:
            while hasil is not None:
                simpan.append(hasil)
                hasil = hasil.left
            hasil = simpan.pop()
            if hasil.data % 2 == 0:
                total += hasil.data
            else:
                total -= hasil.data
            hasil = hasil.right
        return (f"Jadi Hasil Plus Minus adalah {total}")
                        
    #Cara 4
        total = 0
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            current = nodes_to_visit.pop()
            if current:
                if current.data % 2 == 0:
                    total += current.data
                else:
                    total -= current.data

                # Tambahkan anak kiri dan kanan ke list untuk dikunjungi
                if current.left:
                    nodes_to_visit.append(current.left)
                if current.right:
                    nodes_to_visit.append(current.right)

        return f"Hasil dari Fungsi Plus Minus Adalah {total}"




if __name__ == '__main__':
    binaryT = BinaryTree()
    binaryT.add(5)
    binaryT.add(4)
    binaryT.add(3)
    binaryT.add(9)
    binaryT.add(8)
    binaryT.add(6)
    binaryT.add(7)
    binaryT.add(11)
    binaryT.add(10)
    print()
    print(binaryT.plus_minus())