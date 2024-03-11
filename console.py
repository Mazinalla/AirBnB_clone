#!/usr/bin/env python3
"""Console module for HBNB project"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand Module

    This module defines a simple command-line interpreter using the cmd module.
    It provides a prompt with "(hbnb) " and allows the user to enter commands.

    Commands:
    - quit: Exit from the console.
    - EOF: Exit on system end of file.
    - help: Get help on commands.

    Usage:
    1. Run the script to start the console.
    2. Enter commands at the prompt.

    Example:
    ```
    (hbnb) help
    (hbnb) quit
    ```
        
                """

    prompt = "(hbnb) "

    def handle_empty_line(self, line):
        """
        Eliminates empty lines
        """
        return False

    def do_quit(self, line):
        """Handles the 'quit' command

        Args:
            line(args): input argument for quiting
            the terminal

        """
        return True

    def do_EOF(self, line):
        """Quits command interpreter with ctrl+d

         Args:
            line(args): input argument for quiting
            the terminal

        """
        return True
    
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()

