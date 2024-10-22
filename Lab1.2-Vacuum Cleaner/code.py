class VacuumCleanerAgent:
    def __init__(self):
        self.places = {'A': True, 'B': True}  
        self.current_location = 'A'  

    def clean(self):
        print(f"Cleaning {self.current_location}.")
        self.places[self.current_location] = False 

    def move(self):
        if self.current_location == 'A':
            self.current_location = 'B'
        else:
            self.current_location = 'A'
        print(f"Moving to {self.current_location}.")

    def is_environment_clean(self):
        return not self.places['A'] and not self.places['B']

    def run(self):
        while not self.is_environment_clean():
            if self.places[self.current_location]:  
                self.clean()
            else:
                self.move()

        print("Both places are clean!")

agent = VacuumCleanerAgent()
agent.run()
