"""
can-raise is a module that provides a decorator to indicate that a function can raise specific exceptions.
This is useful for documentation purposes and for tools that analyze code for exception handling.
"""
from typing import Callable, ParamSpec, TypeVar, Type


P = ParamSpec("P")
T = TypeVar("T")


def can_raise(*exc: Type[Exception]) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    Decorator to indicate that a function can raise the specified exceptions.

    Args:
        exc: The exceptions that the function can raise. If no exceptions are specified, it defaults to `Exception`.

    Returns:
        A decorator that adds the `__raises__` attribute to the function, indicating the exceptions it can raise.
    """

    if not exc:
        exc = (Exception, )

    def wrapper(func: Callable[P, T]) -> Callable[P, T]:
        try:
            func.__raises__ = exc
        except (AttributeError, TypeError):
            pass
        return func
    return wrapper
