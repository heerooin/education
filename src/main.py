def qwer(func):
    def is_float(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return  result
    return  is_float



@qwer
def float(x):
    return round(x)

x = float(2.67)

# def printing(function):
#     def inner(*args, **kwargs):
#         result = function(*args, **kwargs)
#         print('result =', result)
#         return result
#     return inner
#
# @printing
# def add_one(x):
#     return x + 1
#
# y = add_one(10)
# print(y)