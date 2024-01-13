# @leet start
class Solution:

    def longestPalindrome(self, s: str) -> str:
        # Mancher algo, not necessary, but why not :)
        # https://en.wikipedia.org/wiki/Longest_palindromic_substring

        s1 = ['|']
        for i in s:
            s1.append(i)
            s1.append('|')
        n = len(s1)
        palindrome_radii = [0] * n
        center = 0
        radius = 0
        
        while center < n:  # len(s1)
            while ( center<n  and center+radius+1<n and s1[center-radius-1]==s1[center+radius+1] ):
                radius += 1

            palindrome_radii[center] = radius

            old_center = center
            old_radius = radius

            center += 1

            radius = 0

            while center <= old_center + old_radius:
                mirrored_center = 2*old_center - center
                max_mirrored_radius =old_center + old_radius -  center

                if palindrome_radii[mirrored_center] < max_mirrored_radius:
                    palindrome_radii[center] = palindrome_radii[mirrored_center]
                    center += 1
                elif palindrome_radii[mirrored_center] > max_mirrored_radius:
                    palindrome_radii[center] = max_mirrored_radius
                    center += 1
                else:
                    radius = max_mirrored_radius
                    break

        m = max(palindrome_radii)
        for j in range(n):
            if palindrome_radii[j] == m:
                return "".join(i for i in s1[j-m:j+m] if i != '|')
        return ''




# @leet end
