import subprocess

def executar_comando(comando):
    print("f\n[+] Executando: {comando}")
    # O subprocess roda o comando no seu temrinal e pega o resultado
    resultado = subprocess.check_output(comando, shell=True, text=True)
    return resultado

print("---FERRAMENTA DE RECONHECUMENTO DE AD (SIMULAÇÃO) ---")

try:
    # 1. Tenta listar os usuários do domínio
    # Nota: Isso só funciona 100% se você estier em uma máquina ligada a um domínio
    usuarios = executar_comando("net user")
    print(usuarios)

    # 2. Tenta ver informações da rede
    config_rede = executar_comando("ipconfig \all")
    print(config_rede)

exept Exception as e:
   print(f"[-] Erro: Você provavelmente não esta em um ambiente de domínio AD no momento.")
   print(f"[-] Detalhes: {e}")