print("name:T P Aswathi\nsec:o\nusn:1AY24AI109")
def print_table(table_data):
    col_widths = [max(len(str(item)) for item in col) for col in table_data]
    num_rows = len(table_data[0])

    for row in range(num_rows):
        row_str = ""
        for col in range(len(table_data)):
            row_str += str(table_data[col][row]).rjust(col_widths[col]) + ' '
        print(row_str)
def main():
    table_data = [
        ['Name', 'Alice', 'Bob', 'Charlie'],
        ['Age', '24', '30', '18'],
        ['City', 'New York', 'Paris', 'Berlin']
    ]

    print("Formatted Table:\n")
    print_table(table_data)
if __name__ == "__main__":
    main()
