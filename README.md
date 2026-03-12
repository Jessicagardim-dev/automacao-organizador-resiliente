# 🤖 Robô Organizador de Arquivos Resiliente

Este projeto é uma automação em Python desenvolvida para organizar diretórios de forma inteligente e resiliente, movendo arquivos para pastas específicas com base nas suas extensões (PDFs e Imagens).

## 🚀 Funcionalidades
- **Organização Automática:** Identifica e move arquivos `.pdf`, `.jpg`, `.png` e `.jpeg`.
- **Resiliência (Error Handling):** Utiliza blocos `try/except` para garantir que o robô não pare de funcionar caso encontre arquivos abertos ou sem permissão de acesso.
- **Sistema de Logs:** Gera um relatório detalhado (`relatorio_de_automacao.txt`) de cada execução, permitindo a auditoria do processo.
- **Nomes Padronizados:** Estrutura de pastas criada automaticamente pelo script.

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **Biblioteca OS:** Manipulação de caminhos e diretórios.
- **Biblioteca Shutil:** Movimentação segura de ficheiros.
- **Biblioteca Datetime:** Timestamp para os relatórios de execução.

## 📁 Como utilizar
1. Coloque o ficheiro `organizador.py` na pasta que deseja organizar.
2. Execute o script.
3. Verifique o ficheiro de log gerado para confirmar as movimentações.

---
Desenvolvido por [Jessica Gardim](https://github.com/Jessicagardim-dev) 🚀



