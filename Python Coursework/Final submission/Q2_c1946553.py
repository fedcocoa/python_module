import random,csv
import matplotlib.pyplot as plt
import itertools
# random.seed(57)

#Plot the probability that a wins against the ra/rb
def plot_probabilities(abilities,trials):
    probabilities = []
    ratings = []
    for pair in abilities:
        probabilities.append(winProbability(pair[0],pair[1],trials))
        ratings.append(pair[0]/pair[1])
    plt.plot(ratings,probabilities,'o--g')
    plt.xlabel('Rating of A/Rating of B')
    plt.ylabel('Probability that player A beats player B')
    plt.suptitle('Probability that player a beats player b')
    plt.show()

#reads the abilities from the filename and returns a list of tuples
def get_abilities(filename):
    abilities_file = csv.reader(open(filename,'r'))
    abilities = []
    for line in abilities_file:
        if abilities_file.line_num != 1:
            abilities.append((int(line[0]),int(line[1])))
    return abilities

#calculate the probability that a wins a single game against b
#n controls how many times this is tested over and loosely represents the accuracy
def winProbability(ra,rb,n):
    prob_a = 0
    for i in range(0,n):
        result = game(ra,rb)
        if result.index(max(result)) == 0:
            prob_a+=1
    return prob_a/n

#Passing in 2 scores, return true if either one of the players had reached the win conditions
def pars_win(score_a,score_b):
    return ((score_a >= 11 or score_b >= 11) and abs(score_a-score_b) >= 2)

def english_win(score_a,score_b,first_to):
    return score_a == first_to or score_b == first_to

#Run one game with the rating of A and the rating of B, once the game is finished
#return a tuple of the scores
def game(ra,rb):
    prob_a = ra/(ra+rb)
    score_a = 0
    score_b = 0
    server = random.choice(['a','b'])
    first_to = 9
    while not english_win(score_a,score_b,first_to):
        point = random.random()
        if point < prob_a:
            if server == 'a':
                score_a+=1
            else:
                server = 'a'
        else:
            if server == 'b':
                score_b+=1
            else:
                server = 'b'
        if score_a == 8 and score_b == 8:
            first_to = random.choice([9,10])
    
    return (score_a,score_b)

def probability_first_to_n(n,probability):
    iterations = list(itertools.permutations(n*'w'+n*'l',n*2))
    no_repeats = []
    for iteration in iterations:
        if iteration not in no_repeats and list(iteration).count('w') == n:
            no_repeats.append(iteration)
    no_losses = []
    for iteration in no_repeats:
        wins = 0
        losses = 0
        for result in iteration:
            if result == 'l':
                losses+=1
            else:
                wins+=1
            if wins == n and losses < n:
                no_losses.append(iteration)
                break
    clipped = []
    for iteration in no_losses:
        wins = 0
        for i in range(0,len(iteration)):
            if wins == n:
                clipped.append(iteration[0:i])
                break
            if iteration[i] == 'w':
                wins+=1
    probabilities = []
    for iteration in clipped:
        probabilities.append((probability**iteration.count('w'))*(1-probability)**iteration.count('l'))
    return sum(probabilities)

def minimum_games(rating_a,rating_b):
    games = 1
    probability = winProbability(rating_a,rating_b,5000)
    while probability_first_to_n(games,probability) < 0.9:
        games+=1
    return games

def testing(iterations):
    test_values = [(50,50),(70,20),(95,5),(80,80),(60,20),(70,50)]
    test_averages = []
    test_wins = [{'a':0,'b':0},{'a':0,'b':0},{'a':0,'b':0},{'a':0,'b':0},{'a':0,'b':0},{'a':0,'b':0}]
    for test in test_values:
        average = [0,0]
        for i in range(0,iterations):
            result = game(test[0],test[1])
            average[0] += result[0]
            average[1] += result[1]
            if result[0] > result[1]:
                test_wins[test_values.index(test)]['a'] += 1
            else:
                test_wins[test_values.index(test)]['b'] += 1
        average[0]/=iterations
        average[1]/=iterations
        test_averages.append(average)

    print("English System")
    for i in range(0,len(test_values)):
        print(f"Test-Values: {test_values[i]} Average-Scores: {test_averages[i]} Wins: {test_wins[i]}")

# testing(1000)