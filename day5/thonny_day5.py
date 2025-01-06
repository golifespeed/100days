import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','#','$','%','^','&','*','(',')','_','+','-'] 
numbers = ['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the PyPassword Generator!")

user_letters=input("How many letters would you like in your password?\n")
letter_list=random.choices(letters,weights=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], k=int(user_letters))
print(letter_list)

user_symbols=input("How many symbols would you like in your password?\n")
symbol_list=random.choices(symbols,weights=[1,1,1,1,1,1,1,1,1,1,1,1], k=int(user_symbols))
print(symbol_list)

user_numbers=input("How many numbers would you like in your password?\n")
number_list=random.choices(numbers, weights=[1,1,1,1,1,1,1,1,1,1], k=int(user_numbers))
print(number_list)

final_list=letter_list+symbol_list+number_list
print(final_list)

random.shuffle(final_list)
print(final_list)
length=len(final_list)
count=0
password=str()
for char in final_list:
    if count<length:
        password=str(final_list[count])+str(password)
        count+=1
print(password)