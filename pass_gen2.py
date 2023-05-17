
import random
import string
import os
os.system('clear')
f = open("output of pass gen.txt", "w")

ref_list = ["uppercase letters", "lowercase letters", "digits", "symbols"]
def type_of_char(i):
    ap= input(f" Do you want {i} be included in the password: (Y/N) :")
    return ap.lower() == "y" or ap==""
    
def welcome():
    n = input("How many characters do you want as a length of your pass: ")
    while not n.isdigit():
        n = input(" Please enter numbers!\nHow many characters as a lenth of your pass: ")
    wish_list = list(filter(type_of_char, ref_list))
    return int(n), wish_list

def pass_gen(list):
    choose_from = []
    if "uppercase letters" in list :
        choose_from.append(random.choice(string.ascii_uppercase))
    if "lowercase letters" in list : 
        choose_from.append(random.choice(string.ascii_lowercase))
    if "digits" in list : 
        choose_from.append(random.choice(string.digits))
    if "symbols" in list:
        choose_from.append(random.choice(string.punctuation))
    return choose_from


while True:
    os.system('clear')
    pas_length , list_of_type = welcome()
    while True:
        your_pass=""
        for i in range(pas_length):
            your_pass = your_pass + (random.choice(pass_gen(list_of_type)))
        print()
        print(f"Your generated random password is \n \n {your_pass}")
        print()
        q1 = input(" If you want to generate another pass with these features and length press Y otherwise any key: ")
        if q1.lower() != "y" and q1!="" :
            break
        print()
        print(30*"**")
    print()
    q2 = input("If you want to update the terms of pass features press ((u or U))  or for exit generator any other key: ")
    if q2.lower() != "u" and q2!="":
        print ("\nOK. THANKS FOR USING PASSGENERATOR.")
        print()
        f.write(f"The generated pass is {your_pass} ")
        break
    print(30*"*=")

