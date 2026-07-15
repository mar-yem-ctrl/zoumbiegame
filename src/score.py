import os

class ScoreSystem:
    def __init__(self, filename="highscore.txt"):
        self.filename = filename
        self.score = 0
        self.multiplier = 1
        self.streak = 0
        self.high_score = self.load_high_score()

    def load_high_score(self):
        
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    return int(f.read().strip())
            except ValueError:
                return 0
        return 0

    def save_high_score(self):
        
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.filename, "w") as f:
                f.write(str(self.high_score))

    def add_points(self, points):
       
        added_score = points * self.multiplier
        self.score += added_score
        return added_score

    def zombie_killed(self):
        
        base_points = 10
        self.streak += 1
        
        
        if self.streak % 5 == 0:
            self.multiplier = min(5, self.multiplier + 1) 
            
        self.add_points(base_points)

    def reset_streak(self):
       
        self.streak = 0
        self.multiplier = 1

    def reset_game(self):
        
        self.save_high_score() 
        self.score = 0
        self.multiplier = 1
        self.streak = 0