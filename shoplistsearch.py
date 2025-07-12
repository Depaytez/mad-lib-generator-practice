import random

# shopping list classification
print("Welcome to the Shopping List Search Program by Philip Depaytez!")
groceries = ["milk", "bread", "eggs"]
fruits = ["apple", "banana", "orange"]
vegetables = ["carrot", "broccoli", "spinach"]
dairy = ["cheese", "yogurt", "butter"]
meats = ["chicken", "beef", "pork"]

shopping_list = [groceries, fruits, vegetables, dairy, meats]
print("Here are the categories of items in your shopping list:")
for category in shopping_list:
    print(f"- {category}")

# Search for an item in the shopping list
def search_item(item):
    user_input = item.lower()
    for category in shopping_list:
        if item in category:
            print(f"{item} is found in the shopping list category: {category}")
            return
        else:
            print(f"{user_input} is not found in the shopping list category: {category}")

search_item(item=input("Enter the item you want to search for: ").lower())