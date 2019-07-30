
# coding: utf-8

# In[1]:


import random


# In[2]:


from collections import Counter


# In[3]:


someWords = 'apple banana mango orange graps pipeapple lychee berry papaya cherry watermelon coconut lemon'


# In[4]:


someWords = someWords.split(' ')


# In[5]:


word = random.choice(someWords)


# In[12]:


if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of fruit')
    for i in word:
        print('_', end =' ')
    print()
    
    playing = True
    #list for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) +2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag ==0:
            #flag is updated when the word is correctly guessed
            print()
            chances -= 1
            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue
            
            #validation of guess
            if not guess.isalpha():
                print('Enter a Letter')
                continue
            elif len(guess)>1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue
            
            #if letter is guessed correctly
            if guess in word:
                k = word.count(guess)
                #k stores the numbers of times the guesswd letter occured in the word
                for x in range(k):
                    letterGuessed += guess
                    #The guess letter is added as many times as it occurs
                    
                #Print the word
                for char in word:
                    if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                        print(char, end =' ')
                        correct +=1
                    #if user has guessed all the letters
                    elif (Counter(letterGuessed) == Counter(word)):
                        #Once the correct word is guessed fully,
                        #the game ends, even if chances remain
                        
                        print("The word is: ", end = ' ')
                        print(word)
                        flag = 1
                        print('Congratulations , You Won!!! ')
                        break
                        #To break out the for loop
                        #To break out the while loop
                    else:
                        print('_', end = ' ')
                        
        #If user has used all of his/her chances
        
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost!! Try again..')
            print('The word was {}'.format(word))
    except KeyboardInterrupt:
        print()
        print('Bye ! Try again.')
        exit()
            
                        

