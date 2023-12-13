class BlockWorld:
    def __init__(self, initial_state):
        self.state = initial_state

    def display_state(self):
        print("Current State:")
        for block, on_top_of in self.state.items():
            print(f"{block} is on top of {on_top_of}")

    def move(self, block, destination):
        if block in self.state and destination in self.state:
            self.state[block] = destination
            self.display_state()
        else:
            print(f"Error: {block} or {destination} not found in the block world.")

# Example usage
if __name__ == "__main__":
    initial_state = {
        'A': 'B',
        'B': 'Table',
        'C': 'Table'
    }

    world = BlockWorld(initial_state)
    world.display_state()

    # Move block 'A' on top of block 'C'
    world.move('A', 'C')

    # Move block 'B' on top of the table
    world.move('B', 'Table')
