def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    if step == 0:
        raise ValueError("step cannot be 0")
    numbers = []
    if step > 0:
        while start < stop:
            numbers.append(start)
            start += step
    else:
        while start > stop:
            numbers.append(start)
            start += step
    return numbers
print(my_range(5))         
print(my_range(2, 7))       
print(my_range(1, 10, 2))   
print(my_range(10, 2, -2))  