import os
import sys
from weather import *


def process_message(msg):
    # Well this is our dictionary of questions
    qtn = {
        '1': ['hi', 'hey', 'wela', 'tsuma', 'oya', 'hello', 'niaje', 'sasa'],
        '2': ['Hi', 'How', 'are', 'you', 'doing'],
        '3': ['sure', 'why', 'not?'],
        '4': ['poa', 'sana!'],
        '5': ['where', 'are', 'you', 'see'],
        '6': ['good', 'morning', 'gdmorning', 'mrning', 'gud', 'gd'],
        '7': ['I\'m', 'I am', 'I', 'am', 'fine', 'fyn', 'doing'],
        '8': ['good', 'afternoon', 'afternun', 'after', 'noon'],
        '9': ['good', 'evening', 'gd', 'gud'],
        '10': ['good', 'night', 'gdnyt', 'gdnight', 'nyt'],
        '11': ['can', 'i', 'meet', 'you', 'want', 'to', 'cn', 'come'],
        '12': ['on', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],
        '13': ['fuck', 'sex', 'you', 'ass', 'penis', 'vagina', 'mjinga', 'stupid'],
        '14': ['do', 'you', 'love', 'me', 'i'],
        '15': ['i', 'miss', 'missing', 'you', 'do'],
        '16': ['and', 'you?', 'abt', 'about', 'you', 'what', 'en', 'tell', 'me', 'sema', 'niambie'],
        '17': ['haha', 'hahaha', 'ha', 'heheh', 'hehehe', 'hihihi', 'hihi', 'waaa', 'waa', ],
        '18': ['what', 'is', 'your', 'name', 'who', 'you', 'are', 'tell', 'abt', 'about', 'yourself', 'me', 'more',
               'tsubot'],
        '19': ['do', 'you', 'have', 'time', 'chat', 'can', 'cn', 'chat?', 'want'],
        '20': ['programming', 'language', 'python', 'java', 'best', 'which'],
        '21': ['do', 'you', 'have', 'a', 'girl', 'friend', 'boyfriend', 'girlfriend', 'boy', 'best']
    }
    ans = {
        '0': "Oups, I didn't understand that. I'm just a robot learning. \n Hint: Bado Sielewi Kiswahili Mazee. Sam will teach me shortly",
        '1': "Hello too",
        '2': "I'm doing fine. Tell me, and what about you?",
        '3': "Thats why am here to clear your doubts",
        '4': "Yeah. Poa sana! I have a limited Swahili vocabulary, text in English to enjoy your Bot Experience",
        '5': "I'm in Nairobi",
        '6': "Good Morning too. How are you doing?",
        '7': "Great to hear that you're fine!",
        '8': "Good afternoon too. How are you doing?",
        '9': "Good evening too. How are you doing?",
        '10': "Good night too and have a peaceful night!",
        '11': "Sure! Tell me where and when I can meet you. Then I check if I will be in a Position",
        '12': "I have noted down the day. Kindly remind me on the morning on that day.",
        '13': "No! That's a wrong gear you're taking. I discourage use of vulgar language!",
        '14': "Aha! Love is a great thing! Ofcouse we should all love each other as humans!",
        '15': "Ofcourse I miss you too",
        '16': "I am fine too. Will tell you more about it",
        '17': "What's soo funny to you? I didnt get the joke :-)",
        '18': "My name is TsuBot. An Assistant texting Robot for Tsuma - The guy who programmed me Officially known as Samuel Tsuma Mwanyasi. You can follow him here: www.twitter.com/itsMwanyasi254",
        '19': "Sure! Why not. Yes we can always chat!",
        '20': "Personally, I enjoy programming in Python. However I love PHP too and yeah CSS effect on HTML plus Java! For a starter, I recommend beginning learning with Python.\n The brain of this TsuBot is running on python!",
        '21': "Heheh! Who doesn't!? Nope I dont. I have a bunch of best friends who keep me moving",

    }

    global keyToAnswer  # This a global variable initialized to answer 0 No Matching detail
    keyToAnswer = "0"
    # Remove Punctuations from the input
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    clean_msg = ""
    for char in msg:
        if char not in punctuations:
            clean_msg = clean_msg + char
            if (len(clean_msg)) == 0:
                return (ans["0"])
                # See! WE have successful removed all characters
    # Convert the users input into lower case for searching in our dictionary
    clean_msg = clean_msg.lower()
    # Splitting the user sentence into array for interpretation
    msg_array = clean_msg.split()
    # Test Split Function
    # print(msg_array)-- In Code Testing -- THis is to test the actions done on user input
   
    '''
    BELOW IS A POSITIVE SCENARIO IF USERS QUESTION IS FOUND IN DICTIONARY OF QTNS
    '''
    LenArray = []
    for key in qtn:
        # Successfully identified question matching users input
        matches = set(msg_array).intersection(qtn[key])
        # Trying to get the array with a maximum match /Accuracy
        # print(matches)
        NotFounds = 0
        if len(matches) != 0:
            Lengths = (len(matches))
            LenArray.append(Lengths)
            # print(LenArray)
            # print(LenArray)  # In Code Testing - THis is the array of matching lengths
            # Get The Key Indexed by the match
            if len(matches) == max(LenArray):
                keyToAnswer = key
    return ans[keyToAnswer]  # Pass any question not matching user input - DO NOTHING WITH IT
    # OUr main aim is getting the highest match
    # END OF EXECUTION


if __name__ == '__main__':
    while 1:
        msg = input("Enter something: ")
        print(process_message(msg))
