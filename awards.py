"""
Program to compute the times spent for athlets on
a triathlon with: Swimming , cycling an running

Pseudo code
1. I am declaring a variable called total_time
2. Also declaring individual time variables for each event
3. the times per event will be requested and stored in an integer type
4. each entered event time will be aded to the total time list
5. the final list will be summed to get total time
6. analysis will then start on the awards based on total time
"""

# reviewer  comments
# you dont want to calculate the sum in the conditional statement
# once i have found the lower bound, use the 
# this function wil return a value to be passed to awards fucntons later
def get_event_times():
    total_time = 0
    time_swimming = int(input("Enter time in minutes "
                              "athlete completed swmming exercise: "))
    total_time += time_swimming
    time_cycling = int(input("Enter time in minutes "
                             "athlete completed cycling exercise: "))
    total_time += time_cycling
    time_running = int(input("Enter time in minutes athlete "
                             "completed running exercise: "))
    total_time += time_running

    return total_time
    

def awards_method_one():
    prizes = ["Provincial colors", "Half Provincial Colors",
              "Provincial Scroll", "Verbal Commendation"]
    total_time = 0
    time_swimming = int(input("Enter time in minutes athlete "
                              "completed swmming exercise: "))
    time_cycling = int(input("Enter time in minutes athlete "
                             "completed cycling exercise: "))
    time_running = int(input("Enter time in minutes athlete "
                             "completed running exercise: "))

    total_time = time_swimming + time_cycling + time_running
    print(total_time)

    # analyse time for award presesntation
    if(total_time >= 0 and total_time <= 100):
        print(f"Good job athlete, you won the {prizes[0]} "
              "with a total time of {total_time} mins")
    elif(total_time >= 101 and total_time <= 105):
        print(f"Good job athlete, you won the {prizes[1]} "
              "with a total time of {total_time} mins")
    elif(total_time >= 106 and total_time <= 110):
        print(f"Good job athlete, you won the {prizes[2]} "
              "with a total time of {total_time} mins")
    elif(total_time >= 111):
        print(f"Good job athlete, you gained {prizes[3]} "
              "with a total time of {total_time} mins")
    else:
        print("No known time recorded")

def awards_method_two():
    prizes = ["Provincial colors", "Half Provincial Colors",
              "Provincial Scroll", "Verbal Commendation"]
    total_time = []
    time_swimming = int(input("Enter time in minutes athlete "
                              "completed swmming exercise: "))
    total_time.append(time_swimming)
    time_cycling = int(input("Enter time in minutes athlete "
                             "completed cycling exercise: "))
    total_time.append(time_cycling)
    time_running = int(input("Enter time in minutes athlete "
                             "completed running exercise: "))
    total_time.append(time_running)

    # display time taken
    print(sum(total_time))

    # analyse time for award presesntation
    if(sum(total_time) >= 0 and sum(total_time) <= 100):
        print(f"Good job athlete, you won the {prizes[0]} "
              "with a total time of {sum(total_time)} mins")
    elif(sum(total_time) >= 101 and sum(total_time) <= 105):
        print(f"Good job athlete, you won the {prizes[1]} "
              "with a total time of {sum(total_time)} mins")
    elif(sum(total_time) >= 106 and sum(total_time) <= 110):
        print(f"Good job athlete, you won the {prizes[2]} "
              "with a total time of {sum(total_time)} mins")
    elif(sum(total_time) >= 111):
        print(f"Good job athlete, you gained {prizes[3]} "
              "with a total time of {total_time} mins")
    else:
        print("No known time recorded")

# this takes an argument total time
def awards_method_three(total_time):
    prizes = ["Provincial colors", "Half Provincial Colors",
              "Provincial Scroll", "Verbal Commendation"]

    # display time taken
    print(f"Total elapsed time is: {total_time}")
    
    # analyse time for award presentation
    if(total_time >= 0 and total_time <= 100):
        print(f"Good job athlete, you won the {prizes[0]} "
              "with a total time of {total_time} mins")
    elif(total_time >= 101 and total_time <= 105):
        print(f"Good job athlete, you won the {prizes[1]} "
              "with a total time of {total_time} mins")
    elif(total_time >= 106 and total_time <= 110):
        print(f"Good job athlete, you won the {prizes[2]} "
              "with a total time of {total_time} mins")
    elif(total_time >= 111):
        print(f"Good job athlete, you gained {prizes[3]} "
              "with a total time of {total_time} mins")
    else:
        print("No known time recorded")
        
# main method here
def main():
    # testing the get_event_times function
    elapsed_time = get_event_times()
    
    print("testing method one")
    awards_method_one()
    print("testing method two")
    awards_method_two()
    print("testing method three")
    awards_method_three(elapsed_time)
    

if __name__ == '__main__':
    main()
