from user_input import choose_map
from bind_map import run_bind_map
from ascent_map import run_ascent_map
from split_map import run_split_map
from lotus_map import run_lotus_map

def main():
    while True:
        selected_map = choose_map()

        if selected_map == "Ascent":
            run_ascent_map()
        elif selected_map == "Bind":
            run_bind_map()
        elif selected_map == "Split":
            run_split_map()
        elif selected_map == "Lotus":
            run_lotus_map()
        elif selected_map == "gg":
            break
        else:
            print("Functionality for the selected map is not yet implemented.")


if __name__ == "__main__":
    main()
