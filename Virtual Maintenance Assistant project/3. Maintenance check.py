machine = {
    "runtime_hours": 25,
    "max_hours_before_maintenance": 100,
    "last_maintenance_at": 0
}
machine["runtime_hours"] - machine["last_maintenance_at"] >= machine["max_hours_before_maintenance"]
# Maintenance check function
def check_maintenance(machine):
    hours_since_maintenance = machine["runtime_hours"] - machine["last_maintenance_at"]
    
    if hours_since_maintenance >= machine["max_hours_before_maintenance"]:
        print("\n⚠️ Maintenance ALERT!")
        print("Machine:", machine["name"])
        print("It's been", hours_since_maintenance, "hours since last maintenance.")
        print("Please service the machine!\n")
    else:
        print(f"No maintenance needed yet. Hours since last service: {hours_since_maintenance}")
run_increment = 30  # simulate 30 hours at once
machine["runtime_hours"] += run_increment

check_maintenance(machine)
