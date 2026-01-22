class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage] * 5001
        self.furthest = 0
        self.time = 0
        

    def visit(self, url: str) -> None:
        self.time += 1
        self.history[self.time] = url
        self.furthest = self.time

        

    def back(self, steps: int) -> str:
        jump = min(self.time, steps)
        self.time -= jump
        return self.history[self.time]
        

    def forward(self, steps: int) -> str:
        jump = min(self.furthest - self.time, steps)
        self.time += jump
        return self.history[self.time]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
