print("name:T P Aswathi\nsec:o\nusn:1AY24AI109")
def display_inventory(inventory):
    print("Inventory:")
    total_items = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        total_items += count
    print(f"Total number of items: {total_items}\n")
def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory
player_inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1
}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print("Before loot:")
display_inventory(player_inventory)
o_inventory(player_inventory, dragon_loot)
print("After loot:")
display_inventory(player_inventory)
