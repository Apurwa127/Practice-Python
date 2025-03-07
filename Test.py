import re

# chat1 = 'codebasics: you ask lot of questions 12345678912, abc@xyz.com'
# chat2 = 'codebasics: here it is: (123)-567-8912,1234567891,123-456-7891 abx@xyz.com'
# chat3 = 'codebasics: yes, phone: 12345678912 email: abx@xyz.com'


# pattern = r'\(\d{3}\)-\d{3}-\d{4}|\d{10}|\d{3}-\d{3}-\d{4}'
# pattern2 = r'[a-z0-9A-Z_]*@[a-z]*\.[a-z]*'
# output = re.findall(pattern, chat2)
# output2 = re.findall(pattern2, chat3)
# print(output)
# print(output2)

# chat1 = 'codebasics: Hello, I am having an issue with my order # 412889912'
# chat2='codebasics: I have a problem with my order number 412889912'
# chat3='codebasics: My order 412889912 is having an issue, I was charged 300$ when online it says 280$'

# pattern = r'order[^\d]*(\d*)'
# output = re.findall(pattern, chat1)
# print(output)

text = 'Gates in 2024 Born William Henry Gates IIIOctober 28, 1955 (age 69) Seattle, Washington, U.S.'

pattern = r'age (\d+)'
output = re.findall(pattern, text)
print(output)