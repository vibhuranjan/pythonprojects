import random
import os
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
    'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for quizNum in range(35):
    quizFile = open('C:\\fuNke\\docs\\python\\quiz%s.txt' %(quizNum+1),'w')
    answerFile = open('C:\\fuNke\\docs\\python\\answerquiz%s.txt' %(quizNum+1),'w')
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    answerFile.write("Answer for all questions\n")
    answerFile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(50) :
        quizFile.write((' ' * 4))
        quizFile.write("%s. What is the capital of %s?\n" %(questionNum+1, states.__getitem__(questionNum)))
        correct_answer = capitals[states.__getitem__(questionNum)]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correct_answer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correct_answer]
        random.shuffle(answerOptions)
        for i in range(4):
            quizFile.write((' ' * 8))
            quizFile.write('%s. %s' % (i+1, answerOptions[i]))
            quizFile.write('\n')
        answerFile.write("%s. %s" %(questionNum+1,correct_answer))
        answerFile.write('\n')
    quizFile.close()
    answerFile.close()
print("Done")