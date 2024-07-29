'''
1. Python Sets Adventure

Task 1: Flight Route Comparison

Imagine you work for an airline and need to compare the flight routes of your airline with a competitor, You have two sets of flight destinations, one for each airline. Write a Python program to find out: 

1. Destinations that both airlines fly to
2. Destinations unique to your airline
3. Whether there are any destinations that neither airline shares

'''



our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


def main():

    while True:
        print("\n1. Find destinations that both airlines fly to")
        print("2. Find destinations unique to your airline")
        print("3. Find whethere there are any destinations that neither airline shares.")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            intersection_airlines = our_routes.intersection(competitor_routes)
            print(intersection_airlines)
        elif choice == '2':
            difference_airlines = our_routes.difference(competitor_routes)
            print(difference_airlines)
        elif choice == '3':
            neither_shares = our_routes.symmetric_difference(competitor_routes)
            print(neither_shares)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Please enter a valid choice. ")

main()
