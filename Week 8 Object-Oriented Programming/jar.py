# Defne a class Jar with initial capacity = 12
class Jar:
    # Initialize the cookie Jar
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("You need to a have a pozitive capacity! ")
        self._size = 0

    # Return the number of cookies as a str
    def __str__(self):
        return  "🍪" * self._size

    # Define a method that adds cookies in the jar
    def deposit(self, n):
        if n <= (self.capacity - self._size):
            self._size = self._size + n
        else:
            raise ValueError("Not enough space in the jar! ")

    # Define a method that takes cookies from the jar
    def withdraw(self, n):
        if n <= self._size:
            self._size = self._size - n
        else:
            raise ValueError("Not enough cookies in the jar! ")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():

    jar = Jar()
    print(jar)

if __name__ == "__main__":
    main()
