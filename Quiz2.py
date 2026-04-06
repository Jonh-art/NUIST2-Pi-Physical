import RPi.GPIO as GPIO
import time

RED_LED = 17
GREEN_LED = 18

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(RED_LED, GPIO.OUT)
    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.LOW)

def led_correct():
    GPIO.output(GREEN_LED, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(GREEN_LED, GPIO.LOW)

def led_incorrect():
    GPIO.output(RED_LED, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(RED_LED, GPIO.LOW)

def cleanup_gpio():
    GPIO.cleanup()

def quiz():
    print("Welcome to the Python Quiz!")
    print("Answer the following questions by entering a, b, c, or d:\n")

    questions = [
        "1) Which of the following is NOT a python data type?\na) int\nb) float\nc) rational\nd) string\ne) bool\nYour answer: ",
        "2) Which of the following is NOT a built-in operation in Python?\na) +\nb) %\nc) abs()\nd) sqrt()\nYour answer: ",
        "3) In a mixed-type expression involving ints and floats, Python will convert:\na) floats to ints\nb) ints to strings\nc) floats and ints to strings\nd) ints to floats\nYour answer: ",
        "4) The best structure for implementing a multi-way decision in Python is:\na) if\nb) if-else\nc) if-elif-else\nd) try\nYour answer: ",
        "5) What statement can be executed in the body of a loop to cause it to terminate?\na) if\nb) exit\nc) continue\nd) break\nYour answer: "
    ]

    answers = [
        "c",
        "d",
        "d",
        "c",
        "d"
    ]
    score = 0

    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()
        if user_answer == answers[i]:
            print("Correct!\n")
            led_correct()
            score += 1
        else:
            print(f"Incorrect!\n")
            led_incorrect()

    print("\nQuiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")

if __name__ == "__main__":
    try:
        setup_gpio()
        quiz()
    except KeyboardInterrupt:
        print("\nQuiz interrupted.")
    finally:
        cleanup_gpio()
        print("GPIO cleaned up.")

