import tkinter as tk
import speech_recognition as sr
import pyperclip

def copyText():
    text = T.get('1.0', tk.END)
    pyperclip.copy(text)
    
def voiceCommand():
    recognizer = sr.Recognizer()
    voice_btn.config(text='Listening...', bg='steelblue', fg='white')
    
    with sr.Microphone() as source:
        root.update()
        
        try:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Listening...")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=20)
            print("Recognizing...")
            text = recognizer.recognize_google(audio, language='bn-BD')
            T.insert(tk.END, text + " ")
            output_label.config(text="Completed")
        except sr.WaitTimeoutError:
            output_label.config(text="Listening timed out while waiting for phrase to start")
            print("Listening timed out while waiting for phrase to start")
        except sr.UnknownValueError:
            output_label.config(text="Could not understand audio")
            print("Could not understand audio")
        except sr.RequestError as e:
            output_label.config(text=f"Could not request results; {e}")
            print(f"Could not request results; {e}")
        except Exception as e:
            output_label.config(text=f"An error occurred; {e}")
            print(f"An error occurred; {e}")

# Initialize the main window
root = tk.Tk()
root.title("Bangla Speech to Text")

# Create a Text widget
T = tk.Text(root)
T.pack()

# Create a Button to start voice command
voice_btn = tk.Button(root, text="Start Voice Command", command=voiceCommand)
voice_btn.pack()

# Create a Button to copy text
copy_btn = tk.Button(root, text="Copy Text", command=copyText)
copy_btn.pack()

# Create a Label to show output status
output_label = tk.Label(root, text="")
output_label.pack()

# Run the main loop
root.mainloop()