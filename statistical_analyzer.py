import pandas as pd

class StatisticalAnalyzer:
    def __init__(self, characters):
        self.df = pd.DataFrame([c.to_dict() for c in characters])

    def summary(self):
        return self.df.describe()

    def mean_stats(self):
        return self.df.mean(numeric_only=True)