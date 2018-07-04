def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# Running result:
# [1, 2, 3, 'Hello']