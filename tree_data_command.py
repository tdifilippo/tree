"""
    tree_data.py
    
    usage:
       Usage: tree_data.py 
        
    Notes:
        This version was developed without any specific libraries, as requested in the 
        Candidate Evaluation Assignment document.
        To that end, I have limited command line arguments to a single optional FILE, 
            
            python tree_data.py [FILE]
        
"""

import sys   
import os


class node():
    def __init__(self, parent_name, node_name, parent):
        """
            Data structure to hold a tree node, which includes:
                parent_name: Name of parent node
                node_name:Name of this node
                parent_link: Link to parent node
        """
        # Get node_name, parent_name and parent's link
        self.node_name = node_name
        self.parent_name = parent_name
        self.parent = parent
        # If the parent is None, this is the root node, so indent is 0
        if parent == None:
            self.indent = 0
        # else: indent=parent indent + 1
        else:
            self.indent = parent.indent + 1
        # Initialize the next link to None
        self.next = None
        
    def show(self):
        """ show the NODE as parent|node_name """
        print ('    NODE: {}|{}'.format(self.parent_name,self.node_name))
        
    def debug(self):
        """ debug the NODE with additional info """
        print ('[{}|{}|{}|{}]'.format(self.node_name,self.parent_name,self.indent,self.next))

class tree():
    def __init__(self, file_name):
        """
            Save the tree file_name and init root, last nodes
        """
        self.file_name = file_name
        self.root = None
        self.last = None
        
    def find_node(self, text):
        """
            find node or nodes which have text as the node_name
        """
        nodes=[]
        node = self.root
        while node:
            if text == node.node_name:
                nodes.append(node)
            # Point node to next one
            node = node.next
        return nodes

    def find_parents(self, text):
        """
            find one or more parents with text name as parent
        """
        nodes = []
        node = self.root
        while node:
            if text == node.parent_name:
                nodes.append(node)
            # Point node to next one
            node = node.next
        return nodes

    def find_parent(self, text):
        """
            find a nodes parent name
        """
        node = self.root
        while node:
            if text == node.node_name:
                return node
            # Point node to next one
            node = node.next
        return None

    def isnotparent(self, node):
        # look at all children of node
        test_node = node.next
        while test_node:
            # See whether node is test_node's parent
            if test_node.parent == node:
                # Return False, node test_node is a parent
                return False
            # link to next test_node
            test_node = test_node.next
        return True
            
    def get_leaves(self):
        """
            find leaves (a node without children)
            search in self.last ->link
        """
        nodes=[]
        node = self.root.next
        while node:
            # See whether this node is NOT a parent
            if self.isnotparent(node):
                nodes.append(node)
            # link to next node
            node = node.next
        return nodes
        
    def lowest_indent(self):
        """
            get the lowest nodes
        """
        indent = 0
        # Start at root
        node = self.root
        while node:
            # If the indent is higher, set to it
            if node.indent > indent:
                indent = node.indent
            # Go to next node
            node=node.next
        return indent
        
    def get_lowest(self):
        """
            get the lowest nodes, based on the indent
        """
        lowest_indent = self.lowest_indent()
        nodes = []
        node = self.root
        # Iterate from root through last node
        while node:
            if lowest_indent == node.indent:
                nodes.append(node)
            # Point node to next one
            node = node.next
        return nodes

    def input_tree(self):
        """
            Read in the input tree, each is two fields, the parent and child 
        """
        index = 0
        # read file_name and parse line by line
        with open(self.file_name) as filep:
            lines = filep.readlines()
        # Iterate each line
        for line in lines:
            # Split up each line, strip the parent_name and node_name
            txt=line.split('|')
            parent_name = txt[0].strip()
            node_name = txt[1].strip()
            # Create a root node
            if index == 0:
                # Create root: node(parent_name, node_name, parent)
                self.root = node(parent_name, node_name, None)
                self.last = self.root
            else:
                # Find this parent
                parent = self.find_parent(parent_name)
                # Create new_node: node(parent_name, node_name, parent)
                new_node = node(parent_name, node_name, parent)
                self.last.next = new_node
                self.last = new_node
            index = index + 1
                
    def find(self, name):
        """
            find all 'name' nodes
        """
        ret=[]
        # Start at root
        node = self.root
        while node:
            # If the name is what we are looking for, add to ret
            if name == node.node_name:
                ret.append(node)
            # Go to next node
            node=node.next
        return ret
        
    def print_tree(self):
        print ('*********************************')
        print ('    DISPLAY TREE')
        # Start at root
        node = self.root
        while node:
            # initialize ind to ''
            ind = ''
            for x in range(node.indent):
                ind += '-'
            print ('{}{}'.format(ind,node.node_name))
            # Go to next node
            node=node.next
        print ('*********************************')

