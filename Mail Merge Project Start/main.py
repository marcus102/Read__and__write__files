#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
        
PLACEHOLDER = '[name]'
    
with open('Mail Merge Project Start/Input/Names/invited_names.txt') as data:
    guess_names = data.readlines()
    
    with open('Mail Merge Project Start\Input\Letters\starting_letter.txt') as data:
        letter = data.read()
        for name in guess_names:
            stripped_names = name.strip()
            new_letter = letter.replace(PLACEHOLDER, stripped_names)
            with open(f"Mail Merge Project Start\Output\ReadyToSend\letter_for_{stripped_names}.txt", mode='w') as all_letters:
                all = all_letters.write(new_letter)
                
                
