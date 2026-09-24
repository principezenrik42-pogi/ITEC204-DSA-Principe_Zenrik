"""
IT Automation Incident Ticket Manager
ITEC 204 - Data Structures and Algorithms
Laboratory Activity 1

Linear Data Structure Used: List of Dictionaries
"""

incident_tickets = []  # main linear data structure (list)


def add_ticket(incident_id, bot, description):
    """Add a new incident ticket to the list."""
    ticket = {"id": incident_id, "bot": bot, "description": description}
    incident_tickets.append(ticket)
    print(f"\nTicket {incident_id} added successfully.")


def display_tickets():
    """Display all active incident tickets."""
    if not incident_tickets:
        print("\nNo active incident tickets.")
        return
    print("\n" + "-" * 75)
    print(f"{'Incident ID':<15}{'Bot':<20}{'Short Description'}")
    print("-" * 75)
    for ticket in incident_tickets:
        print(f"{ticket['id']:<15}{ticket['bot']:<20}{ticket['description']}")
    print("-" * 75)


def search_ticket(incident_id):
    """Search for a specific incident ticket using its Incident ID."""
    for ticket in incident_tickets:
        if ticket["id"] == incident_id:
            print("\nTicket Found:")
            print(f"Incident ID : {ticket['id']}")
            print(f"Bot         : {ticket['bot']}")
            print(f"Description : {ticket['description']}")
            return ticket
    print(f"\nTicket {incident_id} not found.")
    return None


def remove_ticket(incident_id):
    """Remove a resolved incident ticket from the list."""
    for ticket in incident_tickets:
        if ticket["id"] == incident_id:
            incident_tickets.remove(ticket)
            print(f"\nTicket {incident_id} has been marked resolved and removed.")
            return
    print(f"\nTicket {incident_id} not found.")


def count_active_tickets():
    """Display the total number of active incident tickets."""
    print(f"\nTotal active incident tickets: {len(incident_tickets)}")


def load_sample_data():
    """Pre-load the 10 sample incident tickets for testing."""
    sample_data = [
        ("INC1392939", "BOT-Inventory", "Failed to generate the daily report"),
        ("INC1392940", "BOT-Email", "Failed to send the scheduled notification"),
        ("INC1392941", "BOT-DataSync", "Encountered an error during data transfer"),
        ("INC1392942", "BOT-Invoice", "Failed to process an invoice"),
        ("INC1392943", "BOT-Report", "Failed to generate the weekly report"),
        ("INC1392944", "BOT-FileTransfer", "Failed to upload the required file"),
        ("INC1392945", "BOT-DataEntry", "Encountered an error while entering records"),
        ("INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"),
        ("INC1392947", "BOT-Validation", "Failed to validate the submitted records"),
        ("INC1392948", "BOT-Notification", "Failed to send the system alert"),
    ]
    for incident_id, bot, description in sample_data:
        add_ticket(incident_id, bot, description)


def main():
    print("=" * 75)
    print("     IT AUTOMATION INCIDENT TICKET MANAGER")
    print("=" * 75)
    load_sample_data()
    print("\n10 sample incident tickets have been loaded for testing.")

    while True:
        print("\n--------- MENU ---------")
        print("1. Add Incident Ticket")
        print("2. Display All Active Incident Tickets")
        print("3. Search Incident Ticket")
        print("4. Remove Resolved Incident Ticket")
        print("5. Count Active Incident Tickets")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            incident_id = input("Enter Incident ID: ").strip()
            bot = input("Enter Bot Name: ").strip()
            description = input("Enter Short Description: ").strip()
            add_ticket(incident_id, bot, description)

        elif choice == "2":
            display_tickets()

        elif choice == "3":
            incident_id = input("Enter Incident ID to search: ").strip()
            search_ticket(incident_id)

        elif choice == "4":
            incident_id = input("Enter Incident ID to remove: ").strip()
            remove_ticket(incident_id)

        elif choice == "5":
            count_active_tickets()

        elif choice == "6":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
