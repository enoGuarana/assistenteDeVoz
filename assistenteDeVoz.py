import speech_recognition as sr
import os
import webbrowser
from datetime import datetime

# Nome simplificado para facilitar o reconhecimento
NOME_ASSISTENTE = "arnaldo" 

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print(f">>> {NOME_ASSISTENTE.upper()} está ouvindo...")
        audio = microfone.listen(source)

    try:
        # Pega o que você falou e transforma em letras minúsculas
        frase = microfone.recognize_google(audio, language='pt-BR').lower()
        print(f"Você disse: '{frase}'")

        # Verifica se a primeira palavra que você disse foi "Arnaldo"
        if frase.startswith(NOME_ASSISTENTE):
            
            # Remove a palavra "arnaldo" da frase para isolar o comando
            comando = frase.replace(NOME_ASSISTENTE, "").strip()
            print(f"Comando para processar: '{comando}'")

            # 1. Comando: Abrir YouTube
            if "youtube" in comando:
                print("Arnaldo: Abrindo o YouTube...")
                webbrowser.open("https://www.youtube.com")

            # 2. Comando: Pesquisa no Google
            elif "pesquise" in comando or "pesquisar" in comando:
                # Remove a palavra "pesquise" e busca o resto
                termo = comando.replace("pesquise", "").replace("pesquisar", "").strip()
                print(f"Arnaldo: Pesquisando '{termo}' no Google...")
                webbrowser.open(f"https://www.google.com/search?q={termo}")

            # 3. Comando: Abrir Bloco de Notas
            elif "anotar" in comando or "bloco de notas" in comando:
                print("Arnaldo: Abrindo Bloco de Notas.")
                os.system("notepad.exe")

            # 4. Comando: Horas
            elif "horas" in comando:
                agora = datetime.now().strftime('%H:%M')
                print(f"Arnaldo: Agora são {agora}.")

            # 5. Comando: Sair
            elif "tchau" in comando or "descansar" in comando:
                print("Arnaldo: Desligando. Até logo!")
                return True
            
            else:
                print(f"Arnaldo: Identifiquei meu nome, mas não entendi o comando: {comando}")
        
        else:
            print("Dica: Comece a frase com 'Arnaldo'...")

    except sr.UnknownValueError:
        # Se você não falar nada, ele apenas volta a ouvir sem dar erro
        pass
    except sr.RequestError:
        print("Arnaldo: Estou com problemas de conexão com a internet.")
    
    return False

print(f"--- ASSISTENTE {NOME_ASSISTENTE.upper()} INICIADO ---")

while True:
    if ouvir_microfone():
        break