# **Voice-to-Text Control**

### A Python-based background service that converts real-time audio input into text and simulates typing the recognized text in any active window. The recording starts and stops with a double press of the right control key for seamless typing experience.

## **Table of Contents**
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
  - [Using `setup_env.sh`](#using-setup_envsh)
- [Usage](#usage)
  - [Running the Software](#running-the-software)
  - [Using Voice-to-Text](#using-voice-to-text)
  - [Stopping the Software](#stopping-the-software)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Contributors](#contributors)
- [License](#license)

---

## **Introduction**

**Voice-to-Text Control** is a Python-based background service designed to seamlessly convert your spoken words into text in real time. By using your system's microphone, the software listens to your voice and dynamically types out the recognized speech wherever your cursor is focused—whether you're in a browser, text editor, terminal, or any other application.

This tool allows for hands-free typing, where the recording process is intuitively controlled by pressing the **right control key** twice in quick succession. Once activated, you can speak naturally, and the program will convert your speech into text. Common punctuation like commas and periods are recognized and inserted as symbols (`","` and `"."`), ensuring grammatically correct output. After each recognized sentence, a space is automatically added, allowing you to continue typing smoothly without manual intervention.

The recording can be stopped by pressing the right control key again, making it simple to control when to start and stop dictation. **Voice-to-Text Control** is ideal for dictation, hands-free writing, accessibility purposes, or simply increasing productivity by reducing the need for manual typing.

With support for real-time speech recognition and a flexible, platform-independent architecture, this tool integrates seamlessly into various workflows, empowering users to leverage voice input effectively.

## **Features**

- Real-time speech-to-text conversion using your microphone.
- Easy start/stop functionality by double-pressing the **right control key**.
- Automatically inserts punctuation such as commas, periods, and spaces.
- Seamless integration with any text input area (browser, text editor, terminal, etc.).
- Runs as a background service.
- Cross-platform support for Linux, macOS, and Windows (with minimal modification).

## **Installation**

### **Using `setup_env.sh`**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/voicetotext-control.git
   cd voicetotext-control
   ```

2. **Run the Setup Script**
   The script `setup_env.sh` will automatically set up a virtual environment, install dependencies, and handle system-level packages such as `portaudio` for you.

   First, make sure the script is executable:
   ```bash
   chmod +x setup_env.sh
   ```

   Then, run the setup script:
   ```bash
   ./setup_env.sh
   ```

   The script will:
   - Create a virtual environment named `voice_to_text`
   - Install all required Python packages
   - Install system-level dependencies (e.g., `portaudio`)

---

## **Usage**

### **Running the Software**

1. **Activate the Virtual Environment** (if not already activated):
   ```bash
   source voice_to_text/bin/activate
   ```

2. **Run the Script**:
   ```bash
   python voice_to_text.py
   ```

3. **Start Recording**:
   - Press the **right control key** twice within one second to start recording.
   - You will see "Recording has started" in the terminal, and the tool will begin converting your speech to text.

4. **Speak and Dictate**:
   - Speak into your microphone, and the recognized text will be typed where your cursor is focused.
   - Punctuation (e.g., **comma**, **full stop**) is automatically inserted as symbols (`,` and `.`).

5. **Stop Recording**:
   - Press the **right control key** once to stop recording.
   - The terminal will display "Recording has stopped."

### **Stopping the Software**
Simply **press `Ctrl + C`** in the terminal to stop the background process running the voice-to-text software.

## **Troubleshooting**

- **PyAudio installation issues**:
   - If you encounter errors related to `portaudio.h` or `PyAudio`, ensure you’ve installed the necessary system dependencies (e.g., `portaudio19-dev` for Linux).
   - Use pre-built binaries for **Windows** from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

- **Speech recognition not working**:
   - Ensure your microphone is working and properly configured.
   - Test with other speech-to-text tools to ensure the audio is being captured.

- **Right control key not functioning as expected**:
   - Check if the correct key (`Key.ctrl_r`) is mapped on your system.
   - You can modify the key detection logic in the `voice_to_text.py` file if needed.

## **Contributing**

We welcome contributions! If you have suggestions or would like to improve this project, follow the steps below:

1. **Fork this repository**.
2. Create a new **branch**:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and **commit** them:
   ```bash
   git commit -m "Add a meaningful commit message"
   ```
4. **Push** to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a **Pull Request** with a detailed description of your changes.

Feel free to open an issue for feature requests, bug reports, or any other questions.

## **Contributors:**

| ![Pranjal Bhaskare](https://github.com/Pranjal-neo.png?size=100) |
|:----------------------------------------------------------------:|
| [Pranjal Bhaskare](https://github.com/Pranjal-neo)               |

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

