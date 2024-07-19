from typing import Any, Callable
from functools import wraps


def log(filename: Any) -> Callable:
    """Декоратор логирования вызова функции и результат в консоль или файл"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            try:
                if filename:
                    result = func(*args, **kwargs)
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write('\nmy_function ok')

                else:
                    print("\nmy_function ok")

            except Exception as e:
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(f'\nmy_function error: {e} Inputs: {args}, {kwargs}')
                raise Exception(f'Ошибка: {e}')
            return result
        return wrapper

    return decorator

@log(filename="mylog.txt")
def my_function(x, y):
    """ Функция, складывающая 2 числа"""
    return x + y

print(my_function(12, 0))
