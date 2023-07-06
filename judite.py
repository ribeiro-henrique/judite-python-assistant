import pyttsx3
import datetime
import wikipedia
import pywhatkit
import speech_recognition as sr
from urllib.parse import urlparse, parse_qs

engine = pyttsx3.init()
escutando = True  # Variável de controle para o estado de escuta

def falar(audio):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        comando = r.recognize_google(audio, language='pt-BR')
        print(comando)
        return comando

    except Exception as e:
        print(e)
        falar('Nossa! Eu não entendi o que você disse!')
        return 'None'

def welcome():
    hora_exata = datetime.datetime.now().hour
    if 6 <= hora_exata < 12:
        falar('Muito bom dia!')
    elif 12 <= hora_exata < 18:
        falar('Boa tarde!')
    elif 18 <= hora_exata <= 24:
        falar('Boa noite!')
    else:
        falar('Você não deveria estar dormindo?')
    falar('Sou Judite, sua assistente, como posso ajudá-lo?')

def time():
    hora = datetime.datetime.now().strftime('%I:%M')
    falar('São exatamente: ' + hora)

def data():
    hoje = datetime.datetime.now()
    dia = str(hoje.day)
    mes = hoje.strftime('%B')
    ano = str(hoje.year)
    falar('Hoje é dia ' + dia + ' de ' + mes + ' de ' + ano)

def procurar(comando):
    termo = comando.replace('procure por', '')
    wikipedia.set_lang('pt')
    try:
        resultado = wikipedia.summary(termo, 2)
        falar(resultado)
    except wikipedia.exceptions.DisambiguationError as e:
        falar('Há várias opções disponíveis. Por favor, especifique sua pesquisa.')
    except wikipedia.exceptions.PageError as e:
        falar('Desculpe, não foi possível encontrar informações sobre esse termo.')

def musica(comando):
    musica = comando.replace('toque', '')
    resultado = pywhatkit.playonyt(musica)
    if resultado:
        url = resultado[0]
        parsed_url = urlparse(url)
        video_id = parse_qs(parsed_url.query).get('v')
        if video_id:
            video_title = pywhatkit.title(video_id[0])
            falar('Tocando música ' + video_title)
            pywhatkit.playonyt(url)
    else:
        falar('Desculpe, não encontrei resultados para essa música.')

def parar_escuta():
    global escutando
    escutando = False

def main():
    welcome()
    while escutando:
        print('Ouvindo...')
        comando = microphone().lower()

        if 'procure por' in comando:
            procurar(comando)
            parar_escuta()

        elif 'pesquise' in comando:
            procurar(comando)
            parar_escuta()

        elif 'pesquise por' in comando:
            procurar(comando)
            parar_escuta()

        elif 'significa' in comando:
            procurar(comando)
            parar_escuta()

        elif 'toque' in comando:
            musica(comando)
            parar_escuta()

        elif 'horas' in comando:
            time()
            parar_escuta()

        elif 'data' in comando:
            data()
            parar_escuta()

if __name__ == '__main__':
    
  main()