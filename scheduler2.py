import random
from collections import deque

# Property listings
apartments = [
    'HD-1185', 'HD-1153Y', 'HD-1153K', 'HD-1144', 'HD-1052', 'HD-1180', 'HD-1175',
    'HD-1099', 'HD-1127', 'HD-1118', 'HD-1142', 'HD-1156', 'HD-1126',
    'HD-1153L', 'HD-1179A', 'HD-1162', 'HD-1101', 'HD-1165A', 'HD-1160', 'HD-1168',
    'HD-1148', 'HD-808', 'HD-1173', 'HD-1161', 'HD-1140', 'HD-1063', 'HD-1060',
    'HD-1125', 'HD-1133', 'HD-1131'
]

villas = [
    'HD-1182', 'HD-1053', 'HD-1169', 'HD-1158', 'HD-1130', 'HD-1095', 'HD-1151',
    'HD-1034', 'HD-1159', 'HD-1058', 'HD-1048', 'HD-1066', 'HD-1106', 'HD-1097',
    'HD-1083', 'HD-1042', 'HD-1132'
]

# Combine all properties
all_properties = apartments + villas

# Create a dictionary to track usage of each property
property_usage = {prop: {'Video': 0, 'Photo': 0, 'Story': 0} for prop in all_properties}

# Create deques for each post type
video_deque = deque(random.sample(all_properties, len(all_properties)))
photo_deque = deque(random.sample(all_properties, len(all_properties)))
story_deque = deque(random.sample(all_properties, len(all_properties)))

def get_next_property(deque_type, post_type):
    for _ in range(len(deque_type)):
        prop = deque_type[0]
        deque_type.rotate(-1)
        if property_usage[prop][post_type] == min(property_usage[prop].values()):
            property_usage[prop][post_type] += 1
            return prop
    # If we've gone through the entire deque without finding a suitable property,
    # just return the first one (this should rarely happen)
    prop = deque_type[0]
    property_usage[prop][post_type] += 1
    return prop

def generate_daily_schedule(day):
    schedule = {
        "Day": day,
        "Video": [get_next_property(video_deque, 'Video') for _ in range(2)],
        "Photo": [get_next_property(photo_deque, 'Photo') for _ in range(2)],
        "Story": [get_next_property(story_deque, 'Story') for _ in range(2)]
    }
    return schedule

# Open a file to write the schedule
with open('social_media_schedule.txt', 'w') as file:
    # Generate schedule for 30 days
    for day in range(1, 31):
        daily_schedule = generate_daily_schedule(day)
        
        # Write to console
        print(f"Day {daily_schedule['Day']}:")
        print(f"  Video: {daily_schedule['Video']}")
        print(f"  Photo: {daily_schedule['Photo']}")
        print(f"  Story: {daily_schedule['Story']}")
        print()
        
        # Write to file
        file.write(f"Day {daily_schedule['Day']}:\n")
        file.write(f"  Video: {daily_schedule['Video']}\n")
        file.write(f"  Photo: {daily_schedule['Photo']}\n")
        file.write(f"  Story: {daily_schedule['Story']}\n")
        file.write("\n")

    # Write usage statistics to both console and file
    print("Property Usage Statistics:")
    file.write("Property Usage Statistics:\n")
    for prop in all_properties:
        stats = f"{prop}: {property_usage[prop]}"
        print(stats)
        file.write(stats + "\n")

print("Schedule has been saved to 'social_media_schedule.txt'")