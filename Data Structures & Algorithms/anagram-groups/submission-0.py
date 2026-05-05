class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = {}
        output = []
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in sorted_strings:
                 sorted_strings[sorted_string].append(string)
            else:
                sorted_strings[sorted_string] = [string]
        for value in sorted_strings.values():
            output.append(value)
        return output

        