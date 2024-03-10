# AirBnB Clone Project

## Project Description

This project is an implementation of a simplified AirBnB clone, focusing on the development of a command-line interface (CLI) for managing various aspects of the application. The goal is to create a user-friendly interface that allows users to interact with and manage AirBnB-like data.

## Command Interpreter

The command interpreter is a command-line interface that enables users to interact with the AirBnB clone application. It provides a set of commands for managing different functionalities, such as creating and managing user accounts, listing and booking properties, and performing various administrative tasks.

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your_username/airbnb_clone.git
   ```

2. Navigate to the project directory:

   ```bash
   cd airbnb_clone
   ```

3. Run the command interpreter:

   ```bash
   ./console.py
   ```

### How to Use the Command Interpreter

Once the command interpreter is running, you can use the following commands:

- **create**: Create a new instance of a specified class.
  ```bash
  create <class_name>
  ```

- **show**: Display information about a specific instance.
  ```bash
  show <class_name> <instance_id>
  ```

- **destroy**: Delete an instance based on the class name and ID.
  ```bash
  destroy <class_name> <instance_id>
  ```

- **all**: Display all instances or all instances of a specific class.
  ```bash
  all [class_name]
  ```

- **update**: Update an instance with new attribute values.
  ```bash
  update <class_name> <instance_id> <attribute_name> "<attribute_value>"
  ```

- **quit/EOF**: Exit the command interpreter.
  ```bash
  quit
  ```

### Examples

1. Create a new user:
   ```bash
   create User
   ```

2. Show information about a specific user:
   ```bash
   show User 123
   ```

3. Destroy a property instance:
   ```bash
   destroy Place 456
   ```

4. Display all instances of a specific class:
   ```bash
   all Review
   ```

5. Update a user's email address:
   ```bash
   update User 789 email "new_email@example.com"
   ```

6. Exit the command interpreter:
   ```bash
   quit
   ```

Feel free to explore additional commands and functionalities within the command interpreter to manage your AirBnB clone application.