from functools import wraps
from inspect import signature


class StrictTypeError(TypeError):
    pass


def strict(func):
    sig = signature(func)
    annotations = func.__annotations__

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        # Validate arguments
        for name, value in bound.arguments.items():
            if name in annotations:
                expected = annotations[name]

                if type(value) is not expected:
                    raise StrictTypeError(
                        f"Argument '{name}' expected {expected.__name__}, "
                        f"got {type(value).__name__} ({value})"
                    )

        result = func(*args, **kwargs)

        # Validate return
        return_type = annotations.get("return")
        if return_type is not None:
            if type(result) is not return_type:
                raise StrictTypeError(
                    f"Return value expected {return_type.__name__}, "
                    f"got {type(result).__name__} ({result})"
                )

        return result

    return wrapper