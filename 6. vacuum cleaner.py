class VacuumCleaner:
    def __init__(self, environment_size):
        self.environment = [[0] * environment_size for _ in range(environment_size)]
        self.position = (0, 0)  # Starting position of the vacuum cleaner
        self.battery = 100  # Initial battery level
        self.cleaned_cells = 0

    def set_dirty_cells(self, dirty_cells):
        for cell in dirty_cells:
            x, y = cell
            self.environment[x][y] = 1

    def clean_cell(self, x, y):
        if self.environment[x][y] == 1:  # If the cell is dirty
            self.environment[x][y] = 0  # Clean the cell
            self.cleaned_cells += 1
            print(f"Cleaning cell ({x}, {y})")
            self.battery -= 1  # Consume battery
            return True
        return False

    def move(self, direction):
        x, y = self.position
        if direction == 'up' and x > 0:
            x -= 1
        elif direction == 'down' and x < len(self.environment) - 1:
            x += 1
        elif direction == 'left' and y > 0:
            y -= 1
        elif direction == 'right' and y < len(self.environment) - 1:
            y += 1
        self.position = (x, y)
        self.battery -= 1  # Consume battery for movement

    def recharge(self):
        self.battery = 100

    def clean_environment(self):
        while self.battery > 0:
            x, y = self.position
            if self.clean_cell(x, y):  # Clean the current cell
                continue  # Skip movement if the cell was cleaned
            # Move to the next cell
            if x % 2 == 0:  # Move right if the row number is even
                self.move('right')
            else:  # Move left if the row number is odd
                self.move('left')
            # Move down if reached the end of the row
            if self.position[1] == len(self.environment) - 1:
                self.move('down')
        print("Battery depleted. Recharging...")
        self.recharge()
        print("Environment cleaned successfully.")
        print(f"Total cells cleaned: {self.cleaned_cells}")

# Example usage
if __name__ == "__main__":
    environment_size = 5
    dirty_cells = [(1, 1), (2, 2), (3, 3), (4, 4)]  # Example dirty cells
    vacuum_cleaner = VacuumCleaner(environment_size)
    vacuum_cleaner.set_dirty_cells(dirty_cells)
    vacuum_cleaner.clean_environment()
