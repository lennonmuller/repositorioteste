# despesas mensais

carteira = []

print("-------------")
print("@ carteira")
print("-------------")
print("Adicionar Receita: ")
print("Adicionar despesas: ")

def adicionar_transacao():
    nome = input("Nome: ")
    valor = float( input("Valor: ") )
    carteira.append({
        "nome": nome,
        "valor": valor
    })

while True:

    opcao = int( input("Digite a opcao: "))

    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()
    elif opcao == 3:
        adicionar_transacao()
    elif opcao == 4:
        adicionar_transacao()
    else:
        break

#nota fiscal
total = 0
for fc in carteira:
    print("Carteira:", fc['nome'], "Valor: $", fc['valor'])
    total = total + fc['valor']

print("Saldo atual: $", total)