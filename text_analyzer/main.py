"""
Text Analyzer
--------------
Lets the user enter a text and analyze it: count words and
characters, count vowels, find the most repeated word, and
reverse the text.
"""

from analyzer import count_words, count_characters, count_vowels, most_common_word, reverse_text

def main():
    print("=== Text Analyzer ===")
    text = input("Enter the text to analyze: ")
    
    while True:
        print("\nAnalysis options:")
        print("1. Count words")
        print("2. Count characters")
        print("3. Count vowels")
        print("4. Most repeated word")
        print("5. Reverse text")
        print("6. Exit")
        print("7. Change text")

        option = input("\nChoose an option: ")
        
        if option == "1":
            print(f"Word count: {count_words(text)}")
        
        elif option == "2":
            print(f"Character count: {count_characters(text)}")
        
        elif option == "3":
            print(f"Vowel count: {count_vowels(text)}")
        
        elif option == "4":
            word, count = most_common_word(text)
            print(f"The most repeated word is '{word}' with {count} occurrences.")
        
        elif option == "5":
            print(f"Reversed text: {reverse_text(text)}")
        
        elif option == "6":
            print("Thanks for using the text analyzer. Goodbye!")
            break
        
        elif option == "7":
            text = input("Enter the new text to analyze: ")
            
        else:
            print("Invalid option, please choose between 1 and 7.")
    
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()