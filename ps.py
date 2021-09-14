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

def test_sol() :
    test_fa

    testnum = 1
    # test 1
    if solution(["leo", "kiki", "eden"], ["eden", "kiki"]) != "leo" :
        print("test fail ... at " + str(testnum))
        isAllTestPass = False
    testnum += 1

    # test 2
    if solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]) != "vinko" :
        print("test fail ... at " + str(testnum))
        isAllTestPass = False
    testnum += 1

    # test 3
    if solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) != "mislav" :
        print("test fail ... at " + str(testnum))
        isAllTestPass = False
    testnum += 1
    if isAllTestPass :
        print("All test passed! congraturation...!!")


test_sol()