# Machine dictionary
machine = {
    "name": "Compressor-01",
    "runtime_hours": 0,
    "max_hours_before_maintenance": 100,
    "last_maintenance_at": 0
}

# Function to simulate runtime
def simulate_runtime(machine, hours):
    machine["runtime_hours"] += hours
    print(f"{hours} hours added. Total runtime: {machine['runtime_hours']}")

# Function to check maintenance
def check_maintenance(machine):
    hours_since_maintenance = machine["runtime_hours"] - machine["last_maintenance_at"]
    if hours_since_maintenance >= machine["max_hours_before_maintenance"]:
        print("\n⚠️ Maintenance ALERT!")
        print("It's been", hours_since_maintenance, "hours since last maintenance.")
    else:
        print(f"No maintenance needed. {hours_since_maintenance} hours since last maintenance.")

# Function to perform maintenance
def perform_maintenance(machine):
    machine["last_maintenance_at"] = machine["runtime_hours"]
    print("✅ Maintenance performed. Counter reset.")

# Menu loop
while True:
    print("\n--- Virtual Maintenance Assistant ---")
    print("1. Simulate machine running")
    print("2. Check maintenance status")
    print("3. Perform maintenance")
    print("4. View machine status")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    if choice == "1":
        try:
            hours = int(input("Enter number of hours to simulate: "))
            simulate_runtime(machine, hours)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "2":
        check_maintenance(machine)
    elif choice == "3":
        perform_maintenance(machine)
    elif choice == "4":
        print("\nMachine Name:", machine["name"])
        print("Total Runtime:", machine["runtime_hours"])
        print("Last Maintenance At:", machine["last_maintenance_at"])
        print("Max Hours Before Maintenance:", machine["max_hours_before_maintenance"])
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
