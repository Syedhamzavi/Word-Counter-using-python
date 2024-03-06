sentence=input("enter the sentence:")
num_words=len(sentence.split())
num_digits=0
num_uppercase=0
num_lowercase=0
for char in sentence:
    if char.isdigit():
        num_digits+=1
    elif char.isupper():
        num_uppercase+=1
    elif char.islower():
        num_lowercase+=1
print("number of words:",num_words)
print("number of digits:",num_digits)
print("number of uppercase letter:",num_uppercase)
print("number of lowercase letter:",num_lowercase)