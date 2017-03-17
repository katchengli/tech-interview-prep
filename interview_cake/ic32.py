def sortScoresList(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
    n = len(unsorted_scores)
    countScoresList = [0] * (HIGHEST_POSSIBLE_SCORE+1)
    sortedList = list()

    for score in unsorted_scores:
        countScoresList[score] += 1

    for i in range(len(countScoresList)):
        for _ in range(countScoresList[i]):
            sortedList.append(i)

    return sortedList

unsorted_scores = [37, 89, 0, 41, 65, 91, 41, 53, 100]
HIGHEST_POSSIBLE_SCORE = 100
print(sortScoresList(unsorted_scores, HIGHEST_POSSIBLE_SCORE))
