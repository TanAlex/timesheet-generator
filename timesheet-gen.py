import random
import csv


DAYS = 5
MAX_HOUR = [2, 3, 3, 2]
TOTAL_HOURS = [8.5, 10.5, 10, 8.5]
# May 
# DAYS = 22
# MAX_HOUR = [2, 3, 3, 2, 2, 2, 5, 2, 2, 2, 2]
# TOTAL_HOURS = [8.5, 34.5, 34.5, 8.5, 8.5, 8.5,54.5,0.00,0.00,0.00,8.5]
# June 
# DAYS = 22
# MAX_HOUR = [2, 3, 3, 2, 2, 2, 5, 2, 2, 2, 2]
# TOTAL_HOURS = [8.25, 33, 33, 8.25, 8.25, 8.25, 57.75, 0, 0, 0, 8.25]

COLUMN_NAMES = ['Total Hours'] + [f'Day {i+1}' for i in range(DAYS)]
# TIME_FACTOR is the number of hour slots in an hour,
# e.g. 4 means 15 minute slots, 2 means 30 minute slots
TIME_FACTOR = 4
MAX_HOUR_PER_DAY = 7.5


def generate_timesheet(total_hours):
    # Open a CSV file for writing
    with open('timesheet.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(COLUMN_NAMES)

        # Generate a list of time slots for each task
        total_per_day = [0 for _ in range(DAYS)]
        for i in range(len(total_hours)):
            total_hour = total_hours[i]
            max_hour = MAX_HOUR[i]

            # Calculate the total number of half-hour slots needed
            total_slots = int(total_hour * TIME_FACTOR)

            # Generate a list of random half-hour slots for this task
            slots_per_day = [0 for _ in range(DAYS)]
            
            generated_slots = 0
            while generated_slots < total_slots:
                days = list(range(DAYS))
                random.shuffle(days)
                # save generated_slots
                original_generated_slots = generated_slots
                for j in days:

                    # Calculate the maximum and minimum half-hour slots for this day
                    room_left = max(0, MAX_HOUR_PER_DAY * TIME_FACTOR - total_per_day[j])
                    max_slots = int(min(slots_per_day[j] + room_left, max_hour * TIME_FACTOR))
                    # if we are calculating the last task, we need to make sure we use up all the remaining slots
                    max_slots = max_slots if i != len(total_hours) -1 else slots_per_day[j] + room_left
                    min_slots = int(min(slots_per_day[j], max_slots))

                    # Generate a random half-hour slot within the limits
                    slot = random.randint(min_slots, max_slots)

                    # If adding this slot would exceed the remaining total, m
                    if generated_slots + int(slot) - slots_per_day[j] > total_slots:
                        # Adjust the slot to fit the remaining total
                        slot = (total_slots - generated_slots)

                    # Update slot to the list and update the generated total
                    generated_slots = generated_slots + int(slot) - slots_per_day[j]
                    total_per_day[j] = total_per_day[j] + slot - slots_per_day[j]
                    slots_per_day[j] = slot
                    

                row = [total_hour, generated_slots] + [f'{slot/TIME_FACTOR:.2f}' for slot in slots_per_day]
                print(row); print(total_per_day)
                if generated_slots == original_generated_slots:
                    print("Not able to assign hours to this task. You may need to increase the maximum hours per day.")
                    break
            row = [total_hour] + [f'{slot/TIME_FACTOR:.2f}' for slot in slots_per_day]
            print(row); print(total_per_day)
            writer.writerow(row)

generate_timesheet(TOTAL_HOURS)
