#ES main file
#import things you need 
from create import create
from fake_accounts import create_fake_account
from load import load_data, save, stats
from graph import graph 

#make a funtion for main and call the load data funtion
def main():
    load_data()
    #print welcome and options to choose, and an input asking for choice 
    print("Welcome to the RPG")
    while True:
        print("1 Create Character\n2 Show Stats\n3 Graph Character\n4 Save\n5 Fake Profile\n6 Exit")

        choice = input("Choice: ")
        #if choice is 1 call the create funtion 
        if choice == "1":
            create()
        #elif choice is 2 call the stats funtion
        elif choice == "2":
            stats()
        #elif chioce is 3 call the graph funtion 
        elif choice == "3":
            graph()
        #elif choice is 4 call the save funtion 
        elif choice == "4": 
            save()
        #elif choice is 5 call the create fake account funtion 
        elif choice == "5":
            create_fake_account()
        #elif choice is 6 save and brea
        elif choice == "6":
            save()
            break
        #else print please select again
        else:
            print("please select again ")

#call main 
main()