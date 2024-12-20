
from .File import File
import json
import os

class JsonFile(File):
    def __init__(self, Path):
        super().__init__(Path)
        self.Json: dict = json.loads(self.file.read())
    
    def load(self):
        self.file.seek(0)
        self.Json = json.loads(self.file.read())
        return self.Json

    def save(self, key: str, value: any = None):
        self.Json[key] = value
        self.file.write(json.dumps(self.Json, indent=4))
        return self.Json

    def reload(self):
        return self.load()
