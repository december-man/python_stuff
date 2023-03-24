# lets create a decorator function

def func_to_decorate(x):
    print(x ** 2)

def the_decorator(func):
    def wrapper(x):
        print("func_to_decorate returns x squared")
        func(x)
        print("told yo so")
    return wrapper

#decorated func output
decorated_func = the_decorator(func_to_decorate)
decorated_func(2)
#original func output
func_to_decorate(2)

# using python syntax
@the_decorator
def func_under_decorator(x):
    print(f"im just a func!!! But here's your x^2 {x ** 2}")
    
func_under_decorator(2)

# use decorator's closure syntax to count function calls

def call_counter(origin_function):
    count = 0

    def wrapper(func_arg):
        nonlocal count
        count += 1
        print(f'call number is {count}')
        
        return origin_function(func_arg)

    return wrapper


@call_counter
def say_hello(guest_name):
    print(f'Hello, {guest_name}')
    
    
say_hello('hoh')



def decorator_maker(decorator_arg1, decorator_arg2):
    print('I create decorators. I got the following arguments:', decorator_arg1, decorator_arg2)
    
    def decorator_function(func):
        print('I am a decorator. I got a function:', func)
                
        def wrapper(function_arg1, function_arg2):
            print(
                'I am a wrapper around the origin function.\nAnd I have access to \
                all arguments: \n'
                f'\t- and decorator: {decorator_arg1} {decorator_arg2}\n'
                f'\t- and functions: {function_arg1} {function_arg2}\n'
            )
            return func(function_arg1, function_arg2)
        
        return wrapper
    
    return decorator_function