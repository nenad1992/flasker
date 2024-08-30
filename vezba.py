def my_decorator(say_hello):
    def wrapper(name):
        print("Something is happening before the function is called.")
        
        result = say_hello(name)

        print("Something is happening after the function is called.")

        return result
    return wrapper

@my_decorator
def say_hello(name):
    return f"Hello, {name}!"



f = say_hello("Petar")
print(f)