
# time - O(n)
# space - O(1) because the dictionary only stores up to 26 keys
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        max_repeated = 0
        char_freq = {}

        # most freq count per window
        most_freq_count = 0

        for right in range(len(s)):
            curr_char = s[right]
            curr_count = char_freq.get(curr_char, 0) + 1
            char_freq[curr_char] = curr_count

            most_freq_count = max(most_freq_count, curr_count)
            window_size = right - left + 1

            if most_freq_count + k < window_size:
                window_size -= 1
                char_freq[s[left]] = char_freq[s[left]] - 1
                left += 1

            max_repeated = max(max_repeated, window_size)

        return max_repeated

def main():
    sol = Solution()
    print(sol.characterReplacement("AABABBA", 1))


if __name__ == "__main__":
    main()