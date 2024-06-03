class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, " -> ", end="")
            temp = temp.next
        print()
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:   
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
            
    def pop(self):
        slow = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return slow
        fast = slow.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = None
        self.tail = slow
        self.length -= 1
        return fast
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            cur = self.head
            new_node.next = cur
            self.head = new_node
            self.length += 1
        return True
    
    
    def pop_first(self):
        if self.length == 0:
            
        cur = self.head 
        next_node = self.head.next
        cur.next = None
        self.head = next_node
        return cur 
            
        


# TEST CODE
ll = LinkedList(1)
ll.pop()
ll.prepend(0)

ll.print_list()