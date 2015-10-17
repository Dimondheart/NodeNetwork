import sys
import traceback

import nodenetwork


class Main(object):
    ''' Program entry point. '''
    def __init__(self):
        self.node_net = nodenetwork.NodeNetwork(9,9)

    def start(self):
        ''' Start running the main loop. '''
        print("\n\nType '@help' for assistance.\n")
        self.run()

    def run(self):
        ''' Runs and manages the main loop. '''
        # Allow the user to enter commands, which includes python code
        while True:
            cmd = input(">>>").strip()
            if len(cmd) <= 0:
                continue
            # Non-python code commands ("developer commands")
            # TODO: Handle these more generically
            elif cmd[0] == "@":
                dev_cmd = cmd[1:].strip()
                # Print out all commands plus help info
                if len(dev_cmd) == 0 or dev_cmd == "cmds":
                    # TODO: print out dev cmds here
                    print(
                        "@ : List all dev commands",
                        "@cmds : List all dev commands",
                        "@quit : Currently equivalent to 'sys.exit()'",
                        "@help : Display generic help info",
                        "@mknode num=# : Make <num> new nodes with main node as root",
                        "\t<num> default: 1",
                        "@u : Equivalent to 'self.display_stuff()'",
                        sep='\n'
                        )
                # Quit, for just in case you can't use CTRL+C
                elif dev_cmd == "quit":
                    sys.exit()
                # Print out generic help info
                elif dev_cmd == "help":
                    print(
                        "Type developer commands (start with @) or python code.",
                        "  (Just typing '@' lists all developer commands).",
                        "~Scope note: python code entered will have a scope",
                        "  of inside m.run() in main.py",
                        sep="\n"
                        )
                # Quickly create some nodes
                elif dev_cmd[:len("mknode")] == "mknode":
                    args = dev_cmd[len("mknode")+1:].split(' ')
                    num = 1
                    # TODO: Be able to specify the root node
                    for arg in args:
                        if "num" in arg:
                            num = int(arg.split('=')[1])
                    for n in range(num):
                        getattr(self.node_net, "main_root_node").create_node()
                # Shortcut for updating everything
                elif dev_cmd == "u":
                    self.display_stuff()
                # Invalid dev command
                else:
                    print(
                        "'{}' is not a valid developer command.".format(
                            dev_cmd
                            )
                        )
            # Otherwise evaluate it as python code
            else:
                # Print out any exeptions that occur and keep going
                try:
                    eval(cmd)
                except Exception:
                    traceback.print_exc()
            # Separate each cmd block of text with a blank line
            print('')

    def display_stuff(self):
        ''' Used for displaying data as text output. '''
        self.print_sep_text(title="Active Nodes (X's)")
        self.node_net.display_active_nodes()
        self.print_sep_text(title="Connections Per Node")
        self.node_net.display_connection_count()

    def print_sep_text(self, title=''):
        ''' Print the terminal output section separator with title if
        specified.
        '''
        print("\n-----", title, "-----\n", sep='', end='')


class InvalidNodeCreator(object):
    ''' Just used to test the UnknownNodeCreator exception. '''
    
    def __init__(self):
        pass
        
    def cbn(self):

        badnode = Node(self)


m = Main()
m.start()