print('Generator that returns a sequence of even numbers from 0 to N:')


def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


for num in even_numbers(10):
    print(num)

print('Generator that generates a Fibonacci sequence up to a certain number N:')


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fibonacci(10):
    print(num)

print('Iterator to output the elements of a list in reverse order:')


class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            result = self.data[self.index]
            self.index -= 1
            return result
        else:
            raise StopIteration


my_list = [1, 2, 3, 4, 5]
reverse_iterator = ReverseIterator(my_list)
for item in reverse_iterator:
    print(item)

print('Iterator that returns all even numbers in the range 0 to N:')


class EvenNumbersIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration


for num in EvenNumbersIterator(10):
    print(num)

print('Decorator that logs the arguments and results of the called function:')


def log_function_call(func):
    def wrapper(*args):
        print(f"Calling function: {func.__name__} with args: {args}")
        result = func(*args)
        print(f"Function {func.__name__} returned: {result}")
        return result

    return wrapper


@log_function_call
def my_function(a, b):
    return a + b


my_function(2, 3)

print('Decorator that catches and handles exceptions that occur during function execution:')


def handle_exceptions(func):
    def wrapper(*args):
        try:
            result = func(*args)
            return result
        except Exception as e:
            print(f"An exception occurred: {e}")

    return wrapper


@handle_exceptions
def divide(a, b):
    return a / b


divide(10, 0)

