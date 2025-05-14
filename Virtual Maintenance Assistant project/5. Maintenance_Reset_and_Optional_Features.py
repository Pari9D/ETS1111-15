def perform_maintenance(machine):
    machine["last_maintenance_at"] = machine["runtime_hours"]
    print("✅ Maintenance performed. Counter reset.")
def save_machine_status(machine):
    with open("status.txt", "w") as file:
        for key, value in machine.items():
            file.write(f"{key}: {value}\n")
    print("📄 Machine status saved to status.txt.")
print("5. Save machine status to file")
print("6. Exit")

 # Then in the menu:
 # elif choice == "5":
     # save_machine_status(machine)
     # elif choice == "6":
       # print("Exiting program. Goodbye!")
       # break
     # else:
         # print("Invalid choice. Try again.")