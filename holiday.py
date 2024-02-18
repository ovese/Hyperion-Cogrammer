# from pathlib import Path
 
# file_path = 'C:/Users/test.txt'
 
# # stem attribute extracts the file
# # name
# print(Path(file_path).stem)
 
# # name attribute returns full name
# # of the file
# print(Path(file_path).name)

# #########

# import os
 
# file_path = 'C:/Users/test.txt'
 
# file_name = os.path.basename(file_path)
# file = os.path.splitext(file_name)
 
# print(file)  # returns tuple of string
 
# print(file[0] + file[1])

# #########

# import os
 
# file_path = 'C:/Users/test.txt'  # file path
 
# # using basename function from os 
# # module to print file name
# file_name = os.path.basename(file_path)
 
# print(file_name)

import requests # this is used to connect to or access API on the web or external
import json # will be used to read the json file which has been created previously
import re
import imageio
from skimage import transform,io

api_key = "6031df4aa0msh7b97af52b1313fcp18b2b9jsn57a5419afcdf" # key for rapidapi


class UncapturedDestinationError(Exception):
    pass


class UnknownRideError(Exception):
    pass


class Holiday:
    def __init__(self, city_flight, num_nights, rental_days):
        self.city_flight = city_flight
        self.num_nights = num_nights
        self.rental_days = rental_days
    
    """
    Can I incorporate an API into my Python code.
    What the API will do is compute distance between cities given in the code
    Can I also add an API to do exchange rate computation
    
    """
    
    def connect_askpython(self):
        response_API = requests.get('https://www.askpython.com/')
        res_code = response_API.status_code
        print(res_code)
        
        return res_code
    
    def connect_askgmail(self):
        response_API = requests.post('https://gmail.googleapis.com/$discovery/rest?version=v1')
        res_code = response_API.status_code
        print(res_code)
        
        return res_code
    
    def connect_nasa(self):
        pass
        # url = "https://climate-change23.p.rapidapi.com/evidence"
        # # get json with information (including name and date) about Earth pictures
        # response = requests.get(url,
        # headers={
        # "X-RapidAPI-Host": "climate-change23.p.rapidapi.com",
        # "X-RapidAPI-Key": api_key
        # }
        # )
        # # convert json to Python object 
        # data = response.json()
        # print("Debug........")
        # print(data)
        # # create regex pattern to get separately year, month and day of an image
        # dates_pattern = r"^(?P<year>d{4})-(?P<month>d{2})-(?P<day>d{2})"
        # # download images and save each to ./images folder
        # for img in data['contextWrites']['to']:
        #     # get year, month and day with regex to create image url
        #     matches = re.search(dates_pattern, img['date'])
        #     year = matches.group('year')
        #     month = matches.group('month')
        #     day = matches.group('day')
        #     image_name = img['image']
        #     img_url = f'https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{image_name}.png'
        #     # save image to ./images folder
        #     img_data = requests.get(img_url).content
        #     with open(f'images/{image_name}.png', 'wb') as handler:
        #         handler.write(img_data)
            
        # index = range(len(data['contextWrites']['to']))
        # images = []
        # # resize images and create gif from them
        # for i in index:
        #     img_name = data["contextWrites"]["to"][i]["image"]   
        #     img = io.imread(f'images/{img_name}.png')
        #     small_img = transform.resize(img, (500, 500), mode='symmetric', preserve_range=True)
        #     images.append(small_img)
        # imageio.mimsave('images/earth500.gif', images)

    def flight_cost(self, city):
        fuel_price = 3.99 # aviation or jet-a1 cost per gallon
        route_demand = 0  # can be minimal, low, high or medium
        distance_tofro = 0  # will be extracted from API
        seat_inventory = 0
        taxes = 7 # given as a rate of prevailing inflation in percventage
        seasonal_variation = 0  # can be peak or off-peak
        promotion_sales = 10  # any sales promo offers in percentage
        exchange_rate = 0  # will be computed as departure-destination currencies
        
        # readeing from json dest_info file
        with open("dest_info.json") as dest:
            destinations = dest.read()
        
        # print(type(destinations))
        # print(destinations)
        parsed_destinations  = json.loads(destinations)
        # print(type(parsed_destinations)) # this is a dictionary
        print(parsed_destinations)
        
        my_destinations = []
        destination_distances = []
        for key, value in parsed_destinations.items():
            my_destinations.append(key)
            destination_distances.append(value)
            
        print(my_destinations)
        print(destination_distances)
            
        
        try:
            #where_to = input("Enter travel destination: ")
            where_to = city
            dist_km = 0.0
            if where_to == " ":
                print("No destination entered")
            elif where_to not in my_destinations:
                flight_fare = 0.0
                raise UncapturedDestinationError(f"{where_to}, is not a known destination we have ")
            else:
                for i in range(len(my_destinations)):
                    if where_to == my_destinations[i]:
                        dist_km = float(destination_distances[i])
                        flight_fare = (dist_km * fuel_price) + (taxes + promotion_sales)/100
        except UncapturedDestinationError as ude:
            print(ude)
        except UnboundLocalError as ule:
            print(ule)
        else:
            pass
            #flight_fare = (dist_km * fuel_price) + (taxes + promotion_sales)/100
        finally:
            print("Computed flight fare is done statically or dynamically")
            
        return flight_fare    
                        
                
    def hotel_cost(self, nights_spent):
        flat_rate = 100.0
        location  = 7
        reputation = 0
        seasonality = 1.5 # ranges from 1-5
        occupancy = 0 #  days in week when place is full or empty
        customer_type = 0 # BAR, group, corporate
        technology = 0
        vat = 10
        
        hotel_fee = (flat_rate*nights_spent* seasonality*location)* vat/100
        
        return hotel_fee
        
        
    def car_rental_cost(self, num_days):
        vat = 0
        # readeing from json dest_info file
        with open("car_info.json") as transport:
            cars = transport.read()
        
        # parse the returned cars python object into a dictionnary
        parsed_cars  = json.loads(cars)
        print(parsed_cars) # this is a dictionary
        
        # extract the price for the individual ride types
        ride_type = []
        ride_cost = []
        for key, value in parsed_cars.items():
            ride_type.append(key) # creates a list
            ride_cost.append(value) # creates another list of costs
        
        try:
            cost_of_ride = 0
            user_entry = input("Select a ride category (saloon, jeep or limo): ")
            if user_entry not in ride_type:
                raise UnknownRideError(f"{user_entry} is not a known transport option")
            else:
                for i in range(len(ride_type)):
                    if user_entry == ride_type[i]:
                        cost_of_ride = float(ride_cost[i])
        except UnknownRideError as ride_sel_error:
            print(ride_sel_error)
        else:
            if user_entry == "saloon":
                vat = 5
                cost_of_ride = cost_of_ride*num_days*vat/100
            elif user_entry == "jeep":
                vat = 7
                cost_of_ride = cost_of_ride*num_days*vat/100
            elif user_entry == "limo":
                vat = 9
                cost_of_ride = cost_of_ride*num_days*vat/100
        finally:
            print(f"{user_entry} selected as preferred transport")
            
        return cost_of_ride
    
    def compute_total_trip_cost(self, plane_cost, hotel_cost, car_rental):
        trip_cost = plane_cost+hotel_cost+car_rental
        print(f"Trip summary:\n"
              f"Travel cost:....................${plane_cost:,.2f}\n"
              f"Hotel cost......................${hotel_cost:,.2f}\n"
              f"Car rental cost.................${car_rental:,.2f}\n"
              f"Total trip cost.................${trip_cost:,.2f}")
        
        # write the trip summary to a file
        with open("trip_summary.txt","w") as my_trip:
            #trip_summary = my_trip.read()     
            my_trip.write("Trip summary:\n")
            my_trip.write(f"Travel cost:....................${plane_cost:,.2f}\n")
            my_trip.write(f"Hotel cost......................${hotel_cost:,.2f}\n")
            my_trip.write(f"Car rental cost.................${car_rental:,.2f}\n")
            my_trip.write("----------------------------------------------------\n")
            my_trip.write(f"Total trip cost.................${trip_cost:,.2f}\n")
            my_trip.write("====================================================")
            
        return trip_cost

                        
    
    def main(self):        
        print(f"Destination: {hol.city_flight}\n"
          f"Hotel stay: {hol.num_nights}\n"
          f"Car rental: {hol.rental_days}\n")
        computed_fare = self.flight_cost(self.city_flight.lower())
        print(f"The computed air fare for {self.city_flight} is: ${computed_fare:,.2f}")
        
        hotel_stay_fees = self.hotel_cost(self.num_nights)
        print(f"The computed hotel cost for {self.num_nights} nights is: ${hotel_stay_fees:,.2f}")
        
        car_rental_fees = self.car_rental_cost(self.rental_days)
        print(f"Car rental cost for {self.rental_days} days is: ${car_rental_fees:,.2f}")
        
        total_travel_cost = self.compute_total_trip_cost(computed_fare, hotel_stay_fees, car_rental_fees)
        print(f"Total trip cost to {self.city_flight} for {self.num_nights} days is: ${total_travel_cost:,.2f}")
        
    
if __name__ == "__main__":
    hol = Holiday("Berlin", 8, 7) # pass the parameters of the trip to the constructor
    hol.main()