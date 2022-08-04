- **Please note:** read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)
before starting.

Create a custom context manager:

In this task you should implement your own `CleanUpFile` context manager as a class.
It should remove the file if it exists after exiting.

Its constructor should take only the filename parameter. 
Also CleanUpFile must have __enter__ and __exit__ methods.

Example:
```python
with CleanUpFile(“file.txt”):
    with open(“file.txt”, “w”) as file:
        file.write(“Hello Mate!”)
```

# after it file "file.txt" should not exist
