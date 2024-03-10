from base_model import BaseModel

class Note(BaseModel):
    def __init__(self, **kwargs):
        super().__init__({"title", "description", "user_id", "priority"})