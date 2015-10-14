import sys

import nodenetwork


class Main(object):
    ''' Program entry point. '''
    def __init__(self):
        self.node_net = nodenetwork.NodeNetwork(9,9)

    def start(self):
        ''' Start running the main loop. '''
        print("Type '@help' for assistance.")
        self.run()

    def run(self):
        ''' Runs and manages the main loop. '''
        # Allow the user to enter commands, which includes python code
        while True:
            cmd = input(">>>").strip()
            if len(cmd) <= 0:
                continue
            # Non-python code commands ("developer commands")
            elif cmd[0] == "@":
                dev_cmd = cmd[1:]
                # No command specified, print out all commands
                if len(dev_cmd) == 0:
                    # TODO: print out dev cmds here
                    print("TODO: print all @<cmd>'s here")
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
                else:
                    print(
                        "'{}' is not a valid developer command.".format(
                            dev_cmd
                            )
                        )
            # Otherwise evaluate it as python code
            else:
                eval(cmd)
            # Separate each cmd block of text with a blank line
            print('')

    def update(self):
        ''' Used for displaying data as text output. '''
        self.print_sep_text(title="Active Nodes (X's)")
        self.node_net.display_network_text()
        self.print_sep_text()

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