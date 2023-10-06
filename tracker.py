amount_interviews = int(input("How many interviews did you conduct? "))
questions = [[] for _ in range(amount_interviews)] # create a list of empty lists for each interview
answers = [[] for _ in range(amount_interviews)] # create a list of empty lists for each interview
names = [] # create a list to store the names of interviewees

for i in range(amount_interviews):
    name = input(f"Name of the interviewee for interview {i+1}: ")
    names.append(name)
    num_questions = int(input(f"How many questions did you ask in interview {i+1}? "))
    for j in range(num_questions):
        question = input(f"Question number {j+1} for interview {i+1}: ")
        answer = input(f"Answer number {j+1} for interview {i+1}: ")
        questions[i].append(question)
        answers[i].append(answer)

for i, interview in enumerate(questions):
    print(f"Interview {i+1} with {names[i]}:")
    for j, question in enumerate(interview):
        print(f"Question {j+1}: {question}")
        print(f"Answer {j+1}: {answers[i][j]}")
    for j, question in enumerate(interview):
        print(f"Question {j+1}: {question}")
        print(f"Answer {j+1}: {answers[i][j]}")