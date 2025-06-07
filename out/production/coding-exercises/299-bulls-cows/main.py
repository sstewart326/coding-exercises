class Solution:

    # bulls are the number of digits in the correct index
    # cows are the number of correct digits in incorrect places
    #
    #   secret = "1807"    guess = "7810"
    #             _|__   1A3B
    #
    #   secret[i] == guess[i], if so, increment A
    #   else  count = {digit : count}
    #     A=1  B=3
    #
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        counts = {}
        for idx, c in enumerate(secret):
            if guess[idx] == c:
                a += 1
            else:
                count = counts.get(c, 0)
                counts[c] = count + 1

        for idx, c in enumerate(guess):
            if not secret[idx] == c and c in counts:
                b += 1
                count = counts[c]
                if count == 1:
                    del counts[c]
                else:
                    counts[c] = counts[c] - 1

        return f'{a}A{b}B'

def main():
    sol = Solution()
    print(sol.getHint("1123", "0111"))


if __name__ == "__main__":
    main()