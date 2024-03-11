import cmd
import sys

"""
this cmd interperater
"""

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_help(self, args):
        """Get help on commands
           'help' or '?' with no arguments prints a list of commands for which help is available
           'help <command>' or '? <command>' gives help on <command>
        """
        ## The only reason to define this method is for the help text in the doc string
        cmd.Cmd.do_help(self, args)

    def do_EOF(self, arg):
        """Exit on system end of file"""
        return -1
    
    def do_quit(self, arg):
        """ exit from the console """
        return -1
    
    def emptyline(self):    
        """Do nothing on empty input line"""
        
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
