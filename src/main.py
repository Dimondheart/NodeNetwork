import sys
import traceback
import string

import nodenetwork


class Main(object):
    ''' Program entry point. '''
    def __init__(self):
        self.node_net = nodenetwork.NodeNetwork(5,9)
        self.dev_cmds = DevCommand(self)

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
                # TODO: Utilize new DevCommand class here
                dev_cmd = cmd[1:].strip()
                # Print out all commands plus help info
                if len(dev_cmd) == 0 or dev_cmd == "cmds":
                    print(
                        "@ : List all dev commands",
                        "@cmds : List all dev commands",
                        "@quit : Currently equivalent to 'sys.exit()'",
                        "@help : Display generic help info",
                        "@mknode num=# mode='': Make some new nodes",
                        "   <num> number of new nodes",
                        "   <mode> 'oneroot' or 'chain'",
                        "      ~oneroot : all new nodes stem from root",
                        "      ~chain : each node stems from previous node",
                        "@nodeat x=# y=# : Print the node object located at (x,y)",
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
                    mode = "oneroot"
                    root = getattr(self.node_net, "main_root_node")
                    # Process arguments
                    for arg in args:
                        if "num" in arg:
                            num = int(arg.split('=')[1].strip().replace(',', ''))
                        elif "mode" in arg:
                            mode = arg.split('=')[1].strip()
                        elif "rootpos" in arg:
                            coords_str = arg.split('=')[1].strip().split(',')
                            x, y = [int(c.strip()) for c in coords_str]
                            print(x, ',', y)
                            # root = getattr(self.node_net, "node_grid")[x][y]
                    if mode == "oneroot":
                        for n in range(num):
                            root.create_node()
                    elif mode == "chain":
                        for n in range(num):
                            root = root.create_node()
                    else:
                        print("Invalid @mknode <mode> specified.")
                # Shortcut for updating everything
                elif dev_cmd == "u":
                    self.display_stuff()
                elif dev_cmd[:len("nodeat")] == "nodeat":
                    args = dev_cmd[len("mknode")+1:].split(' ')
                    x = 0
                    y = 0
                    for arg in args:
                        av_pair = [av.strip().replace(',','') for av in arg.split('=')]
                        if av_pair[0] == "x":
                            x = int(av_pair[1])
                        elif av_pair[0] == "y":
                            y = int(av_pair[1])
                    print(getattr(self.node_net, "node_grid")[x][y])

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


class DevCommand(object):
    ''' Class for processing a developer command. '''

    # Character that indicates a dev command
    dev_cmd_marker = "@"
    # A Template dev command to use for all commands
    template_cmd = {
        "aliases" : [],
        "helpsummary" : "",
        "args" : [],
        "arghelp" : []
        }
    # Lists all the commands
    listcmds = {
        "aliases" : ["cmds", ""],
        "helpsummary" : "List all dev commands",
        "args" : None,
        "arghelp" : None
        }
    # Exit the program
    # quit = ("quit")
    # Print out general help info
    # generalhelp = ("help")
    # Create one or more nodes
    mknode = {
        "aliases" : ["mknode"],
        "helpsummary" : "Make some new nodes",
        "args" : ["num", "mode"],
        "arghelp" : [
            "Number of new nodes to make",
            "'oneroot' or 'chain'\n" +
            "   ~oneroot : all new nodes stem from root\n" +
            "   ~chain : each node stems from previous node\n"
            ]
        }
    # Print out the object in the node grid at specified position
    # nodeat = ("nodeat")
    # Print out a bunch of useful data to the terminal
    # displaydata = ("u")
    # Clear the main node network
    # reset = ("reset")

    def __init__(self, creator):
        self.creator = creator

    def parse_cmd(self, dev_cmd):
        parsed = dev_cmd.split(' ')
        parsed = [piece.strip() for piece in parsed[:] if piece not in string.whitespace]
        return parsed[0], parsed[1:]

    def do_cmd(self, dev_cmd):
        cmd, args = parse_cmd(dev_cmd)
        print(cmd, args)


m = Main()
m.start()