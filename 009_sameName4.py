def spam():
    print(eggs)  # ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()

# Running:
# Traceback (most recent call last):
#   File "./009_sameName4.py", line 6, in <module>
#     spam()
#   File "./009_sameName4.py", line 2, in spam
#     print(eggs)  # ERROR!
# UnboundLocalError: local variable 'eggs' referenced before assignment