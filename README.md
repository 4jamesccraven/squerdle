# squerdle
A simple Python script that I made to cheat at Wordle.

## ... Why?
My friends decided to add a Wordle bot to our Discord server, and I thought it
would be fun to automate the process.

## Usage
Make a guess at the Wordle and pass information the corresponding information
to squerdle using the following options:

```
python -m squerdle \
    -c abc \           # Indicate the word contains a, b, and c at some position.
    -v def \           # Indicate the word does not contain d, e, or f.
    --ck g=1 h=2 \     # Indicate that g is in the first position and h is in the second position.
    --vk i=3 j=4 \     # Indicate that i is not in the third position and j is not in the fourth position.
```
