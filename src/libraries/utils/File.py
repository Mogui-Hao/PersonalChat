
from abc import ABC, abstractmethod
import os

class File(ABC):
    def __init__(self, Path: str):
        super().__init__()
        with open(os.path.join(os.getcwd(), "src/resource", Path), "r+", encoding="utf-8") as f:
            self.file = f
    
    @abstractmethod
    def load(self): ...
    @abstractmethod
    def save(self): ...
    @abstractmethod
    def roload(self): ...
