def find_restaurant_ratings(filename):
    """Restaurant rating lister."""

    #open the file
    restaurant_info = open(filename)
    dict_restaurant = {}
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
    
# 
