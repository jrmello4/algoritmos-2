def cadastrar_opçao(opcoes):
  nome = input("Digite o nome da nova opção: ")
  if nome == "":
    return "A opcao nao deve ser vazia!"
  for opcao in opcoes:
    if opcao["nome"] == nome:
      return "Essa opção já está cadastrada."
  opcoes.append({"nome": nome, "votos": 0})
  print(f"Opção '{nome}' cadastrada com sucesso!")

