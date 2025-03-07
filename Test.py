import re

chat1 = 'codebasics: you ask lot of questions 12345678912, abc@xyz.com'
chat2 = 'codebasics: here it is: (123)-567-8912,1234567891,123-456-7891 abx@xyz.com'
chat3 = 'codebasics: yes, phone: 12345678912 email: abx@xyz.com'


pattern = r'\(\d{3}\)-\d{3}-\d{4}|\d{10}|\d{3}-\d{3}-\d{4}'
pattern2 = r'[a-z0-9A-Z_]*@[a-z]*\.[a-z]*'
output = re.findall(pattern, chat2)
output2 = re.findall(pattern2, chat3)
print(output)
print(output2)