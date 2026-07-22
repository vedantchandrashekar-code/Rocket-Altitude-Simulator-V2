import time

# Rocket parameters
thrust_acceleration = float(input("Type in your thrust acceleation: "))
planet = input("What planet is the rocket in: ")
Earth_gravity = 9.81
Mercury_gravity = 3.70
Venus_gravity = 8.87
Mars_gravity = 3.71
Jupiter_gravity = 24.79
Saturn_gravity = 10.44
Uranus_gravity = 8.69
Neptune_Gravity = 11.15
if planet == "mercury":
    gravity = Mercury_gravity
elif planet == "venus":
 gravity = Venus_gravity
elif planet == "earth":
 gravity = Earth_gravity  
elif planet == "mars":
 gravity = Mars_gravity
elif planet == "jupiter":
 gravity = Jupiter_gravity
elif planet == "saturn":
 gravity =  Saturn_gravity
elif planet == "uranus":
 gravity = Uranus_gravity
elif planet == "neptune":
 gravity = Neptune_Gravity  
 
 
time_elapsed = 0     # seconds
time_step = 1          # seconds
net_acceleation = thrust_acceleration - gravity
print("🚀 ROCKET ALTITUDE SIMULATOR 🚀")
print("--------------------------------")

simulation_input = int(input("How much time do you want the sim to run for: "))
while time_elapsed <= simulation_input:

    # Calculate altitude
    altitude = 0.5 * net_acceleation * time_elapsed ** 2

    # Calculate velocity
    velocity = net_acceleation * time_elapsed

    print(f"Time: {time_elapsed:2} s | "
          f"Altitude: {altitude:6.1f} m | "
          f"Velocity: {velocity:6.1f} m/s")

    time_elapsed += time_step

    time.sleep(0.2)