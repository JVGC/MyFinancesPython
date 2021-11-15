from typing import Any, Generic, TypeVar, Union

T = TypeVar("T", covariant=True)  # Success type
E = TypeVar("E", covariant=True)  # Error type


class Ok(Generic[T]):
    """
    A value that indicates success and
    which stores arbitrary data for the return value.
    """

    def __init__(self, value: Any = True) -> None:
        self._value = value

    def is_ok(self) -> bool:
        return True

    def is_err(self) -> bool:
        return False

    def ok(self) -> T:
        """
        Return the value.
        """
        return self._value

    def err(self) -> None:
        """
        Return `None`.
        """
        return None

    @property
    def value(self) -> T:
        """
        Return the inner value.
        """
        return self._value


class Error(Generic[E]):
    """
    A value that signifies failure and
    which stores arbitrary data for the error.
    """

    def __init__(self, value: E) -> None:
        self._value = value

    def is_ok(self) -> bool:
        return False

    def is_err(self) -> bool:
        return True

    def ok(self) -> None:
        """
        Return `None`.
        """
        return None

    def err(self) -> E:
        """
        Return the error.
        """
        return self._value

    @property
    def value(self) -> E:
        """
        Return the inner value.
        """
        return self._value


# define Result as a generic type alias for use
# in type annotations
"""
A simple `Result` type inspired by Rust.
Not all methods (https://doc.rust-lang.org/std/result/enum.Result.html)
have been implemented, only the ones that make sense in the Python context.
"""
Result = Union[Ok[T], Error[E]]
