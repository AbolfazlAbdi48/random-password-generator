# moduls
import random
# list of characters
characters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~123456879qwertyuioplkjhgfdsazxcvbnmASDFGHJKLMNBVCXQWERTYUIOP"
# number of digits
n = int(input('Enter the number of digits: '))
# random password
randomPassword = "".join(random.sample(characters,n))
# random password print
print(randomPassword)