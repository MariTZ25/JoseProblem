class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.prev= None
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        current.next = new_node
        self.head = new_node
    def display(self):
        if self.head is None:
            print("Empty list")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(back to head)")
    def traverse(self):
        conteo=1
        current = self.head
        while current.next!=self.head:
            conteo=conteo+1
            current = current.next
        return conteo
    def elimin(self, k):
            cantidad=self.traverse()
            conteo=0
            current=self.head
            while(current.next != current):
                while (cantidad<=k and k<0):
                  k=k-1
                while(conteo<k):
                    current=current.next
                    conteo=conteo+1
                    self.head=current
                current.next=None
                cantidad= cantidad-1
                conteo=0
                
    

