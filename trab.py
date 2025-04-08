import os  

def validar_nome(nome):
    if not nome.strip():
        raise ValueError("O nome não pode estar vazio.")
    if any(char.isdigit() for char in nome):
        raise ValueError("O nome não pode conter números.")
    return nome.strip()

def validar_matricula(matricula):
    if not matricula.isdigit():
        raise ValueError("O número de matrícula deve conter apenas números.")
    return matricula

def validar_telefone(telefone):
    if not telefone.isdigit() or len(telefone) < 9:
        raise ValueError("O telefone deve conter apenas números e ter pelo menos 9 dígitos.")
    return telefone

def escrever_arquivo(nome_arquivo, conteudo):
    try:
        with open(nome_arquivo, 'a') as f:  
            f.write(conteudo + "\n")
    except IOError:
        print("Erro: Não foi possível escrever no arquivo.")

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("Erro: O arquivo não existe.")
    except IOError:
        print("Erro ao tentar ler o arquivo.")

def obter_dado(mensagem, funcao_validacao):
    while True:
        try:
            entrada = input(mensagem)
            return funcao_validacao(entrada)
        except ValueError as e:
            print(f"Entrada inválida: {e}. Tente novamente.")

def main():
    try:
        nome = obter_dado("Digite o nome do aluno: ", validar_nome)
        matricula = obter_dado("Digite o número de matrícula: ", validar_matricula)
        telefone = obter_dado("Digite o telefone do aluno: ", validar_telefone)

        conteudo = f"Nome: {nome}\nMatrícula: {matricula}\nTelefone: {telefone}"
        escrever_arquivo("aluno.txt", conteudo)

        print("Dados gravados com sucesso!")
        print("Lendo arquivo salvo:")
        print(ler_arquivo("aluno.txt"))

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()