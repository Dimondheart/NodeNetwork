from node import Node

class NodeNetwork(object):
    ''' Handles a collection of nodes in a grid. '''
    # TODO: Make new nodes more likely to make new connections
    # The grid of nodes
    node_grid = []
    # An initial node created as a stem for other nodes
    main_root_node = None
    
    def __init__(self, d1=5, d2=5):
        ''' Initialize stuff like the node grid. '''
        self.node_grid = [[None for b in range(0,d2)] for a in range(0,d1)]
        # Create a root node at the center of the grid
        center_d1 = int((d1-1) / 2)
        center_d2 = int((d2-1) / 2)
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
        for x in range(len(self.node_grid)):
            for y in range(len(self.node_grid[0])):
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
        

class FullNodeGrid(Exception):
    ''' Exception raised when attempting to add a node to a full node grid. '''
    def __init__(self):
        pass
        
    def __str__(self):
        return "Cannot add a node to a full node grid."


class PathfinderIterator2D(object):
    ''' An iterable object used to iterate over a 2d grid for simple
    pathfinding.
    '''
    # The 2D list to iterate over
    iterate_over = None

    def __init__(self, grid_list):
        self.iterate_over = grid_list

    def __iter__(self):
        # TODO: make this actually use a pathfinding algorithm
        for d1 in self.iterate_over:
            for d2 in d1:
                yield d2