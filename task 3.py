
def bus_occupancy_simulation(capacity, initial_passengers, stops):
    passengers = initial_passengers

    print("\nBUS PASSENGER OCCUPANCY SIMULATION")
    print("-" * 75)
    print(f"Bus Capacity: {capacity}")
    print(f"Initial Passengers: {initial_passengers}")
    print("-" * 75)

    print(f"{'Stop':<10}{'Boarding':<12}{'Alighting':<12}"
          f"{'Passengers':<14}{'Status':<20}")
    print("-" * 75)

    for stop, boarding, alighting in stops:
        # Validate passenger counts
        if boarding < 0 or alighting < 0:
            print(f"Invalid data at {stop}: counts cannot be negative.")
            continue

        if alighting > passengers:
            print(f"Invalid data at {stop}: "
                  f"only {passengers} passengers are on the bus.")
            continue

        # Update passenger count
        passengers = passengers - alighting + boarding

        # Check capacity
        if passengers > capacity:
            status = "CAPACITY EXCEEDED!"
        else:
            status = "Normal"

        print(f"{stop:<10}{boarding:<12}{alighting:<12}"
              f"{passengers:<14}{status:<20}")

    print("-" * 75)
    print(f"Final passenger count: {passengers}")


# Example input
bus_capacity = 50
initial_passengers = 20

# Each entry: (Stop Name, Boarding Count, Alighting Count)
stops_data = [
    ("Stop 1", 10, 5),
    ("Stop 2", 15, 8),
    ("Stop 3", 20, 4),
    ("Stop 4", 5, 10),
    ("Stop 5", 8, 6)
]

# Run the simulation
bus_occupancy_simulation(
    bus_capacity,
    initial_passengers,
    stops_data
)
