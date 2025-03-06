import re

chat1 = 'codebasics: you ask lot of questions 12345678912, abc@xyz.com'
chat2 = 'codebasics: here it is: (123)-567-8912,1234567891, abx@xyz.com'
chat3 = 'codebasics: yes, phone: 12345678912 email: abx@xyz.com'

pattern = '\d{10}| \(\d{3}\)-\d{3}-\d{4}'
matches = re.findall(pattern, chat2)
print(matches)