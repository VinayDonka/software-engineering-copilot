```python
def even_numbers():
    """
    This function returns a list of even numbers from 1 to 10.
    """
    even_nums = []
    for i in range(1, 11):
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums

result = even_numbers()
print(result)
```