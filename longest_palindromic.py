class Solution: 
    def longestPalindrome(self, s):
        slen = len(s)
        longest = ''
        longest_len = 0
        for i in range(1, slen-1):
            loops+=1
            l, r = i-1, i+1
            subs = s[i]
            while l >= 0 and r < slen:
                if s[l] != s[r]:
                    if s[r] == s[i]:
                        l+=1
                        subs = ''
                    else:
                        break
                subs = s[l] + subs + s[r]
                l -= 1
                r += 1
                loops+=1
            subs_len = i - l
            if subs_len > 1:
                if subs_len > longest_len:
                    longest_len = subs_len
                    longest = subs
        return longest
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
