def quiz():
        print("welcome to the animal quiz!")
        print("answer the following questions:")
        questions=[
        "1.what is the largest animal on earth?:a.blue whale,b.mouse,c.cat",
        "2.which bird can fly backwards?:a.cuckoo,b.eagle,c.hummingbird",
        "3.what is the only mammal capable of flight?:a.bat,b.squirrel,c.dolphin"
        ]
        answers=[
        "blue whale",
        "hummingbird",
        "bat"
        ]
        score=0
        for i in range(len(questions)):
            user_answer=input(questions[i]).strip().lower()
            if user_answer==answers[i]:
                print("correct!")
                score += 1
            else:
                print("incorrect!")

        print("\nquiz completed!")
        print(f"you got {score}/{len(questions)} questions correct.")
quiz ()
