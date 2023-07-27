import csv
from typing import List
from encoder import PpsLgbEncoder
from decoder import PpsLgbDecoder
from did import DidObject

class Core:
    def __init__(self):
        self.encoder = PpsLgbEncoder()
        self.decoder = PpsLgbDecoder()

    def execute(self, ppsids: List[str], username: str):
        processed_data = self.encoder.encode(ppsids, username)
        output_data = self.decoder.decode(processed_data)

        # Save the decoded data to output.csv
        with open("data/output.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["did_str"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(output_data)

