dict_restaurant = {}
def print_restaurant_ratings(filename):
    """Restaurant rating lister."""

    #open the file
    restaurant_info = open(filename)
    #tokennize the line
    for line in restaurant_info:
        line = line.rstrip()
        list_info = line.split(":")
        dict_restaurant[list_info[0]] = list_info[1]
    #restaurant name
    #rating
    #create an empty dictionary
    #put it into the dicctionary
    #use a for-loop to print the sorted restaurants and print the rating
    for key in sorted(dict_restaurant):
        print(f"{key} is rated at {dict_restaurant[key]}")

def enter_new_restaurant():
    new_restaurant_name = input("Enter restaurant name: ")

    new_restaurant_rating = input("Enter restaurant rating: ")
    new_restaurant_rating = int(new_restaurant_rating)

    while new_restaurant_rating > 5 or new_restaurant_rating < 1:
            print("Please enter a rating 1-5")
            new_restaurant_rating = input("Please input a new rating: ")
            new_restaurant_rating = int(new_restaurant_rating)
    
    
    dict_restaurant[new_restaurant_name] = new_restaurant_rating

    
while True:
    print("1: Print Restaurant Ratings List in Alphabetical Order")
    print("2: Add a new restaurant")
    print("Quit")

    answer = input("Please make a selection: ")
    
    
    if answer == "1":
        print_restaurant_ratings("scores.txt")

    elif answer == "2":
        enter_new_restaurant()
    
    elif answer == "Quit":
        break
    else:
        print("Please select an option '1','2', or 'Quit'")



