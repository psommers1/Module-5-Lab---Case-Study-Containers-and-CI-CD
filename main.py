def hello_world():
    print("Hello, World!")


def calculate_sum(a, b):
    return a + b


def multiply(a, b):
    return a * b


if __name__ == "__main__":
    hello_world()
    result = calculate_sum(5, 10)
    print(f"Sum: {result}")
    product = multiply(5, 10)
    print(f"Product: {product}")
