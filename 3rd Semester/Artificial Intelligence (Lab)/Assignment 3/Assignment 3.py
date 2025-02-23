class SimpleReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature 
        self.previous_action=None

    def percept(self, current_temperature):
        return current_temperature

    def act(self, current_temperature):
        if current_temperature<self.desired_temperature:
            action = "Turn on heater"
        elif current_temperature>self.desired_temperature:
            action = "Turn off heater"
        else:
            action = self.previous_action

        if action != self.previous_action:
            self.previous_action=action
        return action

rooms = {
    "Bedroom1": 22,
    "Kitchen": 18,
    "Living Room": 20,
    "Bedroom2": 24, 
    "Bathroom": 23
}

desired_temperature = 20
agent = SimpleReflexAgent(desired_temperature)

for room, temperature in rooms.items():
    action = agent.act(temperature)
    print(f"{room}: Current temperature = {temperature}°C. {action}.")