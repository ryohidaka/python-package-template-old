class PythonPackageTemplate:
    def __init__(self):
        """
        Initializes a new instance of the PythonPackageTemplate class.
        Sets the initial value of the counter to 0.
        """
        self.counter = 0

    def add_numbers(self, a, b):
        """
        Adds two numbers and increments the counter.

        Parameters:
        - a (int): The first number.
        - b (int): The second number.

        Returns:
        int: The sum of the two numbers.
        """
        result = a + b
        self.counter += 1
        return result
