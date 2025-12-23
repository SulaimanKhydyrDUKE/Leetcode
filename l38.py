class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"  # base case: countAndSay(1)

        for _ in range(2, n + 1):
            result = []
            i = 0

            while i < len(s):
                count = 1
                # count consecutive identical digits
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1

                result.append(str(count))
                result.append(s[i])
                i += 1

            s = "".join(result)

        return s
