from strictpy import strict

@strict
def add(x: int, y: int) -> int:
    return x + y

print(add(2, 3))      # ✅ 5
print(add("2", 3))    # ❌ StrictTypeError