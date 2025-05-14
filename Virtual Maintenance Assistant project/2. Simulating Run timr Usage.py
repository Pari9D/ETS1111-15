# Step 1: Define the machine
machine = {
    "name": "Compressor-01",
    "runtime_hours": 0,
    "max_hours_before_maintenance": 100,
    "last_maintenance_at": 0
}

# Step 2: Define how many hours the machine runs per cycle
run_increment = 5

# Step 3: Simulate the machine running in a loop
for day in range(1, 6):  # Simulate 5 days
    print(f"\nDay {day} running...")
    machine["runtime_hours"] += run_increment  
    print("Updated Runtime (hrs):", machine["runtime_hours"])
