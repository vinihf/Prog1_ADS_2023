agenda = {}
while True:
    cpf = input("CPF:")
    nome = input("Nome:")
    idade = input("Idade:")
    telefone = input("Telefone:")
    dados = {"nome":nome,"idade":idade,"telefone":telefone}
    agenda[cpf] = dados
    continuar = input("Quer inserir mais? (S/N)")
    if continuar == "N":
        break

print(agenda)
'''

chaves = agenda.keys()
for chave in chaves:
    print(f"{chave} {agenda[chave]['nome']} - {agenda[chave]['idade']}({agenda[chave]['telefone']})")

'''