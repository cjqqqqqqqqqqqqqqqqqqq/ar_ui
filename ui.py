import tkinter as tk
import time
import speech_recognition as sr

def update_time():
    current_time = time.strftime('%Y-%m-%d \n%H:%M')
    time_label.config(text=current_time)
    root.after(1000, update_time)

def recognize_speech_from_mic():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    text = "" 
    # Use microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1) 
        print("Listening... Speak now.")

        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        
        except sr.WaitTimeoutError:
            print("You didn't say anything! Try again.")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from the recognition service; {e}")

    speak_label.config(text=text)
    root.after(1000, recognize_speech_from_mic) 

#ui
root = tk.Tk()
root.title("User Interface")
root.geometry("800x600")
root.configure(bg='black')

speak_label = tk.Label(root, text="", fg="white", bg="black")
speak_label.place(relx=0, rely=0, relwidth=0.3, relheight=0.3)

navigation_label = tk.Label(root, text="Navigation", fg="white", bg="black")
navigation_label.place(relx=0.3, rely=0, relwidth=0.5, relheight=0.3)

time_label = tk.Label(root, text="", fg="white", bg="black")
time_label.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.3)
update_time()

radar_left_label = tk.Label(root, text="↙", fg="white", bg="black",font=("Arial", 80))
radar_left_label.place(relx=0, rely=0.7, relwidth=0.333, relheight=0.3)

radar_middle_label = tk.Label(root, text="↓", fg="white", bg="black",font=("Arial", 80))
radar_middle_label.place(relx=0.333, rely=0.7, relwidth=0.333, relheight=0.3)

radar_right_label = tk.Label(root, text="↘", fg="white", bg="black",font=("Arial", 80))
radar_right_label.place(relx=0.666, rely=0.7, relwidth=0.333, relheight=0.3)

recognize_speech_from_mic()

root.mainloop()