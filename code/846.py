class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        cards = {}
        for card in hand:
            if card in cards:
                cards[card] += 1
            else:
                cards[card] = 1
        for i in range(n-groupSize+1):
            if cards[hand[i]] > 0:
                for j in range(groupSize):
                    if (hand[i]+j) in cards and cards[hand[i]+j] > 0:
                        cards[hand[i]+j] -=1
                    else:
                        return False
        return True
