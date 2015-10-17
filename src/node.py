import nodenetwork

class Node(object):
    ''' A single node in a node network. '''
    
    def __init__(self, creator):
        ''' Initialize this node.
        One initalize operation is to add creating node as a connected node.
        '''
        self.connections = []
        # Normal new node initializing
        if isinstance(creator, Node):
            # What network this node is part of
            self.my_net = getattr(creator, "my_net")
            # Add the parent node as a connected node
            self.add_connection(creator)
        # NodeNetwork main root node initializing
        elif isinstance(creator, nodenetwork.NodeNetwork):
            self.my_net = creator
        # Unknown node creator, raise exception
        else:
            raise UnknownNodeCreator(type(creator))
        
    def create_node(self):
        ''' Create a new node off of this one. '''
        new_node = Node(self)
        self.my_net.add_node(self, new_node)
        self.add_connection(new_node)
        # Return the new node so the create requestor can use it
        return new_node

    def add_connection(self, node):
        self.connections.append(node)


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