import streamlit as st
import pandas as pd

# Functions to use later
def remove_blocks_for_symbols(blocks,flower,four,flag,tree,heart,clover,pineapple):
    if flower:
        del blocks[0]
    if tree:
        del blocks[1]
    if flag:
        del blocks[2]
    if four:
        del blocks[3]
    if heart:
        del blocks[4]
    if clover:
        del blocks[6]
    if pineapple:
        del blocks[9]

    return blocks

def find_combinations(cubes, message):
    message = message.upper()
    combinations = []

    def recursive_find(available_cubes, current_combination, remaining_word):
        if not remaining_word:
            combinations.append(current_combination[:])
            return
        for i, (cube_number, cube) in enumerate(available_cubes):
            if remaining_word[0] in cube:
                new_available_cubes = available_cubes[:i] + available_cubes[i+1:]
                current_combination.append((cube_number, remaining_word[0]))
                recursive_find(new_available_cubes, current_combination, remaining_word[1:])
                current_combination.pop()

    numbered_cubes = list(enumerate(cubes, start=1))
    recursive_find(numbered_cubes, [], message)
    return combinations

st.title("All Seasons Blocks Word Finder")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# Define the cubes
cubes = [
    'NDH',  # Cube 1, also has flower
    'EIP',  # Cube 2, also has christmas tree
    'MPG',  # Cube 3, also has flag
    'QAI',  # Cube 4, also has 4
    'LOR',  # Cube 5, also has heart
    'LAWS',  # Cube 6
    'ETJ',  # Cube 7, also has clover
    'VOHR',  # Cube 8
    'ABCD',  # Cube 9
    'YGC',  # Cube 10, also has pineapple
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

# Include Symbols?
st.write("Would you like to include any symbols? This will remove possible blocks.")
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
flower = col1.checkbox("🌺",value = False)
tree = col2.checkbox("🌲",value = False)
flag = col3.checkbox("🇺🇸",value = False)
four = col4.checkbox("4️⃣",value = False)
heart = col5.checkbox("❤️",value = False)
clover = col6.checkbox("🍀",value = False)
pineapple = col7.checkbox("🍍",value = False)

total_blocks = remove_blocks_for_symbols(blocks,flower,four,flag,tree,heart,clover,pineapple)

# Input the desired message
message = st.text_input("Type the message you're trying to spell",value="happy",max_chars=len(total_blocks)).replace(" ","")
combinations = find_combinations(total_blocks, message)

if st.button('Find Words'):
    if len(combinations) >0:
        for i, combination in enumerate(combinations):
            letter_list = []
            cube_list = []
            st.write(f"Combination {i + 1}:")
            for cube_number, letter in combination:
                # st.write(f"{letter}: {cube_number}")
                letter_list.append(letter)
                cube_list.append(cube_number)
            st.metric(str(letter_list).replace("'","").replace(",","-"),str(cube_list).replace(",","-"),border=True)
            #st.metric("",str(cube_list).replace(",","-"),label_visibility="hidden")
            # data_df = pd.DataFrame([letter_list,cube_list])
            # st.dataframe(data_df, hide_index=True)
            st.divider()
            if i > 3:
                if st.button('Continue Combinations?'):
                    continue
                else:
                    break
    else:
        st.write("No combinations found, please try again.")