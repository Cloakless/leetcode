class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        options = set(supplies)
        ans = []
        unbuilt = {}
        for i in range(len(recipes)):
            unbuilt[recipes[i]] = ingredients[i]
        increasing = True
        while increasing:
            next_ones = {}
            increasing = False
            for recipe in unbuilt:
                can_build = True
                for ingredient in unbuilt[recipe]:
                    if ingredient not in options:
                        can_build = False
                        break
                if can_build:
                    increasing = True
                    options.add(recipe)
                    ans.append(recipe)
                else:
                    next_ones[recipe] = unbuilt[recipe]
            unbuilt = next_ones
        return ans

        
