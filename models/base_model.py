
from models.__init__ import storage
import uuid
from datetime import datetime


class BaseModel:

    def __init__(self, *args , **kwargs):
        self.id = str(uuid.uuid4().hex)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                # ignore key __class__ from kwargs
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4().hex)
            self.created_at = datetime.now()


    def __str__(self):
        return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}]"
    
    
    def save(self):
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        # Create a dictionary containing all keys/values of __dict__
        obj_dict = self.__dict__.copy()
        obj_dict[__class__] = self.__class__.__name__

        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict