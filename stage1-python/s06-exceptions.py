import json

try:
    with open(file="complaints.json",mode="r",encoding="utf-8") as file:
        complaints = json.load(file)
except json.JSONDecodeError as e:
    print(f"The json file has some improper data,check : {e}")
except FileNotFoundError:
    print("The file is not found.")


    