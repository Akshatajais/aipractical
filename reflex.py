def simple_reflex_agent():
    distance = float(input("Enter obstacle distance in meters: "))

    if distance < 10:
        action = "Brake"
    elif distance <= 20:
        action = "Slow Down"
    else:
        action = "Continue"

    print("Action:", action)

simple_reflex_agent()