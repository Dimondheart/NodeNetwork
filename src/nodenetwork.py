from node import Node


class NodeNetwork(object):
    ''' Handles a collection of nodes in a grid. '''
    
    def __init__(self, d1=5, d2=5):
        ''' Initialize stuff like the node grid. '''
        # TODO?: Consider using numpy arrays
        self.node_grid = [[None for b in range(0,d2)] for a in range(0,d1)]
        # Create a root node at the center of the grid
        center_d1 = int((d1-1) / 2)
        center_d2 = int((d2-1) / 2)
        self.main_root_node = Node(self)
        self.node_grid[center_d1][center_d2] = self.main_root_node
        
    def __iter__(self):
        ''' Iterate over the nodes in grid, starting at node_grid[0][0]. '''
        for d1 in self.node_grid:
            for d2 in d1:
                yield d2

    def add_node(self, root_node, new_node):
        '''Adds a new node as close as possible to the root node. '''
        # Get the coordinates of the main root node
        center_d1 = int((len(self.node_grid)-1) / 2)
        center_d2 = int((len(self.node_grid[0])-1) / 2)
        # Create the pathfinder, starting at the main root node
        pathfinder = PathfinderIterator2D(
            self.node_grid,
            start_at=(center_d1, center_d2)
            )
        # Find an empty node space
        for coords in pathfinder:
            if self.node_grid[coords[0]][coords[1]] == None:
                self.node_grid[coords[0]][coords[1]] = new_node
                return
        # No empty node found, raise exception
        raise FullNodeGrid()
    
    def display_active_nodes(self):
        ''' Print out a grid of what state each node is in. '''
        num_columns = len(self.node_grid[0])
        curr_col = 1
        for node in self:
            if curr_col > num_columns:
                print('\n', sep='', end='')
                curr_col = 1
            print_char = '?'
            if node is None:
                print_char = '-'
            elif isinstance(node, Node):
                print_char = 'X'
            print(print_char, sep='', end=' ')
            curr_col += 1

    def display_connection_count(self):
        ''' Print out a grid of the number of connections each node has. '''
        # Figure out max num connections (make printout cleaner)
        max_con = max(len(node.connections) for node in self if node is not None)
        num_columns = len(self.node_grid[0])
        curr_col = 1
        for node in self:
            # Next print row
            if curr_col > num_columns:
                print('\n', sep='', end='')
                curr_col = 1
            # Create a base string to print
            to_print = ""
            # Modify the number to print if node is active
            if node is not None:
                num_str = str(len(getattr(node, "connections")))
                # Add padding characters
                if len(num_str) < len(str(max_con)):
                    for char in range(len(str(max_con))-len(num_str)):
                        to_print += '0'
                # Concate padding with actual connection count
                to_print += num_str
            # Otherwise print filler text
            else:
                for char in range(max(len(str(max_con)),1)):
                    to_print += '-'
            # Add spacing
            to_print += ' '
            # Print the formatted string
            print(to_print, sep='', end='')
            curr_col += 1
        

class FullNodeGrid(Exception):
    ''' Exception raised when attempting to add a node to a full node grid. '''
    def __init__(self):
        pass
        
    def __str__(self):
        return "Cannot add a node to a full node grid."


class PathfinderIterator2D(object):
    ''' An iterable object used to iterate over a 2d grid for use in simple
    pathfinding algorithms.
    '''

    def __init__(self, grid_list, start_at=(0,0)):
        ''' Initialize stuff like the reference to the grid to iterate over. '''
        # The 2D list/array to iterate over
        self.iter_over = grid_list
        # What grid space to start at
        self.first_tile = start_at

    def __iter__(self):
        ''' Iterate over the path determined by the algorithm.
        Returns : A coordinate pair as a tuple
        '''
        width = len(self.iter_over)
        height = len(self.iter_over[0])
        # Tiles already parsed
        done = []
        # Tiles to search, FIFO (first in first out)
        queue = []
        # Add the tile to start with
        queue.append(self.first_tile)
        while len(queue) > 0:
            next_tile = queue.pop(0)
            done.append(next_tile)
            cx = next_tile[0]
            cy = next_tile[1]
            # Potential tiles to parse
            right = (cx + 1, cy)
            down = (cx, cy - 1)
            left = (cx - 1, cy)
            up = (cx, cy + 1)
            # Right tile
            if right not in done and right not in queue and right[0] in range(0, width):
                queue.append(right)
            # Down tile
            if down not in done and down not in queue and down[1] in range(0, height):
                queue.append(down)
            # Left tile
            if left not in done and left not in queue and left[0] in range(0, width):
                queue.append(left)
            # Up tile
            if up not in done and up not in queue and up[1] in range(0, height):
                queue.append(up)
            # Next item in iterable
            # yield self.iter_over(next_tile[0], next_tile[1])
            # Next coord pair
            yield next_tile