# To score and rank adjudicators
# Need to create questions- each entry in the question_bank should be itself a list in the format [question with options, correct answer (from 1-4)]
# Future plan- create centralised and persistent scores

question_bank = []
my_adj_score = 0

for question in question_bank:
  answer = input(str(question[0]))
  if answer == str(question[1]):
    my_adj_score += 1
    print("The next question is:")
  else:
    print("The next question is:")

print("Your adj score is: " + str(my_adj_score))
