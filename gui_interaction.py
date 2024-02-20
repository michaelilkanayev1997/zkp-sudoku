from zkp_sudoku import *
import tkinter as tk
import tkinter.font as tkFont

IS_VERIFIED = True

window = tk.Tk()
window.title("ZKP-Sudoku Verification")
window.iconbitmap('pastime.ico')
window.configure(background='light grey')
window.minsize(900, 730)  # Set a minimum window size
fontStyle = tkFont.Font(family="Helvetica", size=12, weight="bold")

# Create a frame for the Sudoku grid
grid_frame = tk.Frame(window)
grid_frame.pack(pady=20)
grid_frame.configure(background='light grey')
# Create a frame for the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=20)
button_frame.configure(background='light grey')
# Create a frame for the results
results_frame = tk.Frame(window)
results_frame.pack(pady=20)
results_frame.configure(background='light grey')

# Show the Sudoku Puzzle
def show_sudoku():
    display_grid(puzzle)
    verify_btn.pack_forget()

# Show the Sudoku Solution
def show_solution():
    display_grid(puzzle,True)
    verify_btn.pack(side=tk.RIGHT, padx=20)  # Show Verify button

# Show the Sudoku grid
def display_grid(grid,showSolution = False):
    # Clear the existing grid before displaying a new one
    for widget in grid_frame.winfo_children():
        widget.destroy()

    for i in range(9):
        for j in range(9):
            cell_value = grid[i*9+j]

            if (showSolution):
                text = 'X' if cell_value == 0 else str(cell_value)
            else:
                text = '' if cell_value == 0 else str(cell_value)

            label = tk.Label(grid_frame, text=text, font=fontStyle, width=2, borderwidth=2, relief="groove")
            label.grid(row=i, column=j)

# Verify all the row packets
def verify_row_packets():
    global IS_VERIFIED
    puzzle = chunk_list(transformed_puzzle, 9)

    # Initialize an empty list to hold the packets for each row
    row_packets = []
    #print(puzzle)

    # Iterate over each row in the puzzle
    for row in puzzle:
        # Initialize an empty packet for the current row
        row_packet = []

        # Iterate over each cell in the row
        for cell in row:
            # Randomly select one of the three numbers (cards) in the cell
            selected_card = random.choice(cell)
            # Add the selected card to the row packet
            row_packet.append(selected_card)

        # Shuffle the cards in the current row packet
        shuffled_packet = shuffle_packet(row_packet)
        # Add the shuffled packet to the list of row packets
        row_packets.append(shuffled_packet)

    # Output for demonstration
    for index, packet in enumerate(row_packets):
        bool = all_digits_exist_once(packet)
        verified =check_bool(bool)

        # Create a label for the verification result
        if(bool):
            text4 = tk.Label(results_frame, text=f"Row {index + 1}: {packet}-{verified}", font=fontStyle, bg='green', fg='white')
        else:
            IS_VERIFIED=False
            text4 = tk.Label(results_frame, text=f"Row {index + 1}: {packet}-{verified}   ", font=fontStyle, bg='red', fg='white')

        text4.grid(row=index, column=0, padx=10, pady=5)

    verify_col_packets()

# Verify all the col packets
def verify_col_packets():
    global IS_VERIFIED
    puzzle = chunk_list(transformed_puzzle, 9)
    puzzle_transposed = transpose(puzzle)  # Work with columns

    # Initialize an empty list to hold the packets for each col
    column_packets = []

    for col in puzzle_transposed:
        # Initialize an empty packet for the current col
        column_packet = []
        # Iterate over each cell in the row
        for cell in col:
            selected_card = random.choice(cell)
            column_packet.append(selected_card)

        shuffled_packet = shuffle_packet(column_packet)
        column_packets.append(shuffled_packet)

    # Output for demonstration
    for index, packet in enumerate(column_packets):
        bool = all_digits_exist_once(packet)
        verified = check_bool(bool)

        # Create a label for the verification result
        if(bool):
            text5 = tk.Label(results_frame, text=f"Col {index + 1}: {packet}-{verified}", font=fontStyle, bg='green', fg='white')
        else:
            IS_VERIFIED = False
            text5 = tk.Label(results_frame, text=f"Col {index + 1}: {packet}-{verified}   ", font=fontStyle, bg='red', fg='white')

        text5.grid(row=index, column=10, sticky='e', padx=10, pady=5)

    verify_subgrid_packets()

# Verify all the subgrid packets
def verify_subgrid_packets():
    global IS_VERIFIED
    puzzle = chunk_list(transformed_puzzle, 9)

    def get_subgrid(puzzle, start_row, start_col, size=3):
        # Initialize an empty list to hold the packet for current subgrid
        subgrid = []
        for row in range(start_row, start_row + size):
            for col in range(start_col, start_col + size):
                subgrid.append(puzzle[row][col])
        return subgrid

    # Initialize an empty list to hold the packets for each subgrid
    subgrid_packets = []

    # Extract and shuffle packets for each of the 9 subgrids
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = get_subgrid(puzzle, row, col)
            subgrid_packet = []
            for cell in subgrid:
                selected_card = random.choice(cell)
                subgrid_packet.append(selected_card)
            shuffled_packet = shuffle_packet(subgrid_packet)
            subgrid_packets.append(shuffled_packet)

    # Display verification results for each subgrid
    for index, packet in enumerate(subgrid_packets):
        bool = all_digits_exist_once(packet)
        verified = check_bool(bool)

        # Create a label for the verification result
        if (bool):
            text6 = tk.Label(results_frame, text=f"Subgrid {index + 1}: {packet}-{verified}", font=fontStyle, bg='green', fg='white')
        else:
            IS_VERIFIED = False
            text6 = tk.Label(results_frame, text=f"Subgrid {index + 1}: {packet}-{verified}   ", font=fontStyle, bg='red', fg='white')

        text6.grid(row=index, column=20, sticky='e', padx=10, pady=5)

    color = "green" if IS_VERIFIED else "red"

    # Show the Final Result Label
    text7 = tk.Label(results_frame, text=f"Verified: {IS_VERIFIED}", font=fontStyle, bg=color, fg='white')
    text7.grid(row=index + 1, column=10, pady=10)


# Adding buttons to the button_frame
show_puzzle_btn = tk.Button(button_frame, text="Show Puzzle", command=show_sudoku,font=fontStyle)
show_puzzle_btn.pack(side=tk.LEFT, padx=20)

show_solution_btn = tk.Button(button_frame, text="Show Solution", command=show_solution,font=fontStyle)
show_solution_btn.pack(side=tk.LEFT, padx=20)
# Initially hidden Verify button
verify_btn = tk.Button(button_frame, text="Verify", command=verify_row_packets, font=fontStyle, bg="orange", fg="white")

window.mainloop()


