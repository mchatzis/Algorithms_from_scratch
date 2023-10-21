Sure, here is a coding exercise related to "Unpacking a Sequence into Separate Variables" in Python:

### Exercise:

1. Create a list of tuples where each tuple contains the name, age, and favorite color of a person. The list should contain at least 5 tuples. The format of the tuples should be `(name, age, color)`. 

2. Write a Python program to unpack the tuples into three separate lists - `names`, `ages` and `colors`.

Example:

```python
persons = [("John", 25, "Blue"), ("Sarah", 28, "Red"), ("Tom", 31, "Green"), ("Amy", 27, "Black"), ("Anna", 30, "White")]
```

Your program should be able to unpack this `persons` list into three separate lists like below:

```python
names = ["John", "Sarah", "Tom", "Amy", "Anna"]
ages = [25, 28, 31, 27, 30]
colors = ["Blue", "Red", "Green", "Black", "White"]
```

This task is designed to help you understand how to unpack a sequence (in this case, a list of tuples) into separate variables (in this case, lists). The number of variables you're unpacking into should match the structure of the sequence elements.