import json
import os

article_info = {
    "domain" : "tekkaboki",
    "language" : "python",
    "date" : "28/01/2024",
    "topic" : "holiday planning"
}
myJSON = json.dumps(article_info)

with open("tekkaboki.json", "w") as jsonfile:
    jsonfile.write(myJSON)
    tekk_file_path = os.path.basename("./tekkaboki.json")
    print(f"Written successfully to {tekk_file_path}")
    
    
# or using json.dumps() directly in one line

api_response_info = {
    200 : "Ok",
    204 : "No Content",
    301 : "Moved Permanently",
    400 : "Bad Request",
    401 : "Unauthorized",
    403 : "Forbidden",
    404 : "Not Found",
    500 : "Internal Server Error"
}

with open("res_codes.json", "w") as jsonfile:
    json.dump(api_response_info, jsonfile)
    rescodes_file_path = os.path.basename("./res_codes.json")
    print(f"Written successfully to {rescodes_file_path}")
    
    
# here i am setting up a json object with destinations and distances

destination_info = {
    "new york" : "2690.76",
    "berlin" : "800.35",
    "lagos" : "1050.98",
    "tokyo" : "3543.78",
    "abuja" : "900.32",
    "shanghai" : "2876.23",
    "paris" : "546.87",
    "cairo" : "735.11"
}

with open("dest_info.json", "w") as jsonfile:
    json.dump(destination_info, jsonfile)
    destinations_file_path = os.path.basename("./dest_info.json")
    print(f"Written successfully to {destinations_file_path}")
    
    
# here i am setting up a json object for the car rental

car_type_info = {
    "saloon" : "150",
    "jeep" : "250",
    "limo" : "450"
}

with open("car_info.json", "w") as jsonfile:
    json.dump(car_type_info, jsonfile)
    cartype_file_path = os.path.basename("./car_info.json")
    print(f"Written successfully to {cartype_file_path}")