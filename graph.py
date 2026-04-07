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
    #if choice is an integer make i characters chioce
    try:
        choice  = int(input("Pick: "))
        i = characters[choice]
    #else print invalid option and return 
    except:
        print("Invalid")
        return
    #make labels be strenght speed and intelligence
    labels = ["Strength", "Speed", "Intelligence"]
    #and values a loop for l in labels 
    values = [i[l] for l in labels]
    #make angles the math for the angles 
    angles = [n / float(len(labels)) * 2 * math.pi for n in range(len(labels))]
    values += values[:1]
    angles += angles[:1]
    #make the graph or circle thing using matplotlib 
    plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    plt.title(i["Name"])
    plt.show()

