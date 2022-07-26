def idadef():
    
    try:
        nome = input('Digite o seu nome: ')
        ano_atual = int(input('Digite o ano atual: '))
        ano_nascimento = int(input('Digite o seu ano de nascimento: '))
        
        idade = ano_atual - ano_nascimento
        
        if(ano_atual < 2022 and ano_nascimento > 1922):
            print('Olá', nome, 'você tem (ou vai fazer)', idade)
        else:
            print('Erro!')
            idadef()
        
    except:
            print('Você não digitou números.')
            idadef()
        
    idadef()