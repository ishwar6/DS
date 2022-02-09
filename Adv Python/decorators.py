# it accepts a function as arg, call it in wrapper function and returns that wrapper function
# use @function_name to apply it on other function
def decorator_function(funtion_on_which_decorator_to_be_called):
    print("a")

    def wrapper_function():
        print("Function running is: {}".format(
            funtion_on_which_decorator_to_be_called.__name__))
        print("aa")
        return funtion_on_which_decorator_to_be_called()
    print("v")
    return wrapper_function


def display():
    print("display")


decorated_function = decorator_function(display)

decorated_function()
