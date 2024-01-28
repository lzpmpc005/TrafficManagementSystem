# Example: "NW 72 YTZ"
import re

class PlateRecognition:
    def __init__(self):
        pass

    def recognition_number_plate(self, number_plate: str):
        number_plate_upper = number_plate.replace(" ", "")
        number_plate_upper = number_plate.upper()
        if not self.__validation_number_plate(number_plate_upper):
            raise ValueError("Number plate format is not valid")

        [region, postal_area] = self.__local_memory_tag_identifier(number_plate_upper)

        age = self.__age_identifier(number_plate_upper)

        random_letters = number_plate_upper[-3:]

        return {
            "region": region,
            "postal_area": postal_area,
            "age_identifier": age,
            "random_latters": random_letters
        }

    def __validation_number_plate(self, number_plate):
        pattern = r'^[A-Y]{2}\d{2}[A-Z]{3}$'
        if re.match(pattern, number_plate):
            return True
        else:
            return False

    def __local_memory_tag_identifier(self, number_plate):
        region = {
            "A":  "Anglia",
            "B":  "Birmingham",
            "C":  "Cymru (Wales)",
            "D":  "Deeside",
            "E":  "Essex",
            "F":  "Forest And Fens",
            "G":  "Garden Of England",
            "H":  "Hampshire And Dorset",
            "K":  "No official mnemonic",
            "L":  "London",
            "M":  "Manchester and Merseyside",
            "N":  "North",
            "O":  "Oxford",
            "P":  "Preston",
            "R":  "Reading",
            "S":  "Scotland",
            "V":  "Severn Valley",
            "W":  "Anglia",
            "X":  "Personal Export",
            "Y":  "Yorkshire",
        }

        postal_area = {
            "A":  "Anglia",
            "B":  "Birmingham",
            "E":  "Essex",
            "F":  "Forest And Fens",
            "G":  "Garden Of England",
            "H":  "Hampshire And Dorset",
            "K":  "No official mnemonic",
            "L":  "London",
            "M":  "Manchester and Merseyside",
            "N":  "North",
            "O":  "Oxford",
            "P":  "Preston",
            "R":  "Reading",
            "S":  "Scotland",
            "V":  "Severn Valley",
            "W":  "Anglia",
            "X":  "Personal Export",
            "Y":  "Yorkshire",
        }

        number_region = region[number_plate[0]]
        number_postal_area = postal_area[number_plate[1]]

        return [number_region, number_postal_area]

    def __age_identifier(self, number_plate: str):
        age_identifier = int(number_plate[2:4])
        register_month = ''
        register_year = None

        if age_identifier < 50:
            register_month = "March to August"
            register_year = 2000 + age_identifier
        else:
            register_month = "September to February"
            register_year = 2000 + (age_identifier - 50)

        return {
            "register_month": register_month,
            "register_year": register_year
        }
    
# if __name__ == "__main__":
#     #ONLY Currenct number plate
#     number_plate = "NY32YTZ"

#     recognition = PlateRecognition()
#     print(recognition.recognition_number_plate(number_plate))
