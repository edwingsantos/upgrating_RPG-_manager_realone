#ES graph file 
#import all things needed 
from data import characters
import math 
import matplotlib.pyplot as plt

#make a funtion for graph
def graph():
    #if there is nothing in characters list print no characters and return 
    if not characters:
        print("no characters")
        return
    #make a loop and enumerate chraracters
    for choice, i in enumerate(characters):
        print(choice, i["Name"])
    #if 
    try:
        choice  = int(input("Pick: "))
        i = characters[choice]
    except:
        print("Invalid")
        return

    labels = ["Strength", "Speed", "Intelligence"]
    values = [i[l] for l in labels]

    angles = [n / float(len(labels)) * 2 * math.pi for n in range(len(labels))]
    values += values[:1]
    angles += angles[:1]

    plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    plt.title(i["Name"])
    plt.show()

