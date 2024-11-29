# Projeto A3 - Antivírus
# Participantes: Lucas Frozza Ramos, Lucas Alberto de Moraes Luiz, Vinicius Berbert de Lima, Luan Henrique dos Santos Servidone

import os

def obter_virus():
    return os.getcwd()

def buscar_virus(diretorio):
    arquivos_encontrados = []
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if arquivo.lower().endswith((".bat", ".exe")):
                arquivos_encontrados.append(os.path.join(raiz, arquivo))
                print(f"Arquivo encontrado no seguinte caminho: {os.path.join(raiz, arquivo)}")
    return arquivos_encontrados

def gerar_relatorio(arquivos):
    caminhodownloads = os.path.join(os.path.expanduser("~"), "Downloads")
    caminho_relatorio = os.path.join(caminhodownloads, "relatorioa3.txt")

    with open(caminho_relatorio, 'w') as relatorio:
        for arquivo in arquivos:
            relatorio.write(arquivo + '\n')
    print(f"Um relatório com os arquivos maliciosos de sua máquina foi salvo em: {caminho_relatorio}")

if _name_ == "_main_":
    diretorio_base = obter_virus()
    print(f"Faremos a busca de todos os arquivos maliciosos em sua máquina, seguindo conforme o caminho: {diretorio_base}")
    input("Pressione a tecla Enter para iniciar a busca por arquivos maliciosos em sua máquina.")

    arquivos_maliciosos = buscar_virus(diretorio_base)

    if arquivos_maliciosos:
        print(f"Foram encontrados {len(arquivos_maliciosos)} arquivos maliciosos em sua máquina.")
        gerar_relatorio(arquivos_maliciosos)
    else:
        print("Nenhum arquivo malicioso foi encontrado, você está limpo.")