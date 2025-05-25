print("name: Aswathi\nsec:o\nusn:1AY24AI109")
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


# Example inventory and loot
player_inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1
}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Before adding loot
print("Before loot:")
display_inventory(player_inventory)

# Add loot to inventory
player_inventory = add_to_inventory(player_inventory, dragon_loot)

# After adding loot
print("After loot:")
display_inventory(player_inventory)
