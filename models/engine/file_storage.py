#!/usr/bin/python3

import json
import os

class FileStorage:
    __file_path = "file.json"
    __object = {}

    def all(self):
        return self.__object
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__object[key] = obj

    def save(self, __object, file_path):
        __file_path = "objects.json"
        serialized_objects = {}
        for key, obj in __object.items():
            serialized_objects[key] = obj.__dict__
        
        with open(file_path, 'w') as json_file:
            json.dump(serialized_objects, json_file, indent=4)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                data = json.load(json_file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'Example':
                        cls = Example
                    elif class_name == 'BaseModel':
                        cls = BaseModel  # Assuming BaseModel is defined in this module
                    else:
                        continue
                    if key not in self.__objects:  # Check if it's a new instance
                        obj = cls(**value)
                        obj.new()  # Call new method on storage
                        self.__objects[key] = obj