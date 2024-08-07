class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        units = num % 1000
        thous = num % 1000000 // 1000
        mills = num % 1000000000 // 1000000
        bills = num % 1000000000000 // 1000000000

        def render(digits):
            digit_map = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
            teens_map = {0: "Ten", 1: "Eleven", 2: "Twelve", 3: "Thirteen", 4: "Fourteen", 5: "Fifteen", 6: "Sixteen", 7: "Seventeen", 8: "Eighteen", 9: "Nineteen"}
            tens_map = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
            numd = len(str(digits))
            if numd == 1:
                if digits == 0:
                    return ""
                return digit_map[digits]
            ans = ""
            if numd == 3:
                ans += str(digit_map[digits//100]) + " Hundred"
            digits = digits % 100
            tens = digits // 10
            if tens == 1:
                ans += " " + teens_map[digits % 10]
                return ans.strip()
            elif tens == 0:
                ans += " " + digit_map[digits % 10]
                return ans.strip()
            else:
                ans += " " + tens_map[tens] + " "
                if digits % 10 != 0:
                    ans += digit_map[digits % 10]
                return ans.strip()

        part1 = render(bills)
        part2 = render(mills)
        part3 = render(thous)
        part4 = render(units)
        ans = ""
        if part1:
            ans += part1 + " Billion"
        if part2:
            ans += " " + part2 + " Million"
        if part3:
            ans += " " + part3 + " Thousand"
        if part4:
            ans += " " + part4 
        return ans.strip()
