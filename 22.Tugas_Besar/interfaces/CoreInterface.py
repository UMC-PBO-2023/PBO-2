#Interface/khsInterface.py
from abc import ABC, abstractmethod

class CoreInterface(ABC):
    @abstractmethod
    def all():
        pass

    @abstractmethod
    def store(khs_obj):
        pass

    @abstractmethod
    def find(khs_id):
        pass

    @abstractmethod
    def update(khs_id, khs_obj):
        pass

    @abstractmethod
    def delete(khs_id):
        pass