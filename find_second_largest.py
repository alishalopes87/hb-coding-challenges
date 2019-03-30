def find_largest(root_node):

    current = root_node

    #Find the largest node by traversing down the tree

    while current:
        if not current.right: #If there is no more right node
            return current.value #Return the current node's value

            current = current.right #Move down the tree one step to the right

def find_second_largest(root_node):

    #check if there is a root root_node

    if(root_node is None or 
        (root_node.left is None anf root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

        current - root_node

        #Traverse down Tree

        while current:

            #case 1: current is largest and has a left subtree
            # 2nd largest is the the largest in that subtree

            if current.left and not current.right: #If there is a left subtree
                return find_largest(current.left)

            #Case 2: current is parent of largest, and largest has no children
            #so current is 2nd largest
            if(current.right and                   #If there is a right child
                    not current.right.left and     #If the child has no left
                    not current.right.right):      #If the child has no right
                return current.value 


                current = current.right