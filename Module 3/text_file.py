# .txt text file

# with open('massage.txt', 'w') as file:
#     file.write('Hello World')

# with open('massage.txt', 'a') as file:
#     file.write('Hello World\n')

with open('massage.txt', 'r') as file:
    text = file.read()
    print(text)

