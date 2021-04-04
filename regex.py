import re

number = "My number is 12341234 and 1233-4548"
pattern = "[0-9]{4,5}[-]*[0-9]{4}"

result = re.findall(pattern, number)
print(result)