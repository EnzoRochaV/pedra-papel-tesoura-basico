import random as rd

escolha = input('Escolha entre pedra, papel ou tesoura!! ')

print("Vc escolheu ", escolha)

pe = "pedra"

pa = "papel"

t = "tesoura"

lista = [pe, pa, t]

resposta_maquina = rd.choice(lista)

print("Maquina escolheu ", resposta_maquina)

def jogo(escolha, resposta_maquina) :
    if escolha == resposta_maquina :
        print("empate")
    elif escolha == pe :
        if resposta_maquina == pa :
            print("perdeu")
        else:
            print("Ganhou")
    elif escolha == pa :
        if resposta_maquina == pe :
            print("ganhou")            
        else:
            print("perdeu")    
    elif escolha == t :
        if resposta_maquina == pa :
            print("ganhou")        
        else :
            print("perdeu")    
            
resultado = jogo(escolha, resposta_maquina)
