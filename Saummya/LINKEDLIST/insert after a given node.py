def insertAfter(self, prev_node, new_data):
 
    # 1. check if the given prev_node exists
    if prev_node is None:
        print "The given previous node must inLinkedList."
        return
 
    # 2. Create new node &
    # 3. Put in the data
    new_node = Node(new_data)
 
    # 4. Make next of new Node as next of prev_node
    new_node.next = prev_node.next
 
    # 5. make next of prev_node as new_node
    prev_node.next = new_node
