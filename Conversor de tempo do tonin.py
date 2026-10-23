moldura = 50

print('Conversor de Tempo do Tonin!'.center(moldura, '-'))
unidade_um_conversao = input('Você quer converter qual unidade?\n' + 'A: Dias\n' + 'B: Horas\n' + 'C: Minutos\n' + 'D: segundos\n' + 'Digite abaixo a letra:\n')
unidade_dois_conversao = input('Você quer converter para qual unidade chefe?\n' + 'A: Dias\n' + 'B: Horas\n' + 'C: Minutos\n' + 'D: segundos\n' + 'Digite abaixo a letra:\n')

# Inicializamos as variáveis com 0 para evitar erros
dias_um = horas_um = minutos_um = segundos_um = 0

# Agora iremos pegar o numero que iremos converter
if unidade_um_conversao == 'A':
    dias_um = int(input('Quantos dias aí chefe?\n'))
elif unidade_um_conversao == 'B':
    horas_um = int(input('Quantas horas aí chefe?\n'))
elif unidade_um_conversao == 'C':
    minutos_um = int(input('Quantos minutos aí chefe?\n'))
elif unidade_um_conversao == 'D':
    segundos_um = int(input('Quantos segundos aí chefe?\n'))

# Variáveis para os dias!
dias_horas = dias_um * 24
dias_minutos = dias_horas * 60
dias_segundos = dias_minutos * 60

# Variáveis para as horas!
horas_dias = horas_um / 24
horas_minutos = horas_um * 60
horas_segundos = horas_minutos * 60

# Variáveis para os minutos!
minutos_dias = (minutos_um / 60) / 24
minutos_horas = minutos_um / 60
minutos_segundos = minutos_um * 60

# Variáveis para os segundos!
segundos_dias = ((segundos_um / 60) / 60) / 24
segundos_horas = (segundos_um / 60) / 60
segundos_minutos = segundos_um / 60

# Agora iremos converter os dias
if unidade_um_conversao == 'A' and unidade_dois_conversao == 'A':
    print('Tá convertendo de dias para dias mané! Tenta de novo!')
elif unidade_um_conversao == 'A' and unidade_dois_conversao == 'B':
    if dias_horas >= 100:
        print(f'Você tem {dias_horas} horas! Quantas horas!')
    else:
        print(f'Você tem {dias_horas} Horas! Nossa! Poucas horas!')

elif unidade_um_conversao == 'A' and unidade_dois_conversao == 'C':
    if dias_minutos >= 100:
        print(f'Você tem {dias_minutos} minutos! Quantos minutos!')
    else:
        print(f'Você tem {dias_minutos} minutos! Nossa! Poucos minutos!')

elif unidade_um_conversao == 'A' and unidade_dois_conversao == 'D':
    if dias_segundos >= 100:
        print(f'Você tem {dias_segundos} segundos! Quantos segundos!')
    else:
        print(f'Você tem {dias_segundos} segundos! Nossa! Poucos segundos!')
       
# Agora as horas:
elif unidade_um_conversao == 'B' and unidade_dois_conversao == 'B':
    print('Tá convertendo de horas para horas mané! Tenta de novo!')
elif unidade_um_conversao == 'B' and unidade_dois_conversao == 'A':
    if horas_dias >= 100:
        print(f'Você tem {horas_dias} dias! Quantos dias!')
    else:
        print(f'Você tem {horas_dias} dias! Nossa! Poucos dias!')

elif unidade_um_conversao == 'B' and unidade_dois_conversao == 'C':
    if horas_minutos >= 100:
        print(f'Você tem {horas_minutos} minutos! Quantos minutos!')
    else:
        print(f'Você tem {horas_minutos} minutos! Nossa! Poucos minutos!')

elif unidade_um_conversao == 'B' and unidade_dois_conversao == 'D':
    if horas_segundos >= 100:
        print(f'Você tem {horas_segundos} segundos! Quantos segundos!')
    else:
        print(f'Você tem {horas_segundos} segundos! Nossa! Poucos segundos!')

# Agora os minutos!
elif unidade_um_conversao == 'C' and unidade_dois_conversao == 'C':
    print('Tá convertendo de minutos para minutos mané! Tenta de novo!')
elif unidade_um_conversao == 'C' and unidade_dois_conversao == 'A':
    if minutos_dias >= 100:
        print(f'Você tem {minutos_dias} dias! Quantos dias!')
    else:
        print(f'Você tem {minutos_dias} dias! Nossa! Poucos dias!')

elif unidade_um_conversao == 'C' and unidade_dois_conversao == 'B':
    if minutos_horas >= 100:
        print(f'Você tem {minutos_horas} horas! Quantas horas!')
    else:
        print(f'Você tem {minutos_horas} horas! Nossa! Poucas horas!')

elif unidade_um_conversao == 'C' and unidade_dois_conversao == 'D':
    if minutos_segundos >= 100:
        print(f'Você tem {minutos_segundos} segundos! Quantos segundos!')
    else:
        print(f'Você tem {minutos_segundos} segundos! Nossa! Poucos segundos!') 

# Agora os segundos!
elif unidade_um_conversao == 'D' and unidade_dois_conversao == 'D':
    print('Tá convertendo de segundos para segundos mané! Tenta de novo!')
elif unidade_um_conversao == 'D' and unidade_dois_conversao == 'A':
    if segundos_dias >= 100:
        print(f'Você tem {segundos_dias} dias! Quantos dias!')
    else:
        print(f'Você tem {segundos_dias} dias! Nossa! Poucos dias!')

elif unidade_um_conversao == 'D' and unidade_dois_conversao == 'B':
    if segundos_horas >= 100:
        print(f'Você tem {segundos_horas} horas! Quantas horas!')
    else:
        print(f'Você tem {segundos_horas} horas! Nossa! Poucas horas!')

elif unidade_um_conversao == 'D' and unidade_dois_conversao == 'C':
    if segundos_minutos >= 100:
        print(f'Você tem {segundos_minutos} minutos! Quantos minutos!')
    else:
        print(f'Você tem {segundos_minutos} minutos! Nossa! Poucos minutos!')

