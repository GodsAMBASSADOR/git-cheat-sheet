# import the function from sam.py
from sam import get_sam_info

def print_hello(name: str) -> str:
    return f"Hello, {name}!"

print(print_hello("Sam"))
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))

print(get_sam_info())