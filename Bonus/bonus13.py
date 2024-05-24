import json
with open("questions13.json", 'r') as file:
    content = file.read()

data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answers: "))
    question["user_choice"] = user_choice


score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Your answer is correct for question "
    else:
        result = "Your answer is wrong for question "
    message = f"{result} {index + 1} - Your answer was: {question['user_choice']}," \
              f"Correct answer is: {question['correct_answer']}"
    print(message)

# print(data)
print(score, "/", len(data))
