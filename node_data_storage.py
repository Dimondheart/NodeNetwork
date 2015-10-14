class FullNodeGrid(Exception):
    ''' Exception raised when attempting to add a node to a full node grid. '''
    def __init__(self, ng = None):
        ''' ng: Specify the the full node grid normally. '''
        self.ngf = ng
        
    def __str__(self):
        if self.ngf is None:
            return "Cannot add a node to a full node grid."
        else:
            return "Cannot add a node to full node grid '{}'.".format(self.ngf)


class NodeNetwork(object):
    ''' Handles a collection of nodes in a grid. '''
    # TODO: Make new nodes more likely to make new connections
    
    def __init__(self, d1=21, d2=21):
        ''' Initialize stuff like the node grid. '''
        self.node_grid = [[None for b in xrange(0,d2)] for a in xrange(0,d1)]
        # Create a root node at the center of the grid
        center_d1 = (d1-1) / 2
        center_d2 = (d2-1) / 2
        self.node_grid[center_d1][center_d2] = Node(None)
        
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


class Node(object):
    ''' A single node in a node network. '''
    # Other nodes this node is connected to
    connections = []
    
    def __init__(self, node_creator):
        ''' Initialize this node.
        One initalize operation is to add creating node as a connected node.
        '''
        # Add the parent node as a connected node
        self.connections.append(node_creator)
        
    def create_node(self):
        ''' Create a new node off of this one. '''
        pass
        
        
        
        