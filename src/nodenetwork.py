from node import Node


class NodeNetwork(object):
    ''' Handles a collection of nodes in a grid. '''
    
    def __init__(self, d1=5, d2=9):
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
        root_pos = (0,0)
        for x in range(0, len(self.node_grid)):
            if root_node in self.node_grid[x]:
                root_pos = (x, self.node_grid[x].index(root_node))
        # Create the pathfinder, starting at the root node position
        pathfinder = PathfinderIterator2D(
            self.node_grid,
            start_at=root_pos
            )
        # Find an empty node space
        for coords in pathfinder:
            if self.node_grid[coords[0]][coords[1]] == None:
                self.node_grid[coords[0]][coords[1]] = new_node
                print("Found Empty Node")
                return
        # No empty node found, raise exception
        raise FullNodeGrid()
    
    def display_active_nodes(self):
        ''' Print out a grid of what state each node is in. '''
        num_rows = len(self.node_grid[0])
        spacing = ' '
        rows = ["" for row in range(num_rows)]
        curr_row = 0
        for node in self:
            # Default print char, indicates a non-node/None obj in the grid
            print_char = '?'
            # Node is unoccupied
            if node is None:
                print_char = '-'
            # Node is occupied by a node obj
            elif isinstance(node, Node):
                print_char = 'X'
            # Add the node character + spacing to this row
            rows[curr_row] += print_char
            rows[curr_row] += spacing
            # Move to the next row
            curr_row += 1
            # Go back to first row if just on last row
            if curr_row >= num_rows:
                curr_row = 0
        # Print each row, reverse the rows so 0,0 is on lower left
        for row in rows[::-1]:
            print(row, sep='', end='\n')

    def display_connection_count(self):
        ''' Print out a grid of the number of connections each node has. '''
        # Figure out the highest # of connections
        max_con = max(len(node.connections) for node in self if node is not None)
        num_rows = len(self.node_grid[0])
        spacing = ' '
        rows = ["" for row in range(num_rows)]
        curr_row = 0
        for node in self:
            to_print = ""
            # Determine number to display
            if node is not None:
                num_str = str(len(getattr(node, "connections")))
                # Add padding characters
                if len(num_str) < len(str(max_con)):
                    for char in range(len(str(max_con))-len(num_str)):
                        to_print += ' '
                # Concate padding with actual connection count
                to_print += num_str
            # Otherwise print filler text
            else:
                for char in range(max(len(str(max_con)),1)):
                    to_print += '-'
            # Add to row
            rows[curr_row] += to_print
            # Add spacing
            rows[curr_row] += spacing
            # Go to next row
            curr_row += 1
            # Go back to first row if just on last row
            if curr_row >= num_rows:
                curr_row = 0
        # Print each row, reverse the rows so 0,0 is on lower left
        for row in rows[::-1]:
            print(row, sep='', end='\n')
        

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
        print("Finding An Empty Node...")
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
            print("Current In Pathfinder:", next_tile)
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
                print("Queueing Right")
                queue.append(right)
            # Down tile
            if down not in done and down not in queue and down[1] in range(0, height):
                print("Queueing Lower")
                queue.append(down)
            # Left tile
            if left not in done and left not in queue and left[0] in range(0, width):
                print("Queueing Left")
                queue.append(left)
            # Up tile
            if up not in done and up not in queue and up[1] in range(0, height):
                print("Queueing Upper")
                queue.append(up)
            # Next item in iterable
            # yield self.iter_over(next_tile[0], next_tile[1])
            # Next coord pair
            yield next_tile