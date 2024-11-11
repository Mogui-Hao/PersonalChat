
from abc import ABC, abstractmethod
import os

class File(ABC):
    def __init__(self, Path: str):
        super().__init__()
        self._path = Path
        self.file = open(os.path.join(os.getcwd(), Path), "r+", encoding="utf-8")
    
    @abstractmethod
    def load(self): ...
    @abstractmethod
    def save(self, key: str, value: any): ...
    @abstractmethod
    def reload(self): ...
