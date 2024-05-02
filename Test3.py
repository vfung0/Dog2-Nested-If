# 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Would you like to climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")



# 2: Setting the Scene

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Would you like to climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("Do you want to light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("The torch reveals ancient wall paintings!")
    elif action == "proceed in the dark":
        print("You stumble upon a sleeping dragon!")

        
# 3: Default Path

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Would you like to climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass  # Placeholder for invalid choice in the forest

elif place == "cave":
    action = input("Do you want to light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("The torch reveals ancient wall paintings!")
    elif action == "proceed in the dark":
        print("You stumble upon a sleeping dragon!")
    else:
        pass  # Placeholder for invalid choice in the cave

else:
    pass  # Placeholder for invalid choice of place


# 1: Code Correction
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# 2: Venue Selection
attendees = int(input("Enter number of attendees: "))

# Determine the venue based on the number of attendees
venue = "large hall" if attendees > 100 else "conference room"

# Recommend additional facilities based on the number of attendees
facilities = []
if attendees > 80:
    facilities.append("audio system")
if attendees > 100:
    facilities.append("projector")

# Output the venue and recommended facilities
print(f"Venue: {venue}")
print("Recommended facilities:")
for facility in facilities:
    print(f"- {facility}")


# 3: Catering Choices

attendees = int(input("Enter number of attendees: "))

# Determine the venue based on the number of attendees
venue = "large hall" if attendees > 100 else "conference room"

# Recommend additional facilities based on the number of attendees
facilities = []
if attendees > 80:
    facilities.append("audio system")
if attendees > 100:
    facilities.append("projector")

# Ask for the user's food preference
vegetarian = input("Do you want vegetarian food? (yes/no): ").strip().lower()
caterer = "Veggie Delight Caterers" if vegetarian == "yes" else "Gourmet Meals Caterers"

# Output the venue, recommended facilities, and the caterer
print(f"Venue: {venue}")
print("Recommended facilities:")
for facility in facilities:
    print(f"- {facility}")
print(f"Recommended caterer: {caterer}")


