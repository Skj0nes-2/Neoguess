# Neoguess
### The Most Advanced Combo Finder

## Installation
To install Neofire use wget to grab main.py
```
wget https://github.com/Skj0nes-2/Neoguess/releases/download/Neoguess/neoguess
```

## How to use
To use run main.py with Python then enter your digit list and combo length.
```
python neoguess
```

## How it works
Neoguess works by assembling a list of your desired characters, duplicating the characters until the combo length requirement is satisfied, and using itertools.product() to assemble these lists of characters into viable combinations. The script then removes unnecessary list characters and seperates each combo onto a new line. Finally Neoguess writes all the combinations into a file at your location.
