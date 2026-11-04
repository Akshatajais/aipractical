class UtilityBasedAgent:
    def decide_action(self, distance):
        actions = {
            "Brake": (10, 2),
            "Slow Down": (8, 5),
            "Maintain Speed": (6, 8),
            "Accelerate": (3, 10)
        }
        if distance < 10:
            actions = {
                "Brake": (10, 2),
                "Slow Down": (8, 5),
                "Maintain Speed": (3, 8),
                "Accelerate": (1, 10)
            }
        elif distance < 20:
            actions = {
                "Brake": (9, 2),
                "Slow Down": (10, 6),
                "Maintain Speed": (6, 8),
                "Accelerate": (2, 10)
            }
        elif distance < 30:
            actions = {
                "Brake": (7, 2),
                "Slow Down": (8, 5),
                "Maintain Speed": (10, 8),
                "Accelerate": (7, 10)
            }

        utilities = {}
        for action, scores in actions.items():
            safety, speed = scores
            utility = 0.7 * safety + 0.3 * speed
            utilities[action] = utility
            print(action, "Utility:", round(utility, 2))

        best_action = max(utilities, key=utilities.get)
        print("Selected Action:", best_action)
agent = UtilityBasedAgent()

while True:
    distance = float(input("Enter obstacle distance (-1 to exit): "))

    if distance == -1:
        break

    agent.decide_action(distance)