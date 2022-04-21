'''Type annotations used with data abstraction

PROBLEM: Not all sequence types in Python support concatenation.
'''

# We need to import some types!
from typing import Sequence

def my_replace(s: Sequence, old: Sequence, new: Sequence) -> Sequence:
    """Returns a string replacing all occurrences of old with new."""
    i: int = 0           # tracks where we are in the input string
    j: int = len(old)    # skip-ahead amount for index calculations
    new_s: Sequence = s[0:0]  # the new string we're building

    while i < len(s):
        if s[i:i+j] == old:
            new_s = new_s + new
            i += j
        else:
            new_s = new_s + s[i:i+1]
            i += 1

    return new_s


def main() -> None:
    # Create a string object with a line from The Cat in the Hat
    the_line: str = 'The Cat in the Hat!'
    print(the_line)
    the_line = my_replace(the_line, 'Hat', '\N{top hat}')
    print(the_line)

    # Create a representation of the objects on my shelf
    stuffed_lion: str = '\N{lion face}'
    kids_pic: str = 'kids.jpg'
    textbook: str = 'cs50y.scriv'
    favorite_cd: str = 'BornToRun.mp3'
    novel: str = 'CatInTheHat.txt'

    # Create a sequence object that represents my shelf
    shelf: list = [stuffed_lion, kids_pic, textbook, favorite_cd, novel]
    print(shelf)

    # Make it look like our textbook has been opened on my shelf
    shelf = my_replace(shelf, [textbook], ['\N{open book}'])
    print(shelf)

if __name__ == '__main__':
    main()
