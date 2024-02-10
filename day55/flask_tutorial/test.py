inputs = eval(input())  # create a list like [1,2,3]


def logging_decorator(fn):
    def wrapper(*args):
        print(f"you called a function {fn.__name__}{args}")
        result = fn(args[0],args[1], args[2])
        print(f"Result is:{result}")
    return wrapper


@logging_decorator
def a_function(a,b,c):
    return a*b*c


a_function(inputs[0], inputs[1], inputs[2])