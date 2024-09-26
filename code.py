print ("Starting")

import board
import digitalio
import time

COLUMNS = (digitalio.DigitalInOut(board.GP16), digitalio.DigitalInOut(board.GP17))
for column in COLUMNS:
    column.direction = digitalio.Direction.OUTPUT

ROWS = (digitalio.DigitalInOut(board.GP13), digitalio.DigitalInOut(board.GP15))

for row in ROWS:
    row.switch_to_input(pull=digitalio.Pull.DOWN)

def set_active_column(column, idx):
    """Turn off all columns except the indicated column which is turned on."""
    for idx2, column2 in enumerate(COLUMNS):
        if idx2 != idx:
            column2.value = False
    column.value = True

def get_active_key():
    """Scan the matrix for the active key, if any."""
    for col_idx, column in enumerate(COLUMNS):
        #set_active_column(column, col_idx)
        for other_column_idx, other_column in enumerate(COLUMNS):
            if other_column_idx != col_idx:
                other_column.value = False
            else:
                other_column.value = True
        for row_idx, row in enumerate(ROWS):
            if row.value:
                return (row_idx, col_idx)


if __name__ == '__main__':
    print("yodawg")
    while True:
        active_key = get_active_key()
        if (active_key):
            print(active_key)
            time.sleep(0.5)
