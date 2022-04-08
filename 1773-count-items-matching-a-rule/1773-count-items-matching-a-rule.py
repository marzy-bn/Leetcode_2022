class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for item in items:
            if ruleValue == item[0] and ruleKey == "type":
                count += 1
            if ruleValue == item[1] and ruleKey == "color":
                count += 1
            if ruleValue == item[2] and ruleKey == "name":
                count += 1
        return count