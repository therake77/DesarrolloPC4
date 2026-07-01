from users.domain.hash_strategy import HashStrategy
import bcrypt
from users.domain.user import HashedPassword

class BcryptHashStrategy(HashStrategy):

    def hash(self, string : str )-> HashedPassword:
        return HashedPassword(
            bcrypt.hashpw(  #type: ignore
                string.encode("utf-8"),
                bcrypt.gensalt()    #type: ignore
                ).decode("utf-8")
        )

    def compare_hash(self, string : str, hashed : HashedPassword) -> bool:
        return bcrypt.checkpw(  #type: ignore
            string.encode("utf-8"),
            hashed.as_raw.encode("utf-8")
        )
