class ModelBasedReflexAgent:
    def __init__(self,temp):
        self.desired_temp=temp
        self.previous_action=None
    def act(self,temp):
        if temp>self.desired_temp and self.previous_action!="On":
            action_taken="On"
            result=(f"Temperature: {temp}, Action: Turn the Heater off....")
        elif temp<self.desired_temp and self.previous_action!="Off":
            action_taken="Off"
            result=(f"Temperature: {temp}, Action: Turn the Heater on....")
        else:
            action_taken=self.previous_action
            result=(f"Temperature: {temp}, Action: No action required....")
        self.previous_action=action_taken
        return result
obj3=ModelBasedReflexAgent(int(input("Enter the desired temperature: ")))
rooms={
    "Living room": 22,
    "Dining room": 20,
    "Bedroom": 16,
    "Library": 12,
}
for room,temperature in rooms.items():
    print(f"{room}: {obj3.act(temperature)}.")