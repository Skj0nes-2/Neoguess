# Neoguess
### The Most Advanced Combo Finder

## Installation
To install Neoguess, use wget to grab the installer.
```
wget https://github.com/Skj0nes-2/Neoguess/releases/download/1.5.0/MakeFile
```
Then install Neoguess,
```
sudo make
```

## To use
Run,
```
neoguess
```
To specify characters and combo length beforehand, run, 
```
neoguess '[CHARACTERS]' [COMBO LENGTH]
```
Replace [CHARACTERS] with the characters to use in the combo and replace [COMBO LENGTH] with an integer value indicating the length of every combo.
For example:
```
neoguess 'a!1' 4
```
This will generate 4-digit codes with the characters ' a ', ' ! ', and ' 1 '.

## How it works
Neoguess works by assembling a list of your desired characters, duplicating the characters until the combo length requirement is satisfied, and using itertools.product() to construct these lists of characters into viable combinations. The script then removes unnecessary list characters and separates each combo onto a new line. Finally, Neoguess writes all the combinations into a file at your location.
