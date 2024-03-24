import redis
import uuid
from functools import wraps
from typing import Callable, Optional, Union

def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a function is called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to count calls."""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper

def call_history(method: Callable) -> Callable:
    """Decorator to store history of inputs and outputs for a function."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to store history."""
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        
        self._redis.rpush(inputs_key, str(args))  # Store input arguments
        output = method(self, *args, **kwargs)    # Execute the function
        self._redis.rpush(outputs_key, str(output))  # Store the output
        
        return output

    return wrapper

class Cache():
    """Cache class"""

    def __init__(self) -> None:
        """Initialize"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Retrieve data from Redis"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """Get string data from Redis"""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """Get integer data from Redis"""
        return self.get(key, fn=int)

# Example usage
if __name__ == "__main__":
    cache = Cache()

    s1 = cache.store("first")
    print(s1)
    s2 = cache.store("second")
    print(s2)
    s3 = cache.store("third")
    print(s3)

    inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
    outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

    print("inputs:", [item.decode('utf-8') for item in inputs])
    print("outputs:", [item.decode('utf-8') for item in outputs])
