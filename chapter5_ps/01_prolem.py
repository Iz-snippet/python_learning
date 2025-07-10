#write a python program to create a dictionary of hindi words with value as therir english translation provide user with an option to look it up

hindi_to_english = {
   "namaste": "Hello",
   "shukriya": "Thank you",
    "pyaar": "Love",
    "dost": "Friend",
}

word = input("Enter a Hindi word to look up its English translation: ")
print(hindi_to_english[word])