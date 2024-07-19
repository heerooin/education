from typing import Any, Callable
from functools import wraps


def log(filename: Any) -> Callable:
    """Декоратор логирования вызова функции и результат в консоль или файл"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} called with args: {args}, kwargs:{kwargs}. Result: {result}"
                with open(filename, "a") as f:
                    f.write(log_message + "\n")
                print(log_message)
            except Exception as e:
                error_message = f"{func.__name__} error: {e}. Inputs:{args}, {kwargs}"
                with open(filename, "a") as f:
                    f.write(error_message + "\n")
                print(error_message)
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x / y


my_function(2, 0)
