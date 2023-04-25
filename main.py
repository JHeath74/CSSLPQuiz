import random

import CSSLPQuizAwards
import CSSLPQuizQuestionsDict

guess = -1
CSSLPpoints = 0
correct = 0
incorrect = 0
newvalue = 0
newvalue2 = 0
newvalue3 = 0
newvalue4 = 0

shuffledvalues = {}

playername = input("Please Enter your name and press the enter key: ")

while guess != 0:

	print("\nCSSLP Quiz")
	print("You'll be given a question,  and must choose the best answer\n")

	CSSLPInfo = random.choice(list(CSSLPQuizQuestionsDict.CSSLPdict.values()))
	dictvalue = {i for i in CSSLPQuizQuestionsDict.CSSLPdict if CSSLPQuizQuestionsDict.CSSLPdict[i] == CSSLPInfo}

	value = str(dictvalue).replace("{", "").replace("}", "").replace("'", "")
	value2 = random.choice(list(CSSLPQuizQuestionsDict.CSSLPdict.keys()))
	value3 = random.choice(list(CSSLPQuizQuestionsDict.CSSLPdict.keys()))
	value4 = random.choice(list(CSSLPQuizQuestionsDict.CSSLPdict.keys()))

	shuffledvalues[value] = value
	shuffledvalues[value2] = value2
	shuffledvalues[value3] = value3
	shuffledvalues[value4] = value4

	newvalue = random.choice(list(shuffledvalues.keys()))
	shuffledvalues.pop(newvalue)
	newvalue2 = random.choice(list(shuffledvalues.keys()))
	shuffledvalues.pop(newvalue2)
	newvalue3 = random.choice(list(shuffledvalues.keys()))
	shuffledvalues.pop(newvalue3)
	newvalue4 = random.choice(list(shuffledvalues.keys()))

	if newvalue4 is None:
		newvalue4 = random.choice(list(shuffledvalues.keys()))

	shuffledvalues.clear()
	print("Question is in Red,\n"
		  "  Choose option \u001b[32m 1 \033[39m" + ",\u001b[32m 2, \033[39m" + "\u001b[32m 3, \033[39m" +
		  "or \u001b[32m 4 \033[39m" + "for your answer\n incorrect responses are in Yellow\n")
	guess = input("Answer the following question \n \u001b[31m" + CSSLPInfo + "\033[39m:\n\n"
				  + "Option 1: \u001b[32m" + str(newvalue) + "\033[39m\n"
				  + "Option 2: \u001b[32m" + str(newvalue2) + "\033[39m\n"
				  + "Option 3: \u001b[32m" + str(newvalue3) + "\033[39m\n"
				  + "Option 4: \u001b[32m" + str(newvalue4) + "\033[39m\n"
				  + "Type 0 to exit\n"
				  + "\nWhich open is your guess?\n"
				  + "Answer is: ")
	guess.lower()
	value.lower()

	if guess == "0":
		CSSLPQuizAwards.CorrectIncorrectResponses(playername, CSSLPpoints)
		break

	if guess == "1":
		if newvalue == value:
			print("Congratulations, your right!")
			CSSLPpoints += 1
			correct += 1
			print("Your Current Score: " + str(CSSLPpoints))
			CSSLPQuizAwards.CorrectAnswersCSSLPDict[newvalue] = CSSLPInfo

			for i in CSSLPQuizAwards.CorrectAnswersCSSLPDict:
				print("Values: " + i + "Port Info: ", CSSLPInfo)

			shuffledvalues.clear()
			print("______________________________________")
			print("______________________________________")

		else:
			print("\nYour choice was not correct.\n"
				  "The correct answer is \033[1;33m" + value + "\033[39m")
			CSSLPpoints -= 1
			incorrect += 1
			CSSLPQuizAwards.IncorrectAnswersCSSLPDict[newvalue] = CSSLPInfo

			shuffledvalues.clear()
			print("Your Current Score: " + str(CSSLPpoints))
			print("______________________________________")
			print("______________________________________")

	if guess == "2":
		if newvalue2 == value:
			print("Congratulations, your right!")
			CSSLPpoints += 1
			correct += 1
			print("Your Current Score: " + str(CSSLPpoints))
			CSSLPQuizAwards.CorrectAnswersCSSLPDict[newvalue2] = CSSLPInfo

			for i in CSSLPQuizAwards.CorrectAnswersCSSLPDict:
				print("Values: " + i + "Port Info: ", CSSLPInfo)

			shuffledvalues.clear()
			print("______________________________________")
			print("______________________________________")

		else:
			print("\nYour choice was not correct.\n"
				  "The correct answer is \033[1;33m" + value + "\033[39m")
			CSSLPpoints -= 1
			incorrect += 1
			CSSLPQuizAwards.IncorrectAnswersCSSLPDict[newvalue2] = CSSLPInfo

			shuffledvalues.clear()
			print("Your Current Score: " + str(CSSLPpoints))
			print("______________________________________")
			print("______________________________________")

	if guess == "3":
		if newvalue3 == value:
			print("Congratulations, your right!")
			CSSLPpoints += 1
			correct += 1
			print("Your Current Score: " + str(CSSLPpoints))
			CSSLPQuizAwards.CorrectAnswersCSSLPDict[newvalue3] = CSSLPInfo

			for i in CSSLPQuizAwards.CorrectAnswersCSSLPDict:
				print("Values: " + i + "Port Info: ", CSSLPInfo)

			shuffledvalues.clear()
			print("______________________________________")
			print("______________________________________")

		else:
			print("\nYour choice was not correct.\n"
				  "The correct answer is \033[1;33m" + value + "\033[39m")
			CSSLPpoints -= 1
			incorrect += 1
			CSSLPQuizAwards.IncorrectAnswersCSSLPDict[newvalue3] = CSSLPInfo

			shuffledvalues.clear()
			print("Your Current Score: " + str(CSSLPpoints))
			print("______________________________________")
			print("______________________________________")

	if guess == "4":
		if newvalue4 == value:
			print("Congratulations, your right!")
			CSSLPpoints += 1
			correct += 1
			print("Your Current Score: " + str(CSSLPpoints))
			CSSLPQuizAwards.CorrectAnswersCSSLPDict[newvalue4] = CSSLPInfo

			for i in CSSLPQuizAwards.CorrectAnswersCSSLPDict:
				print("Values: " + i + "Port Info: ", CSSLPInfo)

			shuffledvalues.clear()
			print("______________________________________")
			print("______________________________________")
		else:
			print("\nYour choice was not correct.\n"
				  "The correct answer is \033[1;33m" + value + "\033[39m")
			CSSLPpoints -= 1
			incorrect += 1
			CSSLPQuizAwards.IncorrectAnswersCSSLPDict[newvalue4] = CSSLPInfo

			shuffledvalues.clear()
			print("Your Current Score: " + str(CSSLPpoints))
			print("______________________________________")
			print("______________________________________")

	print("Quiz Over")
	print("Total Score: " + str(CSSLPpoints))
	print("Number of correct guesses: " + str(correct))
	print("Number of incorrect guesses: " + str(incorrect))
