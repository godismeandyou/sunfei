def convert_to_numeric(score):
    return int(score)


def sum_of_middle_three(score1, score2, score3, score4, score5):
    return score1 + score2 + score3 + score4 + score5


def score_to_rating_string(average_score):
    return '%d' % average_score


def scores_to_rating(score1, score2, score3, score4, score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """

    # STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    # STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1, score2, score3, score4, score5) / 3

    # STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating


print scores_to_rating(1, 1, 5, 1, 1)
# print score_to_rating_string(3)
