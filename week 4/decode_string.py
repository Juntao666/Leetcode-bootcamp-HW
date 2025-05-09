class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        strings = []
        curr_s = ""
        curr_num = ""
        res = ""
        for char in s:
            if char.isdigit():
                curr_num += char
                if len(curr_s) > 0:
                    strings.append(curr_s)
                curr_s = ""
            elif char == "[":
                nums.append(int(curr_num))
                curr_num = ""
            elif char == "]":
                if len(strings) == 0:
                    res += nums.pop() * curr_s
                    curr_s = ""
                if len(strings) > 0:
                    curr_s  = strings.pop() + curr_s * nums.pop()

            else:
                curr_s += char
        res += curr_s
        return res