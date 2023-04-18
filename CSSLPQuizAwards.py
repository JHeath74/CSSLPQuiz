CorrectAnswersCSSLPDict = {}
IncorrectAnswersCSSLPDict = {}


def CorrectIncorrectResponses(playername, portpoints):
	response = -1

	while response != 0:
		response = input("Do you wish to see the correct or incorrect answers?\n"
						+ "1 for Correct Answers\n"
						+ "2 for Incorrect Answers\n"
						+ "0 for Exit")
		if response == "0":
			final_score(playername, portpoints)
			break
		if response == "1":
			for CorrectAnswers in CorrectAnswersCSSLPDict:
				print(CorrectAnswers)

		if response == "2":
			for IncorrectAnswers in IncorrectAnswersCSSLPDict:
				print(IncorrectAnswers)


def final_score(playername, portpoints):
	file_name = playername + "Score" + ".txt"

	print("Saving your award certificate: " + file_name)

	awardtext = "Congratulations, " + playername + "\n" \
				+ "Name: " + playername + "\n" \
				+ "Final Score: " + str(portpoints) + "\n"
	final_score_award = open(file_name, "w")

	final_score_award.write(awardtext)

	final_score_award.write("\nCorrect Answers\n")

	for line in CorrectAnswersCSSLPDict:
		final_score_award.write("%s\n" % line)

	final_score_award.write("\n\nIncorrectAnswers\n")

	for line in IncorrectAnswersCSSLPDict:
		final_score_award.write("%s\n" % line)

