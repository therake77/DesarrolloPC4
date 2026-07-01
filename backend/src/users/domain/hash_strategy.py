from abc import ABC, abstractmethod
from users.domain.user import HashedPassword


class HashStrategy(ABC):

    @abstractmethod
    def hash(self, string : str )-> HashedPassword:
        pass

    @abstractmethod
    def compare_hash(self, string : str, hashed : HashedPassword) -> bool:
        pass