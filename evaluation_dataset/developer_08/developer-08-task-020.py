def word_score(word, input_letters, questions=0):
    score = 0
    bingo = 0
    filled_by_blanks = []
    rack = list(input_letters)
    for letter in word:
        if letter in rack:
            bingo += 1
            score += letter_score(letter)
            rack.remove(letter)
        else:
            filled_by_blanks.append(letter_score(letter))
    for blank_score in sorted(filled_by_blanks, reverse=True):
        if questions > 0:
            score += blank_score
            questions -= 1
    if bingo > 6:
        score += 50
    return score