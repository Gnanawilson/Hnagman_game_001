import random
import hangman_file
#word_list=["apple","beautiful","potato"]+
lives=6
chosen_word=random.choice(hangman_file.words)  
print(chosen_word) 
display=[]
for letter in range(len(chosen_word)):#1 2 3 4 5 apple
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter :").lower()
    for position in range(len(chosen_word)): 
        letter= chosen_word[position]#apple
        if letter==guessed_letter:              #_ p p_ _
            display[position]=guessed_letter #x
    print(display)        
    if guessed_letter not in chosen_word:
        lives-=1    
        if lives==0:
            game_over= True
            print("You lose!!!👎")   
            
            
    if '_' not in display:
        game_over = True
        print("you win!!🏆!!")
    else:
            
      print(hangman_file.stages[lives])        