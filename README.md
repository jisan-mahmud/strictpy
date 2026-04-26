# 🚀 StrictPy

> Strict runtime type enforcement for Python — no coercion, no surprises.

StrictPy makes Python behave more like C/C++ when it comes to type safety.
It enforces **exact type matching** for function arguments and return values at runtime.

---

## ✨ Features

* ✅ Strict function argument validation
* ✅ Return type enforcement
* ❌ No implicit type conversion
* ⚡ Lightweight and fast
* 🧠 Clear, developer-friendly error messages

---

## 🔥 Why StrictPy?

Python is dynamically typed:

```python
def add(x: int, y: int):
    return x + y

add("1", 2)  # ❌ No error by default
```

StrictPy enforces **fail-fast behavior**:

```python
from strictpy import strict

@strict
def add(x: int, y: int) -> int:
    return x + y

add(1, 2)        # ✅ 3
add("1", 2)      # ❌ StrictTypeError
```

---

## 🧪 Return Type Enforcement

```python
@strict
def get_number() -> int:
    return "10"   # ❌ Error
```

---

## ⚠️ Philosophy

StrictPy follows a simple rule:

> "Wrong type? Fail immediately."

No:

* silent conversions
* hidden bugs
* unexpected behavior

---

## 🆚 Comparison

| Feature              | StrictPy | Pydantic  | mypy |
| -------------------- | -------- | --------- | ---- |
| Runtime validation   | ✅        | ✅         | ❌    |
| Strict (no coercion) | ✅        | ❌         | ✅    |
| Return enforcement   | ✅        | ⚠️ manual | ❌    |
| Lightweight          | ✅        | ❌         | ✅    |

---

## 📦 Installation

```bash
pip install strictpy
```

---

## 📂 Project Structure

```
strictpy/
├── decorator.py
├── validator.py
├── errors.py
```

---

## 🚀 Roadmap

### v1

* [x] Argument validation
* [x] Return validation
* [x] Custom errors

### v2

* [ ] Support for List, Dict, Optional
* [ ] Better error messages
* [ ] Config system

### v3

* [ ] Django / API integration
* [ ] Performance optimizations

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make changes
4. Submit a PR

---

## 📜 License

This project is licensed under the MIT License.

---

## 💡 Author

Backend-focused developer building reliable and predictable systems.

---

## ⭐ Final Thought

> Python is flexible. StrictPy makes it predictable.
