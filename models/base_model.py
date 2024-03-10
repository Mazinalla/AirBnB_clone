import uuid
import datetime
from models import storage

"""
created
updated
soft_delete
id
"""

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4().hex)
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        self.soft_deleted = False
        if kwargs:
            for key, value in kwargs.items():
                # ignore key __class__ from kwargs
                if key != '__class__':
                    setattr(self, key, value)
                # Convert 'created_at' and 'updated_at' strings to datetime objects
            storage.new(self)
            
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            storage.new(self)
    
    def __str__(self):
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()
        
    def to_dict(self):
        # Create a dictionary containing all keys/values of __dict__
        obj_dict = self.__dict__.copy()

        # Add '__class__' key with the class name of the object
        obj_dict['__class__'] = self.__class__.__name__

        # Convert 'created_at' and 'updated_at' to string in ISO format
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
