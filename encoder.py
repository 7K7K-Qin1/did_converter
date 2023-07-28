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
            building_code = ppsid[:4]
            block_code = int(ppsid[4:6])
            floor_code = ppsid[6:8]
            flat_number = ppsid[8:]

            building_name = building_mapping.get(
                building_code, "Unknown\ building error,check again")
            floor_number = generate_did_floor(floor_code)

            # Check if the same address and username already exist
            block = block_number_mapping.get(block_code, "Unknown")
            if block == "":
                address_key = f"{flat_number}/{floor_number}/{building_name}"
            else:
                address_key = f"{flat_number}/{floor_number}/{block}/{building_name}"
            # print(address_key)
            if address_key not in username_counts:
                username_counts[address_key] = 1
                name = f"{username}"
            else:
                username_counts[address_key] += 1
                name = f"{username}{username_counts[address_key]}"

            did = DidObject(name=name, flat_number=flat_number, floor_number=floor_number, block=block, building_name=building_name,
                            area="SWB", district="hk", city="HK", country="CN")
            result.append(did)
        return result


building_mapping = {"0199": "LGB", "0671": "HealthyGardens"}
block_number_mapping = {0: "", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L",
                        13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
