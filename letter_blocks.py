import streamlit as st

# Functions to use later
def remove_blocks_for_symbols(blocks,flower,four,flag,tree,heart,clover,pineapple):
    if flower:
        blocks[0] = ""
    if tree:
        blocks[1] = ""
    if flag:
        blocks[2] = ""
    if four:
        blocks[3] = ""
    if heart:
        blocks[4] = ""
    if clover:
        blocks[6] = ""
    if pineapple:
        blocks[9] = ""

    return blocks

def find_combinations(cubes, message):
    message = message.upper()
    combinations = []

    def recursive_find(available_cubes, current_combination, remaining_word):
        if len(combinations) < 100:
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

# Header and Titles
st.title("Letter Block Combination Finder")
st.sidebar.image('word-blocks.webp')
st.write(
    "This combination finder allows you to generate combinations of blocks to spell whatever you want! Simply pick the number of sets of blocks you have and type your desired phrase below."
)
# Define Sidebar
with st.sidebar.expander("Additional Notes"):
    st.write("This letter block combination finder defaults to the 'Wolf Creek All Seasons Blocks'; the combinations of which you can see below.")
    st.write("If you would like to define your own word blocks, use the space below.")
    col1, col2 = st.columns(2)
    custom_blocks_checkbox = st.checkbox('Check this box to use custom blocks.')
    custom_blocks = st.text_area("Define your letter blocks in order below. Separate each letter grouping with a comma.").split(',')
    st.caption("Symbols are unavailble with custom blocks.")
    st.divider()
    st.write("All Seasons Block combinations are below:")
    st.write("NDH,EIP,MPG,QAI,LOR,LAWS,ETJ,VOHR,ABCD,YGC,HELR,SDNW,SOAC,TNWY,TVUO,FIKM")

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

if custom_blocks_checkbox:
    cubes = custom_blocks
else:
    cubes = cubes

# How many block sets do you have?
block_sets = st.slider("How many sets of blocks do you have?", min_value = 1, max_value = 10, value = 1)
blocks = cubes * block_sets 

# Include Symbols?
with st.expander("Would you like to include any symbols? This will remove possible blocks."):
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
max_characters = len(total_blocks) - flower- four - flag - tree - heart - clover - pineapple

message = st.text_input("Type the message you're trying to spell",value="happy birthday",max_chars=max_characters).replace(" ","")
combinations = find_combinations(total_blocks, message)

#st.write(len(combinations))
if st.button('Find Words'):
    if len(combinations) >0:
        for i, combination in enumerate(combinations):
            letter_list = []
            cube_list = []
            st.write(f"Combination {i + 1}:")
            for cube_number, letter in combination:
                # st.write(f"{letter}: {cube_number}")
                letter_list.append(letter)
                if cube_number > 16:
                    cube_number = cube_number - 16
                else:
                        cube_number
                cube_list.append(cube_number)
            #st.metric(str(letter_list).replace("'","").replace(","," -"),str(cube_list).replace(","," -"),border=True)
            st.write(str(letter_list).replace("'","").replace(","," -"))
            st.write(str(cube_list).replace(","," -"))
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