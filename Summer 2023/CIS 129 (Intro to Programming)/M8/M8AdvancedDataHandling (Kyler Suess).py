# Professor Zak allows students to drop the four lowest scores on the ten 100-point quizzes she gives during the semester. 
# Create the flowchart and pseudocode for an application that accepts a student name and 10 quiz scores.
# Output the student’s name and total points for the student’s six highest-scoring quizzes.

# Program will loop until user enters 'quit'
while True:
    student_name = input("Enter student name (or 'quit' to exit): ")
    
    if student_name.lower() == "quit":
        break
    
    # Initialize empty array for scores
    scores = []

    # Initialize i = 1, then iterate 1-11 for each score inputed.
    for i in range(1, 11):
        score = int(input("Enter score {}: ".format(i)))
        scores.append(score)

    # Sort the scores entered into the array
    sorted_scores = sorted(scores, key=lambda x: -x)

    # User input for if they wish to drop the 4 lowest scores
    drop_scores = input("Do you want to drop the lowest four scores? (yes/no): ")

    if drop_scores.lower() == "yes":
        final_scores = sorted_scores[:6]
    else:
        final_scores = sorted_scores

    print("Student Name:", student_name)
    print("Scores:", final_scores)
    print()
