import os
import shutil
from datetime import datetime

# --- CONFIGURAÇÕES ---
pasta_destino_pdf = "Documentos_PDF"
pasta_destino_imagens = "Imagens_Organizadas"
arquivo_log = "relatorio_de_automacao.txt"

# Criar pastas se não existirem
if not os.path.exists(pasta_destino_pdf):
    os.makedirs(pasta_destino_pdf)
if not os.path.exists(pasta_destino_imagens):
    os.makedirs(pasta_destino_imagens)

print("Iniciando a Organização de Arquivos da Jessica")

# --- EXECUÇÃO ---
with open(arquivo_log, "a", encoding="utf-8") as log:
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log.write(f"\n=== SESSÃO DE ORGANIZAÇÃO: {agora} ===\n")

    for arquivo in os.listdir("."):
        # Lógica para PDFs
        if arquivo.endswith(".pdf"):
            caminho_final = os.path.join(pasta_destino_pdf, arquivo)
            if not os.path.exists(caminho_final):
                shutil.move(arquivo, pasta_destino_pdf)
                log.write(f"Sucesso: {arquivo} movido para PDFs\n")
                print(f"Movendo PDF: {arquivo}")

        # Lógica para Imagens
        elif arquivo.endswith(".jpg") or arquivo.endswith(".png"):
            caminho_final = os.path.join(pasta_destino_imagens, arquivo)
            if not os.path.exists(caminho_final):
                shutil.move(arquivo, pasta_destino_imagens)
                log.write(f"Sucesso: {arquivo} movido para Imagens\n")
                print(f"Movendo Imagem: {arquivo}")

    log.write("=== FIM DA TAREFA ===\n")

# --- FINALIZAÇÃO ---
print("Tudo pronto! Abrindo o relatório...")
os.startfile(arquivo_log)
