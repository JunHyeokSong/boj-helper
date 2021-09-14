def solution(participant, completion):
    countIfCompletion = {}
    for man in participant :
        if man in countIfCompletion :
            countIfCompletion[man] += 1
        else :
            countIfCompletion[man] = 1
    
    for completeMan in completion :
        countIfCompletion[completeMan] -= 1
    
    for candidate in countIfCompletion :
        # who has not complete yet!
        if countIfCompletion[candidate] != 0 :
            answer = candidate

    return answer