def print_nodes(nodes, str):
    """
        print the nodes in the class node
    """
    print ('*********************************')
    print ('    {}    '.format(str))
    if nodes:
        for node in nodes:
            node.show()
    else:
        print ('NONE')

def usage():
    print ('Usage: %s [-h] [-f FILE]'%sys.argv[0])
    print ('           -h       Show this message, and exit')
    print ('           -f FILE  Set the file to FILE')
    print ('\n')
    sys.exit(0)
    
def command_line_arguments():
    """
        handle command_line_arguments, return filename
        
        NOTE:
            This should / would use argparse, however to insure it's use under all versions
            of Pythons
    """
    # Check for a single optional argument, assuming that argparse may not be available
    if len(sys.argv) > 1:
        # Check for: -h, -f FILE 
        if sys.argv[1] == '-h':
            usage()
        elif sys.argv[1] == '-f' and len(sys.argv) == 3:
            filename = sys.argv[2]
        else:
            usage()
    else:
        filename = 'data.txt'
    return filename
    

def main ():
    """
        main function for tree_data.py
    """
    # Process command line arguments and startup
    filename = command_line_arguments()
    # Check that it's a valid file
    if not os.path.isfile(filename):
        print ('File {%s} is not valid',Filename)
        sys.exit(0)

    # Create the tree and input from filename into tree_struct
    tree_structure = tree(filename)
    tree_structure.input_tree()
    # Mode is 0 for abreviation, 1 for verbose
    mode = 2
    while mode != 'E':
        if mode == '?':
            print ('Enter from the following commands')
            print ('    0: Select input mode 0, abbreviation')
            print ('    ?: Select input mode ?, verbose')
            print ('    T: Display the Tree')
            print ('    L: Display the Leaves')
            print ('    N: Show lowest Nodes')
            print ('    F: Find node by Name')
            print ('    P: Find nodes by Parent Name')
            print ('    E: Exit the program')
        # Read the input
        input = raw_input('Enter Mode [0,?] or command [T,L,N,F,P] or Exit--> ')
        if input >= 'a' and input <= 'z':
            input=input.upper()
        if input == '?':
            mode = '?'
        elif input == '0':
            mode = '0'
        elif input == 'T':
            # print_tree
            tree_structure.print_tree()
        elif input == 'L':
            # Retreive all leaves, the nodes which have no children
            nodes = tree_structure.get_leaves()
            print_nodes(nodes, 'GET_LEAVES')
        elif input == 'N':
            # Retreive the nodes that sit at the lowest level
            nodes = tree_structure.get_lowest()
            print_nodes(nodes, 'GET_LOWEST')
        elif input == 'F':
            nodename=raw_input('Enter node to find --> ')
            nodes = tree_structure.find_node(nodename)
            print_nodes(nodes, 'FIND_NODE')
        elif input == 'P':
            parentname=raw_input('Enter parent to find --> ')
            nodes = tree_structure.find_parents(parentname)
            print_nodes(nodes, 'FIND_PARENT')
        elif input == 'E':
            sys.exit(0)
    
    
if __name__ == '__main__':
    main()
