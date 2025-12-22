chai_order = dict(type="Masala chai", size="Large", sugar=2)

chai_recipe = {}

chai_recipe["base"] =  "Black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")

del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar":1}
# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamon": "Crushed", "ginger":"sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")
