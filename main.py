from essential_generators import DocumentGenerator
import time

def random_sentence():
    gen = DocumentGenerator()
    return gen.sentence()

def calculate_typing_speed(text, elapsed_time):
    words = len(text.split())
    minutes = elapsed_time / 60
    speed = words / minutes if minutes > 0 else 0
    return speed

def main():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter to start the test.")
    start_time = time.time()
    text = random_sentence()
    user_input = input(text + "\n")
    count=0
    if len(text)>len(user_input):
        for j in range(len(user_input)):
            if user_input[j]==text[j]:
                count+=1
    else:
        for j in range(len(text)):
            if user_input[j]==text[j]:
                count+=1
    accuracy=count/len(text)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    typing_speed = calculate_typing_speed(text, elapsed_time)
    print(f"\nElapsed time: {elapsed_time:.2f} seconds")
    print(f"Your typing speed: {int(typing_speed*accuracy):.2f} words per minute")

if __name__ == "__main__":
    main()