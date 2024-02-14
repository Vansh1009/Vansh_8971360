import unittest
from Event_Registration import Attendee


class TestAttendeeIntegration(unittest.TestCase):

    def setUp(self):
        self.attendee = Attendee()

    def test_add_view_attendees_integration(self):

        def test_add_remove_view_attendees_integration(self):
            # Add attendees
            self.attendee.add_attendee("Vansh")

            # Add another attendee
            self.attendee.add_attendee("Sid")

            # Capture print output for testing
            import sys
            from io import StringIO
            saved_stdout = sys.stdout
            try:
                out = StringIO()
                sys.stdout = out

                # View attendees
                self.attendee.view_attendees()

                output = out.getvalue().strip()

                # Check if the output is as expected
                expected_output = "Attendees:\nVansh\nSid"
                self.assertEqual(output, expected_output)
            finally:
                sys.stdout = saved_stdout

    def test_add_remove_view_attendees_integration(self):

                # Add attendees
                self.attendee.add_attendee("John")
                self.attendee.add_attendee("Alice")

                # Remove an attendee
                self.attendee.remove_attendee("John")

                # Add another attendee
                self.attendee.add_attendee("Bob")

                # Capture print output for testing
                import sys
                from io import StringIO
                saved_stdout = sys.stdout
                try:
                    out = StringIO()
                    sys.stdout = out

                    # View attendees
                    self.attendee.view_attendees()

                    output = out.getvalue().strip()

                    # Check if the output is as expected
                    expected_output = "Attendees:\nJohn\nBob"
                    self.assertEqual(output, expected_output)
                finally:
                    sys.stdout = saved_stdout

if __name__ == "__main__":
    unittest.main()
