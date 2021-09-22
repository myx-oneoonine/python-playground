def new_func(param):
    print(f"decorator param value: {param}")

    def decorator(func):
        print(f"function name: {func.__name__}")

        def wrapper(func_arg):
            print(f"decorator param value: {param}")
            if not str(func_arg).startswith('A'):
                raise Exception("sssss")
            return func(func_arg)

        return wrapper

    return decorator


@new_func(1)
def say_hi(func_arg):
    return f"matafaka {func_arg}"


if __name__ == '__main__':
    print(say_hi("Akak"))
