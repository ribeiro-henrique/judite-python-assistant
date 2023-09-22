# Judite - Assistente Virtual

Bem-vindo ao repositório do projeto **Judite - Assistente Virtual**. Este projeto é uma assistente virtual simples que pode realizar diversas tarefas, como buscar informações na Wikipedia, reproduzir músicas do YouTube, fornecer a hora atual e a data, entre outras.

## Funcionalidades

A assistente virtual Judite possui as seguintes funcionalidades:

- **Reconhecimento de Voz:** Através da biblioteca SpeechRecognition, Judite pode ouvir comandos de voz do usuário.

- **Cumprimento Personalizado:** Judite saúda o usuário com base na hora do dia (bom dia, boa tarde ou boa noite).

- **Exibição da Hora Atual:** Judite pode informar a hora atual quando solicitada.

- **Exibição da Data Atual:** A assistente também pode fornecer a data atual.

- **Pesquisa na Wikipedia:** Ao receber um comando de pesquisa, Judite busca informações na Wikipedia e fornece um resumo das informações encontradas.

- **Reprodução de Músicas:** Através da biblioteca pywhatkit, Judite é capaz de tocar músicas do YouTube com base em comandos de voz.

- **Encerramento da Escuta:** O usuário pode interromper a escuta da assistente com um comando específico.

## Como Usar

Para usar Judite, basta executar o script Python fornecido. A assistente estará pronta para ouvir seus comandos de voz. Alguns exemplos de comandos que Judite pode entender incluem:

- "Procure por informações sobre..."
- "Pesquise sobre..."
- "Toque a música..."
- "Que horas são?"
- "Qual é a data de hoje?"

## Requisitos

Certifique-se de ter as seguintes bibliotecas Python instaladas:

- pyttsx3
- datetime
- wikipedia
- pywhatkit
- speech_recognition
- urllib.parse

Você pode instalá-las usando o pip:

```bash
pip install pyttsx3 datetime wikipedia pywhatkit SpeechRecognition
```
## Executando o Projeto

Para executar o projeto, simplesmente execute o script Python fornecido:

```bash
python assistente_virtual.py

```
