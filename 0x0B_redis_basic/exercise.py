def replay(func: Callable) -> None:
    """Replay function to display the history of calls of a particular function."""
    qualified_name = func.__qualname__
    inputs_key = f"{qualified_name}:inputs"
    outputs_key = f"{qualified_name}:outputs"

    inputs = cache._redis.lrange(inputs_key, 0, -1)
    outputs = cache._redis.lrange(outputs_key, 0, -1)

    num_calls = min(len(inputs), len(outputs))

    print(f"{qualified_name} was called {num_calls} times:")

    for i in range(num_calls):
        input_args = eval(inputs[i].decode('utf-8'))
        output = outputs[i].decode('utf-8')
        print(f"{qualified_name}{input_args} -> {output}")


# Example usage
if __name__ == "__main__":
    cache = Cache()

    cache.store("foo")
    cache.store("bar")
    cache.store(42)

    replay(cache.store)
