# Define a function named 'get_initials' to extract initials from a full name
def get_initials():
    # Prompt the user to enter first and last name, then split them by space
    user = input("Enter first name and last name: ").split(' ')
    # Extract the first element (first name), then first letter, and convert it into uppercase
    firstname_initial = user[0][0].upper() 
    # Extract the last element (last name), then first letter, and convert it into uppercase
    lastname_initial = user[-1][0].upper()
    # Print the concatenated initials
    print(f'Your initials are {firstname_initial}{lastname_initial}.')

# Call the function
get_initials()
