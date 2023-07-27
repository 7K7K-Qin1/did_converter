# from typing import List
# from did import DidObject

# class PpsLgbDecoder:
#     def decode(self, processed_data: List[DidObject]) -> List[dict]:
#         decoded_data = []
#         for data in processed_data:
#             name = data.name
#             did_str = self.encode_to_did_str(data)

#             decoded_data.append({"name": name, "did_str": did_str})

#         return decoded_data

#     def encode_to_did_str(self, data: DidObject) -> str:
#         return "/".join([
#             data.building_name,
#             data.floor_number,
#             "SWB/hk/HK",
#             data.flat_number
#         ])
from typing import List
from did import DidObject

class PpsLgbDecoder:
    def decode(self, processed_data: List[DidObject]) -> List[dict]:
        result = []
        for data in processed_data:
            if data.block == "":
                did_str = data.name + "/" + data.flat_number + "/" + data.floor_number + "/"+ data.building_name + "/" + data.area + "/" + data.district + "/" + data.city + "/" + data.country
            else:
                did_str = data.name + "/" + data.flat_number + "/" + data.floor_number + "/" + data.block + "/" + data.building_name + "/" + data.area + "/" + data.district + "/" + data.city + "/" + data.country
            result.append({ "did_str": did_str})
        return result
