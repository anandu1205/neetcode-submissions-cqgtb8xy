class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = 0   # pointer for word
        j = 0   # pointer for abbr

        while i < len(word) and j < len(abbr):

            # normal character
            if abbr[j].isalpha():

                if word[i] != abbr[j]:
                    return False

                i += 1
                j += 1

            else:

                # leading zero invalid
                if abbr[j] == '0':
                    return False

                num = 0

                # build complete number
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1

                # skip characters in word
                i += num

        return i == len(word) and j == len(abbr)
        