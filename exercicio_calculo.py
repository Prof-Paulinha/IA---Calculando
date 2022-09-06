import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
maquina = pyttsx3.init()


def executa_comando():
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'Paula' in comando:
                comando = comando.replace('Paula', '')
                maquina.say(comando)
                maquina.runAndWait()
                
    except:
        print('Microfone não está funcionando')
    
    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'calcular' in comando:
        conversa1 = "Insira a quantidade de Refrigerante"
        maquina.say('Por favor' + conversa1)            
        maquina.runAndWait()
        
        qtde_refri = int(input("Insira a quatidade de Refrigerante: "))
        valor_refri = 2
        total_refri = qtde_refri * valor_refri
        
        maquina.say('O valor é: {} reais' .format(total_refri))
        maquina.runAndWait()
       
         

comando_voz_usuario()