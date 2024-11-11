
from .JsonFile import JsonFile
import json
from dataclasses import dataclass

@dataclass
class LanguageFile(JsonFile):
    def __init__(self, Path):
        super().__init__(Path)
        try:
            self.version = self.Json["info"]["version"]
            self.name = self.Json["info"]["name"]
            self.Tab = self.Json["Tab"]
            self.author = self.Json.get("author", {}).get("name", None)
            self.url = self.Json.get("author", {}).get("url", None)
        except KeyError:
            ...

    def save(self, key: str, value: any = None): ...
    def reload(self): ...
    def load(self): ...
