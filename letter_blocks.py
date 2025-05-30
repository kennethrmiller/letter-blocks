import streamlit as st
import itertools
import nltk

st.title("Letter Block Word Finder")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Download the 'words' package if not already downloaded
nltk.download('words')

# Get the English dictionary words
english_words = set(w.lower() for w in nltk.corpus.words.words())

def find_words(cubes, word_length):
    """
    Find words that can be spelled using the letters on the cubes.

    Args:
        cubes (list): List of cubes, each cube is a string of 4 letters.
        word_length (int): Length of words to find.

    Returns:
        list: List of words that can be spelled.
    """
    # Generate all possible combinations of letters
    combinations = itertools.product(*cubes)

    # Filter combinations that form valid English words
    words = []
    for combo in combinations:
        word = ''.join(combo).lower()
        if len(word) == word_length and word in english_words:
            words.append(word)

    return words

# Define the cubes
cubes = [
    'NDH',  # Cube 1
    'EIP',  # Cube 2
    'MPG',  # Cube 3
    'QAI',  # Cube 4
    'LOR',  # Cube 5
    'LAWS',  # Cube 6
    'ETJ',  # Cube 7
    'VOHR',  # Cube 8
    'ABCD',  # Cube 9
    'YGC',  # Cube 10
    'HELR',  # Cube 11
    'SDNW',  # Cube 12
    'SOAC',  # Cube 13
    'TNWY',  # Cube 14
    'TVUO',  # Cube 15
    'FIKM'   # Cube 16
]
# How many block sets do you have?
block_sets = st.number_input("How many sets of blocks do you have?", min_value = 1, max_value = 100, value = 1)

blocks = cubes * block_sets

# Find words of length 4 (adjust word_length as needed)
word_length = st.number_input("Word Length", min_value=1, max_value=16, value=4)
words = find_words(blocks, word_length)

print(f"Words of length {word_length}:")
for word in set(words):  # Use set to remove duplicates
    print(word)
