refeição = 35
meia = 17.50
lata = 5
suco = 8 
heineken = 15
original = 14
skol = 12
sorvete = 4
caipirinha = 15
agua = 3
agua_gas = 3.5
contador = 0
marmitex = 35
dosepinga = 5
relatorio = 0
nref = 0
nmeia = 0
nagua = 0
nagua_gas = 0
nlata = 0
nsuco = 0
nheinek = 0
noriginal = 0
nskol = 0
nsorvete = 0
ncaipirinha = 0
npinga = 0
nmarmitex = 0

while contador != 2:
    contador = 0
    print('*'*40)
    print(' ')
    print(' 1 - COMEÇAR A CONTAGEM DE VALORES')
    print(' 2 - ENCERRAR O PROGRAMA')
    print(' ')
    print('*'*40)
    print(' ')
    contador = int(input('Seleciona uma das opçôes acima: '))
    if contador == 1:
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print('='*71)
        print("""
 _____ ___  ____  ____  _____ ____  __  __    _    ____  ___    _     |
|_   _/ _ \|  _ \|  _ \| ____/ ___||  \/  |  / \  |  _ \|_ _|  / \    |
  | || | | | |_) | |_) |  _| \___ \| |\/| | / _ \ | |_) || |  / _ \   |
  | || |_| |  _ <|  _ <| |___ ___) | |  | |/ ___ \|  _ < | | / ___ \  |
  |_| \___/|_| \_\_| \_\_____|____/|_|  |_/_/   \_\_| \_\___/_/   \_\ | 
  """)

        print('='*71)
        print(' ')
        print(' ')
    

        qtdn_ref = float(input('RFEIÇÕES = '))
        qtdn_meia = float(input('MEIA = '))
        qtdn_agua = float(input('ÁGUA = '))
        qtdn_agua_gas = float(input('ÁGUA COM GÁS = '))
        qtdn_lata = float(input('LATA = '))
        qtdn_suco = float(input('SUCO = '))
        qtdn_heineken = float(input('HEINEKEN = ')) 
        qtdn_original = float(input('ORIGINAL = '))
        qtdn_skol = float(input('SKOL = '))
        qtdn_sorvete = float(input('SORVETE = '))
        qtdn_caipirinha = float(input('CAIPIRINHA = '))
        qtdn_pinga = float(input('DOSE PINGA = '))
        qtdn_marmitex = float(input('MARMITEX = '))

        soma_ref = qtdn_ref * refeição
        soma_meia = qtdn_meia * meia
        soma_agua = qtdn_agua * agua
        soma_agua_gas = qtdn_agua_gas * agua_gas
        soma_lata = qtdn_lata * lata
        soma_suco = qtdn_suco * suco
        soma_heinek = qtdn_heineken * heineken
        soma_original = qtdn_original * original
        soma_skol = qtdn_skol * skol
        soma_sorvete = qtdn_sorvete * sorvete
        soma_caipirinha = qtdn_caipirinha * caipirinha
        soma_pinga = qtdn_pinga * dosepinga
        soma_marmitex = qtdn_marmitex * marmitex

        valor = (soma_ref + soma_meia + soma_agua + soma_agua_gas + soma_lata + soma_suco + soma_heinek + soma_original + soma_skol + soma_sorvete + soma_caipirinha + soma_pinga + soma_marmitex)
        garçom = (valor * 1.10) - valor
        valorfinal = garçom + valor
        relatorio =  valorfinal + relatorio
        
        nref = qtdn_ref + nref
        nmeia = qtdn_meia + nmeia
        nagua = qtdn_agua + nagua
        nagua_gas = qtdn_agua_gas + nagua_gas
        nlata = qtdn_lata + nlata
        nsuco = qtdn_suco + nsuco
        nheinek = qtdn_heineken + nheinek
        noriginal = qtdn_original + noriginal
        nskol = qtdn_skol + nskol
        nsorvete = qtdn_sorvete + nsorvete
        ncaipirinha = qtdn_caipirinha + ncaipirinha
        npinga = qtdn_pinga + npinga
        nmarmitex = qtdn_marmitex + nmarmitex
        
        print(' ')
        print(' ')
        print(' ')
        print('Valor de comsumo a pagar é de: R${:.2f}'.format(valor))
        print('Valor dos 10% do garçom é de: R${:.2f}'.format(garçom))
        print('Valor total a pagar para o restaurante é de: R${:.2f}'.format(valorfinal))
        print(' ')
        print('='*55)
        print(' ')
        

    else:
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print('Relatorio total do dia de hoje foi: ')
        print(' ')
        print('RFEIÇÕES = ',nref)
        print('MEIA = ',nmeia)
        print('ÁGUA = ',nagua)
        print('ÁGUA COM GÁS = ',nagua_gas)
        print('LATA = ',nlata)
        print('SUCO = ',nsuco)
        print('HEINEKEN = ',nheinek) 
        print('ORIGINAL = ',noriginal)
        print('SKOL = ',nskol)
        print('SORVETE = ',nsorvete)
        print('CAIPIRINHA = ',ncaipirinha)
        print('DOSE PINGA = ',npinga)
        print('MARMITEX = ',nmarmitex)
        print(' ')
        print(' ')
        print('Valor final pago no dia de hoje foi de: R${}'.format(relatorio))

        print('FIM DO PROGRAMA')