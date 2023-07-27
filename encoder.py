from typing import List
from did import DidObject
from controller import Controller

def generate_did_floor(floor_code):
    if floor_code == "00":
        return "G"
    else:
        return floor_code


class PpsLgbEncoder:
    def encode(self, ppsids: List[str], username: str) -> List[DidObject]:
        result = []
        root_domain = Controller("ROOT")
        username_counts = {}
        
        for ppsid in ppsids:
            building_code = ppsid[:5]
            floor_code = ppsid[5:7]
            flat_number = ppsid[-2:]

            building_name = building_mapping.get(building_code, "Unknown\ building error,check again")
            floor_number = generate_did_floor(floor_code)

            # Check if the same address and username already exist
            address_key = f"{flat_number}/{floor_number}/{building_name}"
            if address_key not in username_counts:
                username_counts[address_key] = 1
                name = f"{username}"
            else:
                username_counts[address_key] += 1
                name = f"{username}{username_counts[address_key]}"
            
            did = DidObject(name=name, flat_number=flat_number, floor_number=floor_number, building_name=building_name,
                            area="SWB", district="hk", city="HK", country="CN")
            result.append(did)
        return result

        
building_mapping = {"19900" : "LGB"}
# class Encoder:
#     def encode(self, input_content) -> List[Controller]:
#         encoded_data = []

#         for ppsid in input_content:
#             flat_number = ppsid[-2:]
#             floor_code = ppsid[-4:-2]
#             building_code = ppsid[:5]
#             building_name = building_mapping.get(building_code, "Unknown") # Replace this with the actual building name from the ppsid
#             area = "SKB"  # Replace this with the actual area from the ppsid
#             district = "hk"  # Replace this with the actual district from the ppsid
#             city = "HK"  # Replace this with the actual city name from the ppsid
#             country = "CN"  # Replace this with the actual country from the ppsid

#             # Generate DID floor using the provided function
#             floor = generate_did_floor(floor_code)

#             # Create the Controller objects with the relevant information
#             did = DidObject(ppsid)
#             did.flat_number = flat_number
#             did.floor_number = floor
#             did.building_name = building_name
#             did.area = area
#             did.district = district
#             did.city = city
#             did.country = country

#             # Add the top-level controller to the list of encoded data
#             encoded_data.append(did)

#         return encoded_data