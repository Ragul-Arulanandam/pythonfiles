def my_func(func):
    def wrap_func():
        print("Hi")
        func()
        print("Hello")
    return wrap_func

@my_func
def hello():
    print("hello")
def bye():
    print("bye")

hello()
bye()
