class Attendee:

    def __init__(self):
        self.attendees = []


def add_attendee(self, name):
    """Add a new attendee."""
    self.attendees.append(name)


def remove_attendee(self, name):
    """Remove an attendee."""
    if name in self.attendees:
        self.attendees.remove(name)
    else:
        print(f"{name} is not in the attendee list.")


def view_attendees(self):
    """View all attendees."""
    if self.attendees:
        print("Attendees:")
        for attendee in self.attendees:
            print(attendee)
    else:
        print("No attendees to display.")