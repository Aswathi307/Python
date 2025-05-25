print("name:Aswathi\nsec:o\nusn:1AY24AI109")
def print_table(table_data):
   col_widths = [max(len(str(item)) for item in col) for col in table_data]

    # Find number of rows (assuming all columns are equal in length)
    num_rows = len(table_data[0])

    for row_idx in range(num_rows):
        for col_idx in range(len(table_data)):
            print(str(table_data[col_idx][row_idx]).rjust(col_widths[col_idx]), end=' ')
        print()  # Newline after each row


# Example table data
table = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

print_table(table)
