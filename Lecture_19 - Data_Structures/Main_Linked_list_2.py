class Node:
    index = 0
    def __init__(self, data):
        self.data = data                
        self.next = None
        self.index = Node.index
        Node.index += 1

    @staticmethod    
    def append(head):
        tmp = head
        while True:
            data = input("Enter data: ")
            if data.upper() == "EXIT":
                break
            else:
                tmp.next = Node(data)
                tmp = tmp.next

    @staticmethod
    def Insert(head, index, data):
        tmp = head
        print(tmp)
        while (tmp is not None) and (tmp.index != index):
            tmp = tmp.next

        if tmp is None:
            raise Exception("Index out of range")
        else:
            tmp0 = tmp.next
            index0 = tmp.index

            tmp.next = Node(data)
            tmp.next.index = index0 + 1            
            tmp.next.next = tmp0
            tmp0.index = index0 + 2

            while tmp0.next is not None:
                tmp0.next.index = tmp0.index + 1
                tmp0 = tmp0.next

    @staticmethod
    def dispaly(node):        
        while node is not None:
            print(f"({node.data}-{node.index})", end= "->")
            node = node.next
        print("end of list")

    def __str__(self):
        return(f"data={self.data}; index={self.index}")


head = Node("Head_Node")

Node.append(head)

Node.dispaly(head)

Node.Insert(head, 1, "dbb")

Node.dispaly(head)