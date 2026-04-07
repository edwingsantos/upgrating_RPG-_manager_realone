#ES main file
 
from create import create
from fake_accounts import create_fake_account
from load import load_data, save, stats
from graph import graph 


def main():
    load_data()

    print("Welcome to the RPG")
    while True:
        print("1 Create Character\n2 Show Stats\n3 Graph Character\n4 Save\n5 Fake Profile\n6 Exit")

        choice = input("Choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            stats()
        elif choice == "3":
            graph()
        elif choice == "4": 
            save()
        elif choice == "5":
            create_fake_account()
        elif choice == "6":
            save()
            break
        else:
            print("Invalid")

main()