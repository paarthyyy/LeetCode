class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        if not s :
            return 0 
        else :
            return len(s[-1])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna