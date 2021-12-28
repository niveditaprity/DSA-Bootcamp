def push(self, new_data):
 
    #        Put in the data
    new_node = Node(new_data)
         
    # 3. Make next of new Node as head
    new_node.next = self.head
         
    # 4. Move the head to point to new Node
    self.head = new_node
