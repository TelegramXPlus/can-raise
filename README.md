# can-raise

A simple library for decorating functions that can raise exceptions.

## Installation

```bash
pip install can-raise
```

## Usage

```python
from can_raise import can_raise

@can_raise(ValueError)
def validate_int(x: int):
    if x < 0:
        raise ValueError
    return x
```

If you don't provide any value, it will default to `Exception`

```python
@can_raise()
def raise_exc():
    raise TypeError # or any other exception
```

You can also provide more than one argument

```python
@can_raise(ValueError, TypeError)
def raise_exc(x: int):
    if x < 0:
        raise ValueError
    if x > 0:
        raise TypeError
    return x
```