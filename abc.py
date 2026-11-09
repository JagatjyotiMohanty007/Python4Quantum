class Node:
    def __int__(self):
        self.data = self.data
        self.next= Node


class LinkedList:
    def __int__(self):
            self.head = Node

    def append(self, data):
         new_node = Node(data)

        if self.head is None:
         self.head = new_node
         return

        current = self.head

        while current.next:
          current = current.next

        current.next= new_node
    def find_nth_node(self, n):
         first = self.head
         second = self.head
        for _in range(n):
         if first is None:
            return None
        first = first.next
    
    while first is not None:
        first = first.next
        second= second.next
    
    return second.data if second else None

        #  current = self.head
        #  count =1

        #  while current:
        #       if count == n
        #         return current.data

        #     current = current.next
        #     count += 1
        # return None

def disply(self):
    current = self.head
    while current:
      print(current.data,end=" ->")
      current = current.next
    print("None")
    
head = Node(1)  
head.next = Node(1)  
head.next.next = Node(2)  
head.next.next.next = Node(3)  
head.next.next.next.next = Node(4)
head.next.next.next.next = Node(5) 
# l1 = LinkedList() 
# l1.append(10)
# l1.append(20)
# l1.append(30)
# l1.append(40)
# l1.append(50)

print("Linked List:")
#l1.disply()

n = int(input("Enter node position to search"))

result = l1.find_nth_node(n)

if result is not None:
    print(f"Node at postion {n} is" : {result}
else
    print("Node position is not found"}          

            
    