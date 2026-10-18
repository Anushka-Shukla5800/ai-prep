import json

with open(file="transactions.json",mode="r",encoding="utf-8") as file:
    transaction_data = json.load(file)

total ={}
for data in transaction_data:
    category = data['category']
    total[category]=total.get(category,0)+data['amount']

[print(key,value) for key,value in total.items()]