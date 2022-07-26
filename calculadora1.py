#!/usr/bin/env python
# coding: utf-8

# In[5]:


print("1 Adição")
print ("2 Subtração")
print ("3 Multiplicação")
print ("4 Divisão")

choice = input("Enter your choice: ")

num1 = float(input("Digite Número 1: "))
num2 = float(input("Digite Número 2: "))

if choice == "1":
    print(num1, "+", num2, "=", (num1+num2))
    
elif choice == "2"
    print(num1, "+", num2, "=", (num1-num2))
    
elif choice == "3"
    print(num1, "*", num2, "=", (num1*num2))
    
elif choice == "4"
    if num2 == 0.0:
        print("Erro ao dividir por 0")
    else:
         print(num1, "/", num2, "=", (num1/num2))
            
else:
    print("Escolha inválida.")


# In[ ]:




