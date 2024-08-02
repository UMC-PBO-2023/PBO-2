from abc import ABC, abstractmethod

class DosenInterface(ABC):
    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def store(self, dosen_obj):
        pass
    
    @abstractmethod
    def find(self, dosen_id):
        pass

    @abstractmethod
    def update(self, dosen_id, dosen_obj):
        pass
    
    @abstractmethod
    def delete(self, dosen_id):
        pass
