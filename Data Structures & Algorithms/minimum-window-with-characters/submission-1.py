class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}

        # Count required characters from t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        countS = {}

        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("infinity")

        left = 0

        for right in range(len(s)):

            # Add current character to window
            c = s[right]
            countS[c] = 1 + countS.get(c, 0)

            # If this character has reached the required frequency
            if c in countT and countS[c] == countT[c]:
                have += 1

            # Try shrinking the window
            while have == need:

                # Check if current window is smaller
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # Remove left character
                leftChar = s[left]
                countS[leftChar] -= 1

                # Removing it makes the window invalid
                if leftChar in countT and countS[leftChar] < countT[leftChar]:
                    have -= 1

                left += 1

        l, r = res

        return s[l:r + 1] if resLen != float("infinity") else ""