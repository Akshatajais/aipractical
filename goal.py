class GoalBasedAgent:
    def __init__(self):
        self.goal_distance = 20

    def decide_action(self, distance):
        if distance < self.goal_distance:
            action = "Brake"
        elif distance == self.goal_distance:
            action = "Maintain Speed"
        else:
            action = "Continue"

        print("Action:", action)

agent = GoalBasedAgent()

while True:
    distance = float(input("Enter obstacle distance (-1 to exit): "))

    if distance == -1:
        break

    agent.decide_action(distance)