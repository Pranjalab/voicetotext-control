import threading
import time
import speech_recognition as sr
from pynput import keyboard
import pyautogui
import datetime

class VoiceToText:
    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.recognizer = sr.Recognizer()
        self.is_recording = False
        self.control_count = 0  # Track right control key presses
        self.last_control_time = None
        self.recording_thread = None
        self.previous_text = ""  # Buffer to store the previously recognized text
        self.listener.start()

    def on_press(self, key):
        try:
            if key == keyboard.Key.ctrl_r:  # Detect right control key press
                current_time = datetime.datetime.now()
                
                # Check if last right control press was within 1 second
                if self.last_control_time is not None:
                    time_diff = (current_time - self.last_control_time).total_seconds()
                    if time_diff <= 1:  # If second control press within 1 second
                        self.control_count += 1
                    else:
                        self.control_count = 1  # Reset if more than 1 second has passed
                else:
                    self.control_count = 1  # First press
                self.last_control_time = current_time

                # Start recording if control pressed 2 times in 1 second
                if self.control_count == 2 and not self.is_recording:
                    print("Starting recording...")
                    self.is_recording = True
                    self.previous_text = ""  # Clear buffer when starting a new recording
                    self.recording_thread = threading.Thread(target=self.record_audio)
                    self.recording_thread.start()

                # Stop recording if control pressed while recording
                elif self.control_count == 1 and self.is_recording:
                    print("Stopping recording...")
                    self.is_recording = False
                    self.control_count = 0
        except Exception as e:
            print(f"Error in key press: {e}")

    def replace_symbols(self, text):
        # Replace the spoken words with symbols
        text = text.lower()  # Convert everything to lowercase for easy matching
        text = text.replace("full stop", ".")
        text = text.replace("comma", ",")
        text = text.replace("space", " ")
        return text

    def record_audio(self):
        print("Recording has started.")
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self.is_recording:
                try:
                    print("Listening for audio...")
                    audio = self.recognizer.listen(source, timeout=2, phrase_time_limit=5)  # Increased phrase_time_limit
                    try:
                        text = self.recognizer.recognize_google(audio)

                        # Replace spoken words with actual symbols (e.g., full stop -> .)
                        text = self.replace_symbols(text)

                        # If the recognized text is the same as the previous one, skip it
                        if text != self.previous_text:
                            text += " "  # Add a space at the end of every recognized text entry
                            print(f"Recognized Text: {text}")
                            pyautogui.write(text)  # Writes the text where the cursor is
                            self.previous_text = text.strip()  # Update the buffer with the new text (without the added space)
                        else:
                            print("Repeated text, skipping output.")
                    except sr.UnknownValueError:
                        print("Could not understand the audio.")
                    except sr.RequestError as e:
                        print(f"Could not request results; {e}")
                except Exception as e:
                    print(f"Error during recording: {e}")
                time.sleep(0.1)  # Add a small sleep to prevent excessive CPU usage

        print("Recording has stopped.")

    def run(self):
        print("Running voice-to-text background service...")
        while True:
            time.sleep(1)  # Keep the main thread alive

if __name__ == "__main__":
    vtt = VoiceToText()
    vtt.run()
