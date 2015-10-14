class FullNodeGrid(Exception):
    def __init__(self):
        pass
        
    def __str__(self):
        return "The specified node grid is completely full."


class Storage(object):
    ''' Handles the collection of nodes. '''
    
    def __init__(self):
        ''' Initialize stuff like the node grid. '''
        self.node_grid = [[None for y in xrange(0,21)] for x in xrange(0,21)]
        # Create a root node at the center of the grid
        center_x = (len(self.node_grid)-1) / 2
        center_y = (len(self.node_grid[0])-1) / 2
        self.node_grid[center_x][center_y] = Node(None)
        
        
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
        raise FullNodeGrid
            
            


class Node(object):
    ''' A single node in the node network. '''
    # Other nodes this node is connected to
    connections = []
    
    def __init__(self, node_creator):
        ''' Initialize this node.
        One initalize operation is to add creating node as a connected node.
        '''
        # Add the parent node as a connected node
        self.connections.append(node_creator)
        
    def create_node(self):
        pass
        
        
        
        