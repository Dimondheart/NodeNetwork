from __future__ import print_function


SEPARATOR = "----------"


class FullNodeGrid(Exception):
    ''' Exception raised when attempting to add a node to a full node grid. '''
    def __init__(self):
        pass
        
    def __str__(self):
        return "Cannot add a node to a full node grid."
        
        
class UnknownNodeCreator(Exception):
    ''' Raised when a object type not specified as a node creator attempts
    to create a new Node.
    '''
    
    def __init__(self, obj_type):
        self.creator = obj_type
    
    def __str__(self):
        return "Type '{}' is not identified as a valid node creator.".format(
            self.creator
            )


class PathfinderIterator2D(object):
    ''' An iterable object used to iterate over a 2d grid for simple
    pathfinding.
    '''
    def __init__(self):
        pass
        
        
class NodeNetwork(object):
    ''' Handles a collection of nodes in a grid. '''
    # TODO: Make new nodes more likely to make new connections
    # The grid of nodes
    node_grid = []
    # An initial node created as a stem for other nodes
    main_root_node = None
    
    def __init__(self, d1=5, d2=5):
        ''' Initialize stuff like the node grid. '''
        self.node_grid = [[None for b in xrange(0,d2)] for a in xrange(0,d1)]
        # Create a root node at the center of the grid
        center_d1 = (d1-1) / 2
        center_d2 = (d2-1) / 2
        self.main_root_node = Node(self)
        self.node_grid[center_d1][center_d2] = self.main_root_node
        
    def __iter__(self):
        ''' Iterate over the nodes in this node network. '''
        for d1 in self.node_grid:
            for d2 in d1:
                yield d2
        
    def add_node(self, root_node, new_node):
        '''Adds a new node as close as possible to the root node. '''
        # Stub, this only adds it to the first open spot
        # TODO: Implement pathfinding algorithm for this
        for x in xrange(len(self.node_grid)):
            for y in xrange(len(self.node_grid[0])):
                # if this space is free, add the node and return
                if self.node_grid[x][y] is None:
                    self.node_grid[x][y] = new_node
                    return
        # No empty node found, raise exception
        raise FullNodeGrid(self)
    
    def display_network_text(self):
        num_columns = len(self.node_grid[0])
        curr_col = 1
        for node in self:
            if curr_col > num_columns:
                print('\n', sep='', end='')
                curr_col = 1
            print_char = '?'
            if node is None:
                print_char = 'O'
            elif isinstance(node, Node):
                print_char = 'X'
            print(print_char, sep='', end=' ')
            curr_col += 1
        print('\n', end='')
         
               
class InvalidNodeCreator(object):
    ''' Just used to test the UnknownNodeCreator exception. '''
    
    def __init__(self):
        pass
        
    def cbn(self):

        badnode = Node(self)
        
                      
class Node(object):
    ''' A single node in a node network. '''
    # Other nodes this node is connected to
    connections = []
    my_net = None
    
    def __init__(self, creator):
        ''' Initialize this node.
        One initalize operation is to add creating node as a connected node.
        '''
        # Normal new node initializing
        if isinstance(creator, Node):
            # What network this node is part of
            self.my_net = getattr(creator, "my_net")
            # Add the parent node as a connected node
            self.connections.append(creator)
        # NodeNetwork main root node initializing
        elif isinstance(creator, NodeNetwork):
            self.my_net = creator
        # Unknown node creator, raise exception
        else:
            raise UnknownNodeCreator(type(creator))
        
    def create_node(self):
        ''' Create a new node off of this one. '''
        new_node = Node(self)
        self.my_net.add_node(self, new_node)
        self.connections.append(new_node)
        
    
nodenet = NodeNetwork(9,9)


def update():
    print(SEPARATOR)
    nodenet.display_network_text()
    print(SEPARATOR)