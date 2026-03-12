import os
import shutil
from datetime import datetime

# --- PASTAS DE DESTINO ---
pasta_pdf = "Documentos_PDF"
pasta_imagens = "Imagens_Organizadas"
arquivo_log = "relatorio_de_automacao.txt"

# Criar as pastas se elas ainda não existirem
if not os.path.exists(pasta_pdf):
    os.makedirs(pasta_pdf)
if not os.path.exists(pasta_imagens):
    os.makedirs(pasta_imagens)

print("Iniciando a Organização de Arquivos...")

# --- EXECUÇÃO ---
with open(arquivo_log, "a", encoding="utf-8") as log:
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log.write(f"\n=== SESSÃO: {agora} ===\n")

    # Olhar cada arquivo na pasta onde o script está
    for arquivo in os.listdir("."):
        
        # Ignorar o próprio script e o log para não dar erro
        if arquivo == "organizador.py" or arquivo == arquivo_log:
            continue

        try:
            # Lógica para arquivos PDF
            if arquivo.lower().endswith(".pdf"):
                shutil.move(arquivo, pasta_pdf)
                log.write(f"Sucesso: {arquivo} movido para PDFs\n")
                print(f"Movido: {arquivo}")

            # Lógica para arquivos de Imagem
            elif arquivo.lower().endswith((".jpg", ".png", ".jpeg")):
                shutil.move(arquivo, pasta_imagens)
                log.write(f"Sucesso: {arquivo} movido para Imagens\n")
                print(f"Movido: {arquivo}")
        
        except:
            # Se der erro (ex: arquivo aberto), ele avisa no log e pula pro próximo
            log.write(f"Erro: Não foi possível mover o arquivo {arquivo}\n")
            print(f"Aviso: O arquivo {arquivo} está em uso e foi pulado.")

    log.write("=== FIM DA TAREFA ===\n")

print("Tudo pronto! O relatório foi atualizado.")
# Abrir o log automaticamente para você ver o resultado
os.startfile(arquivo_log)
