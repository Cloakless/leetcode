class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int drunk = 0;
        int spare = 0;
        while (numBottles > 0) {
            drunk += numBottles;
            spare += numBottles % numExchange;
            numBottles = numBottles / numExchange;
            if (spare >= numExchange) {
                spare -= numExchange;
                numBottles += 1;
            }
        }
        return drunk;
    }
};
