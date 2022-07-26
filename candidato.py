candX, candY, candZ, bran = 0, 0, 0, 0
while True:
    try:
        voto = int(input('Escolha o candidato que desejas votar: \nCandidato X: 889\nCandidato Y: 857\nCandidato Z: 515\nBranco: 0 \n'))
        if voto == 889:
            candX+=1
        elif voto == 857:
            candY+=1
        elif voto == 515:
            candZ+=1
        elif voto == 0:
            bran+=1
        else:
            bran+=1
         op = input('Concluir a votação? (S/N)')
         if op.upper() == 'S':
             break
    except:
        print('Erro! Apenas números são válidos. Favor, tente novamente.')