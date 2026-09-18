opcoes = []
votos = []

def cadastrar_opçao(opcoes, votos):
  opcao = input("Digite a opção que deseja cadastrar: ")
  if opcao in opcoes:
    print("Opção já cadastrada.")
  else:
    opcoes.append(opcao)
    votos.append(0)
    print("Opção cadastrada com sucesso.")

def listar_opcoes():
    for i in opcoes:
        print(i)

def registrar_voto(opcoes, votos):
  listar_opcoes()
  opcao = input("Digite a opção que deseja votar: ")
  if opcao in opcoes:
    voto = opcoes.index(opcao)
    votos[voto] += 1
    print("Voto registrado com sucesso.")
  else:
    print("Opção inválida.")

def consultar_votos(opcoes, votos):
  opcao = input("Digite a opção que deseja consultar os votos: ")
  if opcao in opcoes:
    voto = opcoes.index(opcao)
    print(f"A opção '{opcao}' possui {votos[voto]} votos.")
  else:
    print("Opção inválida.")

def mostrar_resultado(opcoes, votos):
  total_votos = sum(votos)

  if total_votos == 0:
    print("Nenhum voto registrado.")
    return
  for i in range(len(opcoes)):
     percentual_votos = votos[i]/total_votos * 100
     print(f"{opcoes[i]} - {percentual_votos:.2f}% - {votos[i]} votos")
def mostrar_vencedora(opcoes, votos):
  total_votos = sum(votos)
  vencedora = []
  if len(opcoes) == 0:
     print("Nehuma opção cadastrada.")
     return
  if total_votos == 0:
    print("Nenhum voto registrado.")
    return
  for i in range(len(opcoes)):
    if votos[i] == max(votos):
      vencedora.append(opcoes[i])
  if len(vencedora) == 1:
    print(f"A opção vencedora é: {vencedora[0]}")
  else:
    print("Houve um empate entre as opções: ")
    for i in vencedora:
      print(i)
def menu():
  while True:
      print("1. Cadastrar opção")
      print("2. Listar opções")
      print("3. Registrar voto")
      print("4. Consultar votos")
      print("5. Mostrar resultado")
      print("6. Mostrar vencedora")
      print("7. Sair")
      escolha = input("Escolha uma opção (1-7): ")
      if escolha == '1':
          cadastrar_opçao(opcoes, votos)
      elif escolha == '2':
          listar_opcoes()
      elif escolha == '3':
          registrar_voto(opcoes, votos)
      elif escolha == '4':
          consultar_votos(opcoes, votos)
      elif escolha == '5':
          mostrar_resultado(opcoes, votos)
      elif escolha == '6':
          mostrar_vencedora(opcoes, votos)
      elif escolha == '7':
          break
      else:
          print("Opção inválida. Tente novamente.")

menu()
