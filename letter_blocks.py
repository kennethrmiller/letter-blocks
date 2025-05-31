import streamlit as st
import itertools

st.title("Letter Block Word Finder")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

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
block_sets = st.slider("How many sets of blocks do you have?", min_value = 1, max_value = 10, value = 1)

blocks = cubes * block_sets

message = st.text_input("Type the message you're trying to spell",value="happy",max_chars=block_sets*16).replace(" ","")
word_length = len(message)

# def find_words(blocks, word_length):
#     """
#     Find words that can be spelled using the letters on the cubes.

#     Args:
#         cubes (list): List of cubes, each cube is a string of 4 letters.
#         word_length (int): Length of words to find.

#     Returns:
#         list: List of words that can be spelled.
#     """
#     # Generate all possible combinations of letters
#     combinations = itertools.product(*blocks)

#     # Filter combinations that form valid English words
#     words = []
#     for combo in combinations:
#         word = ''.join(combo).lower()
#         if len(word) == word_length and word in english_words:
#             words.append(word)

#     return words

def find_combinations(cubes, message):
    message = message.upper()
    combinations = []

    def recursive_find(combinations, current_combination, remaining_word):
        if not remaining_word:
            combinations.append(current_combination[:])
            return
        for i, cube in enumerate(cubes):
            if remaining_word[0] in cube:
                current_combination.append((i + 1, remaining_word[0]))
                recursive_find(combinations, current_combination, remaining_word[1:])
                current_combination.pop()

    recursive_find(combinations, [], message)
    return combinations

message = "HAPPY"
combinations = find_combinations(cubes, message)

combo_count = 0
if st.button('Find Words'):
    for i, combination in enumerate(combinations):
        print(f"Combination {i + 1}:")
        for cube_number, letter in combination:
            print(f"Cube {cube_number}: {letter}")
        combo_count += 1
        if combo_count >= 10:
            

# if st.button('Find words'):


#     for word in set(words):  # Use set to remove duplicates
#         print(word)
