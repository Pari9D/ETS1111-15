# Create a dictionary representing one machine
machine = {
    "name": "Compressor-01",              # Name of the machine
    "runtime_hours": 0,                   # How many hours it has run so far
    "max_hours_before_maintenance": 100,  # Maintenance needed every 100 hours
    "last_maintenance_at": 0              # When maintenance was last performed
}

# Display current status
print("Machine:", machine["name"])
print("Runtime (hrs):", machine["runtime_hours"])
print("Maintenance interval (hrs):", machine["max_hours_before_maintenance"])
print("Last serviced at:", machine["last_maintenance_at"])
