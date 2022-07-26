#!/usr/bin/env python
# coding: utf-8

# In[4]:


def calculadora():
    
    #Início do programa.
    print('As possibilidades de operações presentes são: 1. soma; 2. subtração; 3. multiplicação; 4. divisão.')
    
    print('Digite o primeiro número')
    num1 = int(input())
    print('Digite o segundo número')
    num2 = int(input())
    print('Qual a operação que você deseja realizar?')
    op = int(input())
    
    if (op == 1):
        res = num1 + num2
    elif (op == 2):
        res = num1 - num2
    elif (op == 3):
        res = num1 * num2;
    elif (op == 4):
        res = num1/num2
    else:
        print('Essa opção não existe')
        calculadora(8, 5, 4)
    print('O resultado da sua operação é', res)


# In[ ]:





# In[ ]:




