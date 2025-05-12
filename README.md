# Neoguess
### The Most Advanced Combo Finder

## Installation
To install Neoguess, use wget to grab the main script.
```
wget https://github.com/Skj0nes-2/Neoguess/releases/download/1.5.0/neoguess
```

## How to use
To use, run main.py with Python, enter your digit list, and then the combo length.
```
python neoguess
```

## How it works
Neoguess works by assembling a list of your desired characters, duplicating the characters until the combo length requirement is satisfied, and using itertools.product() to construct these lists of characters into viable combinations. The script then removes unnecessary list characters and separates each combo onto a new line. Finally, Neoguess writes all the combinations into a file at your location.
