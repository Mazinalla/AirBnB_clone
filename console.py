'''cmd is a module that help you built your own shell'''
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand Module

    This module defines a simple command-line interpreter using the cmd module.
    It provides a prompt with "(hbnb) " and allows the user to enter commands.

    Commands:
    - help: Get help on commands.
    - EOF: Exit on system end of file.
    - quit: Exit from the console.

    Usage:
    1. Run the script to start the console.
    2. Enter commands at the prompt.

    Example:
    ```
    (hbnb) help
    (hbnb) quit
    ```

    Methods:
    - do_help(self, args): Get help on commands.
    - do_EOF(self, arg): Exit on system end of file.
    - do_quit(self, arg): Exit from the console.
    - emptyline(self): Do nothing on an empty input line.

    Attributes:
    - prompt (class attribute): The prompt string displayed at the beginning of each command line.

    Example:
    ```python
    if __name__ == '__main__':
        HBNBCommand().cmdloop()
    ```

    Note: This module serves as a base for a more complex console and can be extended to include additional functionality.

    """
    prompt = "(hbnb) "

    def do_help(self, args):
        """Get help on commands
           'help' or '?' with no arguments prints a list of commands for which help is available
           'help <command>' or '? <command>' gives help on <command>
        """

        cmd.Cmd.do_help(self, args)

    def do_EOF(self, arg):
        """Exit on system end of file"""
        return -1
    
    def do_quit(self, arg):
        """Exit from the console"""
        return -1
    
    def emptyline(self):    
        """Do nothing on an empty input line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

