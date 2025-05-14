import matplotlib.pyplot as plt  # 🔼 UPGRADED: Added for plotting

# ------------------------
# VIRTUAL MAINTENANCE ASSISTANT (With Plotting)
# ------------------------

# ✅ STEP 1: Machine definition using a dictionary
machine = {
    "name": "Compressor-01",
    "runtime_hours": 0,
    "max_hours_before_maintenance": 100,
    "last_maintenance_at": 0
}

# 🔼 UPGRADED: Track runtime history for plotting
runtime_log = []  # Will store runtime after each simulation session

# ✅ STEP 2: Simulate machine runtime
def simulate_runtime(machine, hours, log):  # 🔼 UPGRADED: added log as parameter
    """Adds runtime hours to the machine"""
    machine["runtime_hours"] += hours
    log.append(machine["runtime_hours"])  # 🔼 UPGRADED: track new runtime in log
    print(f"⏱️ Simulated {hours} hours. Total runtime: {machine['runtime_hours']} hours")

# ✅ STEP 3: Check if maintenance is needed
def check_maintenance(machine):
    """Checks if the machine needs maintenance"""
    hours_since_maintenance = machine["runtime_hours"] - machine["last_maintenance_at"]
    
    if hours_since_maintenance >= machine["max_hours_before_maintenance"]:
        print("\n⚠️ Maintenance ALERT!")
        print("Machine:", machine["name"])
        print("It's been", hours_since_maintenance, "hours since last maintenance.")
    else:
        print(f"No maintenance needed yet. Hours since last service: {hours_since_maintenance}")

# ✅ STEP 4: Perform maintenance
def perform_maintenance(machine):
    """Resets the maintenance counter"""
    machine["last_maintenance_at"] = machine["runtime_hours"]
    print("✅ Maintenance done. Counter reset.")

# ✅ STEP 5: Save to file
def save_machine_status(machine):
    """Saves machine data to a text file"""
    with open("status.txt", "w") as file:
        for key, value in machine.items():
            file.write(f"{key}: {value}\n")
    print("📁 Machine status saved to 'status.txt'.")

# 🔼 UPGRADED: NEW FUNCTION — Plot runtime graph
def plot_runtime(log):
    """Plots runtime progress using matplotlib"""
    if not log:
        print("❌ No data to plot yet.")
        return
    
    sessions = list(range(1, len(log) + 1))
    
    plt.plot(sessions, log, marker='o', linestyle='-', color='blue', label='Runtime')
    plt.axhline(y=100, color='red', linestyle='--', label='Maintenance Limit (100 hrs)')
    
    plt.title("Machine Runtime Over Simulations")
    plt.xlabel("Simulation Session")
    plt.ylabel("Total Runtime (Hours)")
    plt.legend()
    plt.grid(True)
    plt.show()

# ✅ STEP 6: Main menu loop
# ✅ STEP 6: Main menu loop
while True:
    print("\n--- Virtual Maintenance Assistant ---")
    print("1. Simulate machine running")
    print("2. Check maintenance status")
    print("3. Perform maintenance")
    print("4. View machine status")
    print("5. Save machine status to file")
    print("6. Plot runtime graph")  # 🔼 UPGRADED: New menu option
    print("7. Exit")

    choice = input("Select an option (1-7): ")

    if choice == "1":
        try:
            hours = int(input("Enter number of hours to simulate: "))
            simulate_runtime(machine, hours, runtime_log)  # 🔼 UPGRADED: pass log
        except ValueError:
            print("❌ Please enter a valid number.")
    elif choice == "2":
        check_maintenance(machine)
    elif choice == "3":
        perform_maintenance(machine)
    elif choice == "4":
        print("\n📊 Machine Status:")
        print("Name:", machine["name"])
        print("Total Runtime:", machine["runtime_hours"])
        print("Last Maintenance At:", machine["last_maintenance_at"])
        print("Max Hours Before Maintenance:", machine["max_hours_before_maintenance"])
    elif choice == "5":
        save_machine_status(machine)
    elif choice == "6":
        plot_runtime(runtime_log)  # ✅ Just show the plot — don't break the loop!
    elif choice == "7":
        print("👋 Exiting program. Goodbye!")
        break  # ✅ Exit only when the user chooses option 7
    else:
        print("❌ Invalid choice. Try again.")