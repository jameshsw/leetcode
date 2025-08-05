class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(ransomNote)
        magazine_conuter = Counter(magazine)

        for k, c in ransom_counter.items():
            if magazine_conuter[k] < c:
                return False
        return True

        """
        ml = list(magazine)
        for c in ransomNote:
            if not c in ml:
                return False
            ml.remove(c)
        return True
        """
