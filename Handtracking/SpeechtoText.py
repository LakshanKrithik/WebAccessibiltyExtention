import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Loop infinitely for the user to speak
while True:
    try:
        # Print instruction for the user
        print("Please say something...")

        # Use the microphone as the source for input
        with sr.Microphone() as source2:
            # Adjust for ambient noise
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # Listen for the user's input
            audio2 = r.listen(source2)

            # Recognize the speech using Google's API
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print(f"Did you say: {MyText}")

            # If the user says 'exit', stop the loop
            if 'exit' in MyText:
                print("Exiting the program...")
                break

    except sr.RequestError as e:
        print(f"Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occurred. Could not understand the audio.")
