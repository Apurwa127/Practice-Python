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

# text = 'Gates in 2024 Born William Henry Gates IIIOctober 28, 1955 (age 69) Seattle, Washington, U.S.'

# pattern = r'age (\d+)'
# output = re.findall(pattern, text)
# print(output)

# text = """Born	Shahrukh Khan
# 2 November 1965 (age 59)
# New Delhi, India
# Alma mater	Hansraj College (BA)
# Occupations	
# Actorfilm producertelevision personalitybusinessman
# Years active	1988–present
# Organisation(s)	Red Chillies Entertainment
# Knight Riders Group
# Works	Full list
# Spouse	Gauri Khan ​(m. 1991)​
# Children	3, including Aryan and Suhana
# Awards	Full list
# Honours	Padma Shri (2005)
# Order of Arts and Letters (2007)
# Legion of Honour (2014)
# Signature"""

# pattern = r'Born([A-Za-z\s]+)\d'
# pattern2 = r'Born.*\n(.*)\(age'
# pattern3 = r'Born.*\n.*\n(.*)'

# output = re.findall(pattern, text)
# output1 = re.findall(pattern2, text)
# output2 = re.findall(pattern3, text)


# output[0].strip()
# print(output)
# print(output1)
# print(output2)

# def get_pattern_match(pattern, text):
#     matches = re.findall(pattern, text)
#     if matches:
#         return matches[0]
#     else:
#         return None
    
# birth = get_pattern_match(pattern3, text)
# print(birth)

# text = '''Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
# on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
# for tesla related news,
# https://twitter.com/teslarati
# https://twitter.com/dummy_tesla
# https://twitter.com/dummy_2_tesla'''


# pattern = 'https://twitter.com/([a-zA-Z0-9_]+)'

# output = re.findall(pattern, text)


# dict1 = {
#     'elon' : output[0],
#     'arati' : output[1],
#     'dummy' : output[2],
#     'dummy2' : output[3]
# }

# print(dict1)

# text = '''
# Concentration of Risk: Credit Risk
# Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
# restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
# or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
# and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
# hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
# Concentration of Risk: Supply Risk
# We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
# products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
# suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
# '''

# pattern = 'Credit Risk|Supply Risk'

# output = re.findall(pattern, text)

# print(output)


text = '''Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.'''

pattern = 'FY2021(.*)'

matches = re.findall(pattern, text)

companies = {
    'Tesla' : matches[0],
    'BMW' : matches[1]
}

print(companies)

