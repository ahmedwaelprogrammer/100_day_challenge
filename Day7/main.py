hangman_stages = [
    """
       ------
       |    |
       |    
       |    
       |    
       |    
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    
       |    
       |    
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |    
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |    
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |    
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |    
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |    
    ---------
    """
]


word ="ahmed"
stage_counter = 0
word_user = []

for letter in word:
    word_user.append("_")

print(f"Guess the word : {word_user}")

while stage_counter != len(hangman_stages) - 1:
    letter_exist = False
    user_letter = input("Enter a letter: ")
    for i in range(0 , len(word_user)):
        if user_letter == word[i] and word_user[i] == "_":
            word_user[i] = word[i]
            print(f"Right guess keep up your word now is {word_user}")
            letter_exist = True
            break
        elif user_letter == word[i] and word_user[i] != "_":
            print("You gisssed this letter before !")
            letter_exist = True
            break
    if not letter_exist:
        stage_counter += 1;
        print(hangman_stages[stage_counter])
        
    if stage_counter == len(hangman_stages) - 1:
        print("Sorry your player dies you lost")
        break
