class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None
    
    def set_next_node(self, node):
        self.next_node = node

    def set_prev_node(self, node):
        self.prev_node = node

    def get_prev_node(self):
        return self.prev_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

class LinkedList:

    def __init__(self, size = 0):
        self.size = size
        self.head = None
        self.tail = None

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head

    def create_head(self, new_head):
        if self.head == None:
            self.head = new_head
            self.tail = new_head
            self.head.set_prev_node(self.tail)
            self.tail.set_next_node(self.head)
            self.size+=1
        elif self.head != None:
            prev_head = self.head
            self.head.set_prev_node(new_head)
            new_head.set_next_node(prev_head)
            new_head.set_prev_node(self.tail)
            self.head = new_head
            self.tail.set_next_node(self.head)
            self.size+=1

    def add_to_head(self, node):
        if self.head != None and (self.head.get_next_node() != None):
            new_next_node = self.head.get_next_node()
            new_next_node.set_prev_node(node)
            self.head.set_next_node(node)
            node.set_next_node(new_next_node)
            node.set_prev_node(self.head)
            self.size+=1
        else:
            self.add_to_tail(node)
            self.size+=1

    def add_to_tail(self, tail_node):
        if self.head == self.tail:
            self.head.set_next_node(tail_node)
            self.head.set_prev_node(tail_node)
            self.tail = tail_node
            self.tail.set_prev_node(self.head)
            self.tail.set_next_node(self.head)
            self.size+=1
        else:
            curr_node = self.head
            while curr_node != self.tail:
                curr_node = curr_node.get_next_node()
            curr_node.set_next_node(tail_node)
            self.tail = tail_node
            self.tail.set_prev_node(curr_node)
            self.tail.set_next_node(self.head)
            self.head.set_prev_node(self.tail)
            self.size+=1    

    def insert(self, node, position):
        curr_position = 0
        curr_node = self.head
        if position <= self.size:
            while (curr_node != self.tail) and (curr_position != position):
                curr_node = curr_node.get_next_node()
                curr_position+=1
            
            if curr_position == 0:
                self.create_head(node)
            elif curr_position == 1:
                self.add_to_head(node)
            elif curr_position == (self.size - 1):
                self.add_to_tail(node)
            elif curr_position > 0:
                prev_node = curr_node
                prev_node_prev_node = prev_node.get_prev_node()
                curr_node.get_prev_node().set_next_node(node)
                curr_node.set_prev_node(node)
                node.set_prev_node(prev_node_prev_node)
                node.set_next_node(prev_node)
                self.size+=1

        elif position > self.get_size():
             print('Cannot place ' + str(node.get_value()) + ' at position ' + str(position))

    def remove(self, target):
        curr_node = self.head
        while curr_node != self.tail:
            if target == curr_node.get_value():
                if curr_node == self.head:
                    self.head = self.head.get_next_node()
                    self.head.set_prev_node(self.tail)
                    self.tail.set_next_node(self.head)
                    self.size-=1
                    break
                else:
                    next_node = curr_node.get_next_node()
                    prev_node = curr_node.get_prev_node()
                    curr_node.get_prev_node().set_next_node(next_node)
                    curr_node.get_next_node().set_prev_node(prev_node)
                    self.size-=1
                    break
            curr_node = curr_node.get_next_node()
        if curr_node == self.tail and curr_node.get_value() == target and curr_node.get_next_node() != curr_node:
            self.tail = self.tail.get_prev_node()
            self.tail.set_next_node(self.head)
            self.head.set_prev_node(self.tail)
            self.size-=1
        elif curr_node == self.tail and curr_node.get_value() == target and curr_node.get_next_node() == curr_node:
            self.tail = None
            self.head = None
            self.size = 0



    def display(self):
        curr_node = self.head
        if self.size > 0:
            while curr_node != self.tail:
                print(curr_node.get_value())
                curr_node = curr_node.get_next_node()
            print(self.tail.get_value())
        else:
            print("------EMPTY LIST------")

    def display_backward(self):
        curr_node = self.tail
        while curr_node != self.head:
            print(curr_node.get_value())
            curr_node = curr_node.get_prev_node()
        print(self.head.get_value())

#---------------------------------------------------------------------
new_list = LinkedList()
count = 0

while True:
    if count == 0:
        node_value = input('What value is your head node? ')
        head_node = Node(node_value)
        new_list.create_head(head_node)
        count+=1
        new_list.display()
        print()
    elif count > 0:
        option = input('Type H to add new head node \nType I to insert new node \nType T to add to the tail \nPress AH to add to head \nPress R to remove \nPress B to print backwarads \nPress E to exit \n')
        if option == 'H':
            node_value = input('What value is your head node? ')
            head_node = Node(node_value)
            new_list.create_head(head_node)
            count+=1
            print('List: ')
            new_list.display()
            print()
        elif option == 'I':
            node_value = input('What value is your node? ')
            curr_node = Node(node_value)
            position = int(input('What position do you want to put your node? '))
            while int(position) > new_list.get_size():
                position = int(input('Cannot place in that position. What position do you want to put your node? '))
            new_list.insert(curr_node, position)
            print('List: ')
            new_list.display()
            print()
        elif option == 'T':
            node_value = input('What value is your node? ')
            curr_node = Node(node_value)
            new_list.add_to_tail(curr_node)
            print('List: ')
            new_list.display()
            print()       
        elif option == 'AH':
            node_value = input('What value is your node? ')
            curr_node = Node(node_value)
            new_list.add_to_head(curr_node)
            print('List: ')
            new_list.display()
            print()
        elif option == 'E':
            print()
            print()
            print('List: ')
            new_list.display()
            break
        elif option == 'B':
            print()
            new_list.display_backward()
            print()
        elif option == 'R':
            print()
            remove = input('What node do you want to remove? ')
            new_list.remove(remove)
            new_list.display()


if new_list.size > 0:
    print('\nHead node: ')  
    print(str(new_list.head.get_value()))

    print('Head node previous pointer: ')
    print(str(new_list.head.get_prev_node().get_value()))

    print('Tail node: ')
    print(str(new_list.tail.get_value()))

    print('Tail node next pointer: ')
    print(str(new_list.tail.get_next_node().get_value()))
    print('List size: ')
    print(str(new_list.get_size()))
else: print('------LIST IS EMPTY------')