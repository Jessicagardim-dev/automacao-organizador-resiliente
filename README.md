# 🤖 Organizador de Arquivos Inteligente (RPA)

Este é um robô de automação (RPA) desenvolvido em **Python** para organizar pastas de forma eficiente, segura e resiliente. 

## 🚀 O que este robô faz?
O script monitora uma pasta específica e move arquivos para diretórios organizados com base em suas extensões (PDFs, Imagens, etc.).

## 🛠️ Diferenciais deste Projeto (Nível Júnior)
Diferente de scripts simples, este projeto foi construído com foco em **boas práticas de automação**:

* **Resiliência (Travas de Segurança):** O robô verifica se o arquivo já existe no destino antes de mover, evitando erros de sistema e perda de dados em caso de interrupção (ex: queda de energia ou internet).
* **Relatórios Automáticos (Logs):** Gera um arquivo `.txt` com o histórico detalhado de cada ação (data, hora e status), permitindo auditoria do trabalho realizado.
* **Interface Limpa:** O robô trabalha silenciosamente em segundo plano e apresenta apenas um único relatório consolidado ao final da execução.

## 💻 Tecnologias Utilizadas
* **Python 3.x**
* Biblioteca `os` (Manipulação de sistema)
* Biblioteca `shutil` (Movimentação de arquivos)
* Biblioteca `datetime` (Registro de logs temporais)

---
### 👩‍💻 Desenvolvido por:
**Jessica Gardim** *Especialista em Automação e RPA | Desenvolvedora Python*+



