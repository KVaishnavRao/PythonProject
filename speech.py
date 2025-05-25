import speech_recognition as sr # type: ignore
import nltk # type: ignore

# Optional: Set custom nltk_data path
nltk.data.path.append(r'C:\Users\K Vaishnav Rao\nltk_data')

# Download tokenizer data
nltk.download('punkt')

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("\nRecognized Text:")
        print(text)

        tokens = nltk.word_tokenize(text)
        print("\nTokenized Words:")
        print(tokens)

        return text

    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Request failed; {e}")

if __name__ == "__main__":
    recognize_speech_from_mic()
