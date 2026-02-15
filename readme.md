# Arnaldo: Assistente de Voz em Python 🎙️

Este é um assistente virtual simples desenvolvido durante meu bootcamp, capaz de reconhecer comandos de voz em português para automatizar tarefas básicas no Windows.

## ✨ Funcionalidades
* **Ativação por Nome:** Responde apenas quando chamado por "Arnaldo".
* **Pesquisa na Web:** Abre o navegador e realiza buscas automáticas no Google.
* **Acesso Rápido:** Atalhos de voz para YouTube e Redes Sociais.
* **Utilitários:** Abre o Bloco de Notas e informa a hora atual.
* **Lógica de Sorteio:** Função "Cara ou Coroa" para decisões rápidas.

## 🚀 Tecnologias Utilizadas
* [Python 3.13+](https://www.python.org/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - Para transformar áudio em texto.
* [PyAudio](https://pypi.org/project/PyAudio/) - Para capturar o som do microfone.
* [Webbrowser & OS](https://docs.python.org/3/library/) - Bibliotecas nativas para controle do sistema.

## 🛠️ Como instalar
1. Clone o repositório:
   ```bas
   Instale as bibliotecas necessárias:

Bash
pip install SpeechRecognition pyaudio
Execute o programa:

Bash
python assistente.py
🎤 Comandos Principais
"Arnaldo, que horas são?"

"Arnaldo, pesquise [assunto]"

"Arnaldo, abrir bloco de notas"

"Arnaldo, youtube"


---

## 2. O arquivo `.gitignore` (Muito Importante!)
Para o seu projeto ficar limpo no GitHub, crie um arquivo chamado `.gitignore` e escreva apenas isso dentro dele:
```text
__pycache__/
*.pyc
.venv/
Isso evita que arquivos temporários do Python que só funcionam no seu PC sejam enviados para a internet.

3. Descrição do Repositório (About)
No campo de descrição do GitHub, use algo curto e chamativo:

"Assistente virtual com reconhecimento de voz em Python que automatiza buscas no Google e abertura de programas nativos. 🚀"
   git clone [https://github.com/seu-usuario/arnaldo-assistente.git](https://github.com/seu-usuario/arnaldo-assistente.git)
