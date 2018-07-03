def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# Running result:
# 21.0
# 3.5
# Traceback (most recent call last):
#   File "010_zeroDivide.py", line 6, in <module>
#     print(spam(0))
#   File "010_zeroDivide.py", line 2, in spam
#     return 42 / divideBy
# ZeroDivisionError: division by zero