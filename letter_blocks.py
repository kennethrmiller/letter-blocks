from tkinter import HORIZONTAL
import streamlit as st
from pathlib import Path

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="LetterBlocks",
    page_icon=".",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Design system CSS — loaded from styles.css
# ---------------------------------------------------------------------------
#CSS_PATH = Path(__file__).parent / "themes/styles.css"
#st.html(f"<style>{CSS_PATH.read_text()}</style>")

# Oak theme overrides — layered on top of styles.css when the toggle is on.
oak_theme = st.toggle("Oak theme (preview)", value=False)
OAK_CSS_PATH = Path(__file__).parent / "themes/oak-theme.css"
if oak_theme and OAK_CSS_PATH.exists():
    st.html(f"<style>{OAK_CSS_PATH.read_text()}</style>")

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
col1, col2 = st.columns(2)

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

# Render helpers --------------------------------------------------
def render_sequence(combination, oak=False, primary=False):
    """Build HTML for one combination as a row of letter blocks.

    Styles are inlined directly on each element so the output works regardless
    of whether Streamlit's HTML pipeline strips classes or sandboxes content.
    Preserves the original display rule for cube numbers (wrap >16 → -16),
    keeping the find_combinations output untouched.
    """
    face_size = 56 if primary else 44
    font_size = 30 if primary else 24

    if oak:
        face_style = (
            f"display:inline-flex;align-items:center;justify-content:center;"
            f"width:{face_size}px;height:{face_size}px;"
            f"background:#C99A66;color:#3A2E26;border-radius:9px;"
            f"font-size:{font_size}px;line-height:1;"
            f"box-shadow:0 3px 0 rgba(58,30,10,0.22),0 5px 8px rgba(58,46,38,0.14);"
        )
        cube_style = (
            "letter-spacing:0.02em;color:#6F5C49;"
        )
    else:
        face_style = (
            f"display:inline-flex;align-items:center;justify-content:center;"
            f"width:{face_size}px;height:{face_size}px;"
            f"background:#FFFFFF;color:#1A1A1A;"
            f"border:1.5px solid #1A1A1A;border-radius:0;"
            f"font-size:{font_size}px;line-height:1;"
        )
        cube_style = (
            "letter-spacing:0.06em;color:#5E5E5E;"
        )

    block_style = (
        "display:inline-flex;flex-direction:column;align-items:center;gap:6px;"
    )
    row_style = (
        "display:flex;flex-wrap:wrap;justify-content:center;align-items:flex-end;"
        f"gap:10px;row-gap:18px;padding:8px 0;margin:{16 if primary else 8}px 0;"
    )

    blocks_html = []
    for cube_number, letter in combination:
        display_num = cube_number - 16 if cube_number > 16 else cube_number
        blocks_html.append(
            f'<div style="{block_style}">'
            f'<span style="{face_style}">{display_num}</span>'
            f'<span style="{cube_style}">{letter}</span>'
            f'</div>'
        )
    return f'<div style="{row_style}">{"".join(blocks_html)}</div>'

# Persist click across reruns so toggling the theme doesn't hide results.
if 'show_combos' not in st.session_state:
    st.session_state.show_combos = False

if st.button('Find Words'):
    st.session_state.show_combos = True

if st.session_state.show_combos:
    if len(combinations) > 0:
        # First combination — featured at full size
        st.markdown(
            render_sequence(combinations[0], oak=oak_theme, primary=True),
            unsafe_allow_html=True,
        )

        # Remaining combinations — tucked into Streamlit's native expander
        if len(combinations) > 1:
            others = len(combinations) - 1
            with st.expander(f"Other combinations ({others})"):
                for combo in combinations[1:]:
                    st.markdown(
                        render_sequence(combo, oak=oak_theme, primary=False),
                        unsafe_allow_html=True,
                    )
    else:
        st.write("No combinations found, please try again.")