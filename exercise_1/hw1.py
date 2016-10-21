import util

def a__at_least_one_ace_over_three_cards():
    res = []
    util.getFirstXCards(3, res)
    cnt = 0
    for r in res:
        for card in r:
            if (card[0] is 1):
                cnt += 1
                break
    return float(cnt) / float(len(res))

def b__exactly_one_ace_over_five_cards(naive=False):
    if naive is not False:
        res = []
        util.getFirstXCards(5, res)
        cnt = 0;
        for r in res:
            number_of_aces = 0
            for card in r:
                if (card[0] is 1):
                    number_of_aces += 1
            if number_of_aces is 1:
                cnt += 1

        return float(cnt) / float(len(res))
    else:
        ''' #aces . how we can combine the other 4 cards (without aces)
                . all the possible permutation of this 5 cards
                . the permutation of the reamins card '''
        return float((4 * util.get_combination(48, 4) * util.fact(5) * util.fact(47)))/float(util.fact(52))

print "Probability to have at least one ace over three cards is", a__at_least_one_ace_over_three_cards()
print "Probability to have exactly one ace over five cards is", b__exactly_one_ace_over_five_cards()
# c --> Simone
# d TODO
# e TODO


