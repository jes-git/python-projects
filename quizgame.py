questions= [
    {
    
        "prompt":["Pure silicon is ?"],
        "options":["A. ptype ","B.ntype", "C. intrinsic","D.extrinsic"],
        "answer":"C"

    },
    {
        "prompt":["If a small amount of phosphorus is added to germanium, then: ?"],
        "options":["A. The conductivity decreases  ","B.Silicon becomes a P-type semiconductor ", "C. Phosphorus becomes an acceptor impurity ","D.There will be more free electrons than holes "],
        "answer":"D"
        

    },
    {
        "prompt":["An intrinsic semiconductor at 0 K behaves as: 0 K ?"],
        "options":["A. A semiconductor   ","B.An insulator  ", "C. A conductor  ","D.A superconductor "],
        "answer":"B"
        

    }


]
def run_quiz(questions):
    score=0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer=input("Enter your answer(A, B, C, or D?):").upper()
        if answer==question["answer"]:
            print("CORRECT\n")
            score+=1 
        else:
            print("Wrong. The correct answer was ",question["answer"],"\n")

    print(f"You got {score} out of {len(questions)} questions correct.")


run_quiz(questions)
