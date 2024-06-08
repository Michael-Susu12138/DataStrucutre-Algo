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
            return None
        elif self.length == 1:
            return self.pop()
        else:
            cur = self.head 
            next_node = self.head.next
            cur.next = None
            self.head = next_node
            return cur 
    
    def get(self,index):
        # 0 -> 1 -> 2 -> 3
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self,value,index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index >= self.length:
            return False
        if index == 0: return self.prepend(value)
        if index == self.length: return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        skip = temp.next
        temp.next = new_node
        new_node.next = skip
        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0: 
            return self.pop_first()     
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get(index-1)
            target = temp.next
            temp.next = target.next
            target.next = None
            self.length -= 1
            return target
    def reverse(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return self.head
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return self.head
            
        
    
        


# TEST CODE
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.print_list()

new_head = ll.reverse()
while new_head.next:
    print(new_head.value)
    new_head = new_head.next
print(new_head.value)