print("name:T P Aswathi\nsec:o\nusn:1AY24AI109")
def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        item_total += count
    print(f"Total number of items: {item_total}")

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory
def main():
    inventory = {
        'gold coin': 42,
        'rope': 1,
        'dagger': 1,
        'torch': 6,
        'arrow': 12
    }
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    print("Before collecting loot:")
    display_inventory(inventory)

    print("\nCollecting loot...")
    inventory = add_to_inventory(inventory, dragon_loot)

    print("\nAfter collecting loot:")
    display_inventory(inventory)
if __name__ == "__main__":
    main()
