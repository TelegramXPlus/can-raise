from src.can_raise import can_raise


@can_raise(ValueError, TypeError)
def random_function(x: int) -> None:
    if x == 0:
        raise ValueError("This is a test error")
    raise TypeError("This is a test error")


def test_can_raise_decorator():
    assert hasattr(random_function, "__raises__")
    assert random_function.__raises__ == (ValueError, TypeError)

    try:
        random_function(0)
    except ValueError:
        pass
    else:
        assert False, "ValueError was not raised as expected"

    try:
        random_function(1)
    except TypeError:
        pass
    else:
        assert False, "TypeError was not raised as expected"
