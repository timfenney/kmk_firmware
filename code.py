print ("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.row_pins = (board.GP13, board.GP15)
keyboard.col_pins = (board.GP16, board.GP17)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A, KC.B],
    [KC.C, KC.D]
]

if __name__ == '__main__':
    keyboard.go()
