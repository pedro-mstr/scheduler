import random

# List of property references
apartments = [
    "HD-1185", "HD-1153Y", "HD-1153K", "HD-1144", "HD-1052", "HD-1180", "HD-1175",
    "HD-1099", "HD-1127", "HD-1118", "HD-1142", "HD-1156", "HD-1126", "HD-1176",
    "HD-1153L", "HD-1179A", "HD-1162", "HD-1101", "HD-1165A", "HD-1160", "HD-1168",
    "HD-1148", "HD-808", "HD-1173", "HD-1161", "HD-1140", "HD-1063", "HD-1060",
    "HD-1125", "HD-1133", "HD-1131"
]

villas = [
    "HD-1182", "HD-1053", "HD-1169", "HD-1158", "HD-1130", "HD-1095", "HD-1151",
    "HD-1034", "HD-1159", "HD-1058", "HD-1048", "HD-1066", "HD-1106", "HD-1097",
    "HD-1083", "HD-1042", "HD-1132"
]

# Combine all properties
all_properties = apartments + villas

# Function to generate a schedule for a specified number of days
def generate_schedule(num_days):
    schedule = {}
    
    for day in range(1, num_days + 1):
        daily_posts = random.sample(all_properties, 4)
        
        schedule[f"Day {day}"] = {
            "16:9 video": daily_posts[0],
            "photo post": daily_posts[1],
            "reel": daily_posts[2],
            "story": daily_posts[3]
        }
    
    return schedule

# Generate the schedule for 30 days
num_days = 27
schedule = generate_schedule(num_days)

# Calculate statistics
apartment_count = sum(1 for posts in schedule.values() for prop in posts.values() if prop in apartments)
villa_count = sum(1 for posts in schedule.values() for prop in posts.values() if prop in villas)

# Save the schedule and statistics to a text file
with open("real_estate_social_media_schedule.txt", "w") as file:
    for day, posts in schedule.items():
        file.write(f"\n{day}\n")
        for post_type, property_ref in posts.items():
            file.write(f"  {post_type}: {property_ref}\n")
    
    file.write(f"\nTotal posts: {num_days * 4}\n")
    file.write(f"Apartment posts: {apartment_count}\n")
    file.write(f"Villa posts: {villa_count}\n")

print("Schedule has been saved to 'real_estate_social_media_schedule.txt'")

# Optional: Print the schedule to console as well
for day, posts in schedule.items():
    print(f"\n{day}")
    for post_type, property_ref in posts.items():
        print(f"  {post_type}: {property_ref}")

print(f"\nTotal posts: {num_days * 4}")
print(f"Apartment posts: {apartment_count}")
print(f"Villa posts: {villa_count}")