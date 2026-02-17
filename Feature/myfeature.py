def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.
    
    Args:
        name: The name to greet
        
    Returns:
        A greeting string
    """
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """
    Returns the sum of two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b


if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")