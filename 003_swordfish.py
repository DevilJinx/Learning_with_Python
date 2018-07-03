while True:
    print('Who are you?')
    name = input()
    if name != 'Devil Jinx':
        continue
    print('Hello, Devil Jinx. What is the password?(It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

# Running result:
# Who are you?
# a
# Who are you?
# Devil Jinx
# Hello, Devil Jinx. What is the password?(It is a fish)
# sdw
# Who are you?
# Devil Jinx
# Hello, Devil Jinx. What is the password?(It is a fish)
# swordfish
# Access granted.