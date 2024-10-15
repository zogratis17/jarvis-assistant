# jarvis-assistant

A voice-activated virtual assistant named **Jarvis**, powered by Google’s Gemini model. It listens to user input via microphone and responds using AI.

## Prerequisites

- **Python 3.x**  
- Install dependencies:
  ```bash
  pip install requests speechrecognition
- **Gemini API Key**: Get a valid API key from Google to use the Gemini model.

## File Structure

graphql

Copy code

`jarvis-assistant/ │ ├── config.py   # Stores Gemini API key ├── speech.py   # Handles microphone input └── main.py     # Core logic to interact with Gemini`

## Configuration

1. **Add API Key**  
    Create `config.py` and add:
    
      ```bash
    
    key = "your_gemini_api_key_here"
    `````

## How to Run

1. **Start the Assistant**  
    Run the following command:
    
    
```bash
    `python main.py`
```
2. **Speak Your Query**
    
    - Wait for the prompt: _"Say something."_
    - Speak clearly into the microphone.
    - Jarvis will recognize your input and respond accordingly.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Google Gemini Language Model](https://cloud.google.com/)
- [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/)
