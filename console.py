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

    def do_quit(self, arg):
        """Exit from the console"""
        return True

    def do_EOF(self, arg):
        """Exit on system end of file"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

