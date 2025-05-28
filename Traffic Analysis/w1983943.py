
"""
****************************************************************************
Additional info
 1. I declare that my work contins no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID: w1983943
 4. Date: 19/11/2024
****************************************************************************
links for reference:
https://www.w3schools.com/python/ref_func_enumerate.asp
https://www.w3schools.com/python/python_lists.asp (including all subtopics)
https://www.youtube.com/playlist?list=PL5FKO8x2yHG-UM-6otrJ0aqyg_wWsfb0B (playlist for the graphics module)
"""

from graphics import *  
import csv
import math

data_list = []

def date_input():
    while True:
        try:
            day = int(input("Please enter the day of the survey in the format DD: "))
            if day < 1 or day > 31:
                print("Out of range - values must be in the range 1 to 31.\n")
                continue

            month = int(input("Please enter the month of the survey in the format MM: "))
            if month < 1 or month > 12:
                print("Out of range - values must be in the range 1 to 12.\n")
                continue

            year = int(input("Please enter the year of the survey in the format YYYY: "))
            if year < 2000 or year > 2024:
                print("Out of range - values must range from 2000 to 2024.\n")
                continue

            return day, month, year # using a tuple to store and return the 3 inputs 
        except ValueError:
            print("Integer required.")

def load_csv_data(filename): 
    global data_list
    data_list= []
    try:
        with open(filename, 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                data_list.append(row)
        print("Data loaded successfully.")
        return header
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist. Please check the date and try again.")
        return None

def requested_data(day, month, year): # using this, the the tuple will lead to the filename based on the input and will display the following error message if the date doesn't match
    if not data_list:  
        print("No data to process.")
        return

    selected_file = f"traffic_data{day:02d}{month:02d}{year}.csv"
    print(f"Selected CSV file: {selected_file}")
    # the code  below all takes a similar approach into calculating the number of vehicles etc with a condition required for each one to check if the row needed to be read actually exists
    total_vehicles = len(data_list)
    
    # finds sum of rows in data_list where the 9th column (row 8) indicates the vehicle type is a truck.
    total_trucks = sum(1 for row in data_list if len(row) > 8 and row[8] == "Truck")
    
    # finds sum of rows in data_list where the 10th column (row 9) is "TRUE"
    electric_vehicles = sum(1 for row in data_list if len(row) > 9 and row[9].strip().upper() == "TRUE")

    # finds sum of rows where the 9th column (row 8) indicates the vehicle is one of bicycle, motorcycle or scooter.
    two_wheeled_vehicles = sum(1 for row in data_list if len(row) > 8 and row[8] in ["Bicycle", "Motorcycle", "Scooter"])

    # finds sum of rows where  a bus is at the junction  Elm Avenue/rabbit road and heading north using row (0) row (4) and row(8)
    northbound_buses = sum(1 for row in data_list if len(row) > 4 and row[0] == "Elm Avenue/Rabbit Road" and row[4].strip().upper() == "N" and row[8] == "Buss")

    # finds sum of rows where the entry direction (row 3) matches the exit direction (row 4), meaning the vehicle went straight through the junction.
    straight_through_vehicles = sum(1 for row in data_list if len(row) > 3 and row[3] == row[4])

    # Calculates the percentage of trucks by dividing total trucks by the total number of vehicles and multiplying by 100
    trucks_percentage = round((total_trucks / total_vehicles * 100)) if total_vehicles > 0 else 0

    # finds sum of rows where the 9th column (row 8) indicates the vehicle is a bicycle
    bicycles = sum(1 for row in data_list if len(row) > 8 and row[8] == "Bicycle")

    # calculates average bikes per hour  by dividing the total by 24
    avg_bicycles_per_hour = round(bicycles / 24)

     # finds sum where rows where the recorded speed (row 7) exceeds the speed limit (row 6)
    over_speed_limit = sum(1 for row in data_list if len(row) > 7 and int(row[7]) > int(row[6]))

     # finds sum where the junction (row 0) is Elm Avenue/Rabbit Road   
    elm_vehicles = sum(1 for row in data_list if len(row) > 0 and row[0] == "Elm Avenue/Rabbit Road")

    # Counts rows where the junction (row 0) is Hanley Highway/Westway.    
    hanley_vehicles = sum(1 for row in data_list if len(row) > 0 and row[0] == "Hanley Highway/Westway")


    scooters_at_elm = sum(1 for row in data_list if len(row) > 8 and row[0] == "Elm Avenue/Rabbit Road" and row[8] == "Scooter")
    
    scooters_percentage = round((scooters_at_elm / elm_vehicles * 100)) if elm_vehicles > 0 else 0
    
    vehicle_counts_by_hour_elm = [0] * 24
    
    vehicle_counts_by_hour_hanley = [0] * 24
    for row in data_list:
        if len(row) > 2:
            hour = int(row[2].split(":")[0])
            if row[0] == "Elm Avenue/Rabbit Road":
                vehicle_counts_by_hour_elm[hour] += 1
            elif row[0] == "Hanley Highway/Westway":
                vehicle_counts_by_hour_hanley[hour] += 1

    busiest_hour_count = max(vehicle_counts_by_hour_hanley)
    busiest_hours = [f"Between {hour}:00 and {hour + 1}:00"
                     for hour, count in enumerate(vehicle_counts_by_hour_hanley)
                     if count == busiest_hour_count]

    
    light_rain_hours = sum(1 for row in data_list if len(row) > 5 and row[5] == "light rain")

    # Outcomes are printed and put into a list. Results file gets created and outcomes gets stored everytime its run
    outcomes = [
        f"The total number of vehicles recorded for this date is: {total_vehicles}.\n",
        f"The total number of trucks recorded for this date is: {total_trucks}.",
        f"The total number of electric vehicles for this date is: {electric_vehicles}.",
        f"The total number of two-wheeled vehicles for this date is: {two_wheeled_vehicles}.",
        f"The total number of Busses leaving Elm Avenue/Rabbit Road heading North is: {northbound_buses}.",
        f"The total number of Vehicles through both junctions not turning left or right is: {straight_through_vehicles}.\n",
        f"The percentage of total vehicles recorded that are trucks for this date is: {trucks_percentage}%.",
        f"The average number of Bikes per hour for this date is: {avg_bicycles_per_hour}.\n",
        f"The total number of Vehicles recorded as over the speed limit for this date is : {over_speed_limit}.\n",
        f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is : {elm_vehicles}.",
        f"The total number of vehicles recorded through Hanley Highway/Westway junction is: {hanley_vehicles}.\n",
        f"{scooters_percentage}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.\n",
        f"The highest number of vehicles in an hour on Hanley Highway/Westway is: {busiest_hour_count}.",
        f"The most vehicles through Hanley Highway/Westway were recorded between: {', '.join(busiest_hours)}.\n",
        f"The number of hours of rain for this date is: {light_rain_hours}."
    ]

    print("\nResults:")
    for outcome in outcomes:
        print(outcome)

    with open("results.txt", "a") as file:
        file.write("Results for processed data:\n")
        file.write("\n".join(outcomes) + "\n\n")
    print("Results saved to results.txt.")

    draw_histogram(vehicle_counts_by_hour_elm, vehicle_counts_by_hour_hanley, day, month, year)

def draw_histogram(vehicle_counts_by_hour_elm, vehicle_counts_by_hour_hanley, day, month, year):
    try:
        win = GraphWin("Histogram", 1000, 600)
        win.setBackground("lavender")

        x_axis = Line(Point(50, 552), Point(950, 552))
        x_axis.draw(win)
        

        title = Text(Point(500, 20), f"Histogram of Vehicle Frequency per hour ({day:02d}/{month:02d}/{year})")
        title.setSize(12)
        title.setStyle("bold")
        title.draw(win)

        for i in range(24):
            hour_label = Text(Point(70 + (i * 38), 570), f"{i}:00")
            hour_label.setSize(8)
            hour_label.draw(win)

        max_count = max(max(vehicle_counts_by_hour_elm), max(vehicle_counts_by_hour_hanley))
        if max_count == 0:
            max_count = 1  # this is to  avoid dividing by 0

         # this draws bars for each hour, side by side for the two junctions together
        for i in range(24):
            # Bar for Elm Avenue/Rabbit Road
            bar_height_elm = (vehicle_counts_by_hour_elm[i] / max_count) * 500
            bar_elm = Rectangle(Point(50 + (i * 38), 550 - bar_height_elm), Point(65 + (i * 38), 550))
            bar_elm.setFill("light green")
            bar_elm.setOutline("light green") 
            bar_elm.draw(win)

            
            value_label_elm = Text(Point(57 + (i * 38), 550 - bar_height_elm - 10), str(vehicle_counts_by_hour_elm[i]))
            value_label_elm.setSize(8)
            value_label_elm.setTextColor("light green") 
            value_label_elm.draw(win)

            # This is the bar for Hanley Highway/Westway (taking the same approach as the previous junction)
            bar_height_hanley = (vehicle_counts_by_hour_hanley[i] / max_count) * 500
            bar_hanley = Rectangle(Point(65 + (i * 38), 550 - bar_height_hanley), Point(80 + (i * 38), 550))
            bar_hanley.setFill("turquoise")
            bar_hanley.setOutline("turquoise")  
            bar_hanley.draw(win)

            value_label_hanley = Text(Point(72 + (i * 38), 550 - bar_height_hanley - 10), str(vehicle_counts_by_hour_hanley[i]))
            value_label_hanley.setSize(8)
            value_label_hanley.setTextColor("turquoise")
            value_label_hanley.draw(win)

        #this is for the colour coded legend on the left side 
        legend_title = Text(Point(100, 80), "Legend")
        legend_title.setSize(10)
        legend_title.setStyle("bold")
        legend_title.draw(win)
        
        #colour coded box for the legend with precise coordinates
        blue_box = Rectangle(Point(80, 100), Point(100, 120))
        blue_box.setFill("light green")
        blue_box.setOutline("black")
        blue_box.draw(win)
        legend_elm = Text(Point(175, 110), "Elm Avenue/Rabbit Road")
        legend_elm.setSize(10)
        legend_elm.draw(win)

        red_box = Rectangle(Point(80, 130), Point(100, 150))
        red_box.setFill("turquoise")
        red_box.setOutline("black")
        red_box.draw(win)
        legend_hanley = Text(Point(180, 140), "Hanley Highway/Westway")
        legend_hanley.setSize(10)
        legend_hanley.draw(win)

        # the histogram window needs to be open and running in order for this to work
        print("Click anywhere in the window to close it.")
        if not win.isClosed():  
            win.getMouse()
        win.close()
    except GraphicsError as e:
        print(f"Graphics error: {e}")

def main():
    while True:
        day, month, year = date_input()
        filename = f"traffic_data{day:02d}{month:02d}{year}.csv"
        header = load_csv_data(filename)

        if header:
            requested_data(day, month, year)

        #This should only pop after the histogram closes
        response = input("Do you want to select a data file for a different date? Y/N: ").strip().lower()
        if response == 'n':
            print("Exiting the program. Goodbye!")
            break
        elif response != 'y':
            print('Please enter "Y" or "N"')

if __name__ == "__main__":
    main()
