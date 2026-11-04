class ModelBasedAgent:
    def __init__(self):
        self.previous_distance = None

    def decide_action(self, distance):
        if distance < 10:
            action = "Brake"
        elif distance < 20:
            action = "Slow Down"
        elif distance < 30:
            action = "Maintain Speed"
        else:
            action = "Accelerate"

        if self.previous_distance is not None:
            if distance < self.previous_distance:
                print("Object is getting closer")
            elif distance > self.previous_distance:
                print("Object is moving farther")
            else:
                print("Object is stationary")

        print("Current Car State:", action)
        self.previous_distance = distance

agent = ModelBasedAgent()

while True:
    distance = float(input("Enter obstacle distance (-1 to exit): "))

    if distance == -1:
        break

    agent.decide_action(distance)