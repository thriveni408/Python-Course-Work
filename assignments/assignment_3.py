def quiz_game():
    questions = [
        ("Which keyword is used to print output?",
         ["print", "output", "show", "display"], "a"),

        ("Which function is used to take user input?",
         ["input()", "scan()", "read()", "get()"], "a"),

        ("What is the file extension of Python?",
         [".java", ".py", ".c", ".txt"], "b"),

        ("Which data type stores multiple values in order?",
         ["set", "tuple", "dictionary", "list"], "d"),

        ("Which keyword starts a function?",
         ["function", "define", "def", "fun"], "c"),

        ("Which operator is used for addition?",
         ["*", "-", "+", "/"], "c"),

        ("What is the output of type(10)?",
         ["int", "float", "str", "bool"], "a"),

        ("Which loop runs while a condition is true?",
         ["for", "while", "if", "switch"], "b"),

        ("Which symbol is used for comments?",
         ["//", "/* */", "#", "--"], "c"),

        ("What does len() function do?",
         ["adds values", "counts values", "removes values", "sorts values"], "b"),

        ("Which data type is immutable?",
         ["list", "set", "dict", "tuple"], "d"),

        ("What is the output of 2 + 3 * 4?",
         ["20", "14", "24", "10"], "b"),

        ("Which keyword stops a loop?",
         ["stop", "end", "break", "exit"], "c"),

        ("Which function converts int to string?",
         ["int()", "str()", "float()", "bool()"], "b"),

        ("Which data type stores key-value pairs?",
         ["list", "tuple", "set", "dictionary"], "d"),

        ("Which keyword is used for condition?",
         ["if", "for", "while", "def"], "a"),

        ("What is the output of bool(1)?",
         ["False", "Error", "True", "None"], "c"),

        ("Which function gives maximum value?",
         ["top()", "big()", "max()", "high()"], "c"),

        ("Which keyword skips current loop iteration?",
         ["skip", "continue", "pass", "break"], "b"),

        ("Which data type does not allow duplicate values?",
         ["list", "tuple", "set", "dict"], "c")
    ]

    score = 0
    print("Welcome to Python Quiz Game\n")

    for i in range(len(questions)):
        q, options, correct = questions[i]
        print(f"Question {i+1}: {q}")

        print("a)", options[0])
        print("b)", options[1])
        print("c)", options[2])
        print("d)", options[3])

        answer = input("Your answer (a/b/c/d): ").lower()

        if answer == correct:
            print("Correct\n")
            score += 1
        else:
            print("Wrong\n")

    print("Quiz Completed")
    print("Your Score:", score, "/ 20")


quiz_game()
