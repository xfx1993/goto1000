def isScramble( s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    memo = dict()

    def createscramble(s1,s2):
        if sorted(s1)!=sorted(s2):
            return False
        if s1==s2:
            return True
        size = len(s1)

        for i in range(size-1):

            if  (createscramble(s1[:i+1],s2[:i+1]) and createscramble(s1[i+1:],s2[i+1:])) or (createscramble(s1[:i+1], s2[-i-1:]) and createscramble(s1[i+1:], s2[:-i-1])):
                return True

        return False

    return createscramble(s1,s2)

s1 ="xstjzkfpkggnhjzkpfjoguxvkbuopi"
s2 ="xbouipkvxugojfpkzjhnggkpfkzjts"
print(isScramble(s1,s2))