# 存储审核函数
APPROVAL_FUNCS = {}


def approval_func(func_name: str = None):
    """
    审核函数的装饰器
    """

    def wrapper(func):
        func_key = func_name if func_name else func.__name__
        APPROVAL_FUNCS[func_key] = func

        def inner_wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return inner_wrapper

    return wrapper
