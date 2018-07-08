def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')

spam()

# Running result:
# Traceback (most recent call last):
#   File "029_errExample.py", line 6, in <module>
#     spam()
#   File "029_errExample.py", line 2, in spam
#     bacon()
#   File "029_errExample.py", line 4, in bacon
#     raise Exception('This is the error message.')
# Exception: This is the error message.