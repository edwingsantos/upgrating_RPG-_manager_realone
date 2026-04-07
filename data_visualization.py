import matplotlib.pyplot as plt
import math

class DataVisualization:
    def radar_chart(self, character):
        labels = ["Strength", "Speed", "Intelligence"]
        values = [character.stats[l] for l in labels]

        angles = [n / float(len(labels)) * 2 * math.pi for n in range(len(labels))]

        values += values[:1]
        angles += angles[:1]

        plt.figure()
        ax = plt.subplot(111, polar=True)
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.1)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)

        plt.title(character.name)
        plt.show()