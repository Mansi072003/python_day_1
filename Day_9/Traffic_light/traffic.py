import time

def show_light(color):
    print("Current Light:", color)
    if color == "Red":
        print("Stop")
    elif color == "Green":
        print("Go")
    elif color == "Yellow":
        print("Wait")

def traffic_light_simulation(cycles):
    colors = ["Red", "Green", "Yellow"]
    
    for i in range(cycles):
        print(f"Cycle {i + 1}")
        for color in colors:
            show_light(color)
            time.sleep(4)

if __name__ == "__main__":
    print("Traffic Light Simulation Started")
    traffic_light_simulation(cycles=1)
    print("Simulation Ended")
