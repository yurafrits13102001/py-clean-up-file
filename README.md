- **Please note:** read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)
before starting.
- Implement the task described [here](app/main.py)

Create a custom context manager:

In this task you should implement your own CleanUpFile context manager as a class. 
It should remove the file if it exists after exiting it.

Its constructor should take only the filename parameter. 
Also CleanUpFile must have __enter__ (returns itself) and __exit__ (deletes a file if it exists) methods.

Example:
```
with open(“file.txt”, “w”) as file:
    with CleanUpFile(“file.txt”):
        file.write(“Hello Mate!”)
```
