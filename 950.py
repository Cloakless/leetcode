class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        initial = []
        for i in range(n):
            initial.append(i)

        dealt = []
        while True:
            m = len(initial)
            if m > 1:
                dealt.append(initial.pop(0))
                initial.append(initial.pop(0))
            elif m > 0:
                dealt.append(initial[0])
                break
        final = [0]*n
        for i in range(n):
            final[dealt[i]] = deck[i]
        return final
