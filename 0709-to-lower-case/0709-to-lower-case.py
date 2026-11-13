class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for char in s:
            # Check if the character is an uppercase letter
            if 65 <= ord(char) <= 90:
                # Convert to lowercase by adding 32 to its ASCII value
                result.append(chr(ord(char) + 32))
            else:
                result.append(char)
        return "".join(result)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna