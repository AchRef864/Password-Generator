import string
from random import *
length = int(input("HOW long do you want your password?: "))
while True:
  try:
    special = input("Contains special letters?(Y/N): ")
    if special in ['Y','y','N','n']:
      break
    print("Invalid answer")
  except Exception as e:
    print(e)
password=''
PwD1 = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
PwD2 = string.ascii_lowercase+string.ascii_uppercase+string.digits
if(special == 'Y'):
    for i in range(length):
        password+=PwD1[randint(1,len(PwD1))]
else:
    for i in range(length):
        password+=PwD2[randint(1,len(PwD2))]
print(password)