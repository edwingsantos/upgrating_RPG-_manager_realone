from load import characters
import math 
import matplotlib.pyplot as plt

def graph():
    if not characters:
        print("No characters")
        return

    for i, c in enumerate(characters):
        print(i, c["Name"])

    try:
        i = int(input("Pick: "))
        c = characters[i]
    except:
        print("Invalid")
        return

    labels = ["Strength", "Speed", "Intelligence"]
    values = [c[l] for l in labels]

    angles = [n / float(len(labels)) * 2 * math.pi for n in range(len(labels))]
    values += values[:1]
    angles += angles[:1]

    plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    plt.title(c["Name"])
    plt.show()

