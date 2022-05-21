class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0)
            return 0;
        vector <int> f(amount + 1 , INT_MAX);
        f[0] = 0;
        for (size_t i = 1; i != f.size(); ++i) {
            for (size_t j = 0; j != coins.size(); ++j) {
                if (i < coins[j] || f[i-coins[j]] == INT_MAX)
                    continue;
                f[i] = min(f[i-coins[j]] + 1, f[i]);
            }
        }
        if (f[amount] == INT_MAX)
            return -1;
        return f[amount];
    }
};
