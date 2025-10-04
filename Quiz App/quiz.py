import random
import requests
import html
from urlLib import *

if __name__ == "__main__":

    print("Welcome to Bablu's Quiz App!\n")

    while True:    
        print(f"Here are some categories to choose from:\n")

        for i in range(1, len(categories) + 1):
            print(f"{i}. {categories[i-1]}")

        print("\n")

        while True:
            try:
                category = int(input("Choose a category for questions (1-10): "))
                if 1 <= category <= 10:
                    break
                else:
                    print("❌ Invalid category! Please enter a number between 1 and 10.")
            except ValueError:
                print("❌ Please enter a valid number.")

        print("\n")

        if category >= 1 and category <= 10:

            while True:
                difficulty = input("Choose a difficulty level(type E for Easy, M for Medium and H for Hard): ")
                if difficulty.upper() in ['E', 'M', 'H']:
                    break
                else: # difficulty not in range
                    print("❌ Invalid difficulty level! Please enter E, M, or H.")

            if difficulty.upper() == "E":
                difficulty = "Easy"
                if category == 1:
                    url = Computers_url[difficulty]
                
                elif category == 2:
                    url = Gadgets_url[difficulty]

                elif category == 3:
                    url = VideoGames_url[difficulty]

                elif category == 4:
                    url = Films_url[difficulty]

                elif category == 5:
                    url = ScienceNature_url[difficulty]

                elif category == 6:
                    url = GK_url[difficulty]
                
                elif category == 7:
                    url = Politics_url[difficulty]

                elif category == 8:
                    url = Maths_url[difficulty]

                elif category == 9:
                    url = Sports_url[difficulty]
                
                elif category == 10:
                    url = Books_url[difficulty]

            elif difficulty.upper() == "M":
                difficulty = "Medium"
                
                if category == 1:
                    url = Computers_url[difficulty]
                
                elif category == 2:
                    url = Gadgets_url[difficulty]

                elif category == 3:
                    url = VideoGames_url[difficulty]

                elif category == 4:
                    url = Films_url[difficulty]

                elif category == 5:
                    url = ScienceNature_url[difficulty]

                elif category == 6:
                    url = GK_url[difficulty]
                
                elif category == 7:
                    url = Politics_url[difficulty]

                elif category == 8:
                    url = Maths_url[difficulty]

                elif category == 9:
                    url = Sports_url[difficulty]
                
                elif category == 10:
                    url = Books_url[difficulty]

            elif difficulty.upper() == "H":
                difficulty = "Hard"
                
                if category == 1:
                    url = Computers_url[difficulty]
                
                elif category == 2:
                    url = Gadgets_url[difficulty]

                elif category == 3:
                    url = VideoGames_url[difficulty]

                elif category == 4:
                    url = Films_url[difficulty]

                elif category == 5:
                    url = ScienceNature_url[difficulty]

                elif category == 6:
                    url = GK_url[difficulty]
                
                elif category == 7:
                    url = Politics_url[difficulty]

                elif category == 8:
                    url = Maths_url[difficulty]

                elif category == 9:
                    url = Sports_url[difficulty]
                
                elif category == 10:
                    url = Books_url[difficulty]

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                print("\n")

                score = 0
                i=1
                for item in data['results']:

                    print(f"Question {i}: {html.unescape(item['question'])}")
                    i+=1

                    randomNumber = random.randint(0, len(item['incorrect_answers']))
                    options = [html.unescape(opt) for opt in item['incorrect_answers']]
                    correct_answer = html.unescape(item['correct_answer'])
                    options.insert(randomNumber, correct_answer)


                    for j in range(0, len(options)):
                        print(f"{j+1}. {options[j]}")

                    while True:
                        try:
                            choice = int(input("Enter the correct option number(option 1/2/3/4): "))
                            if choice in [1, 2, 3, 4]:
                                break
                            else:
                                print("❌ Invalid option! Please enter a number between 1 and 4.")
                        except ValueError:
                            print("❌ Please enter a valid option number (1-4).")

                    print("Correct Answer:", correct_answer)

                    if options[choice - 1] == correct_answer:
                        score += 1
                        print("✅ Correct!\n")
                    else:
                        print(f"❌ Wrong! Correct answer: {correct_answer}\n")

                    print("\n")

                print(f"Your score is: {score}/10")

            else:
                print(f"Failed to load questions. Error code: {response.status_code}")

        except requests.exceptions.RequestException:
            print("❌ No Internet! Please connect and try again...")

        while True:
            try:
                print("\n")
                play_again = input("Do you want to play again? (Y/N): ").upper()
                print("\n")
                print("\n")

                if play_again == 'Y':
                    break  # continue playing

                elif play_again == 'N':
                    exit()

                else:
                    print("❌ Invalid input! Please enter Y or N.")

            except (KeyboardInterrupt, EOFError):
                print("\nExiting...")
                exit()
