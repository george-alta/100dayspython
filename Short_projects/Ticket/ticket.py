class Ticket:
    ticket_counter = 2000  # Class variable to auto-generate ticket numbers

    def __init__(self, ticket_creator: str, caller_name: str, caller_email: str, description: str):
        """
        Initializes a new Ticket instance.

        Args:
        - ticket_creator (str): The name of the person creating the ticket.
        - caller_name (str): The name of the person reporting the issue.
        - caller_email (str): The email address of the person reporting the issue.
        - description (str): A brief description of the issue or request.
        """
        self.ticket_creator = ticket_creator
        self.caller_name = caller_name
        self.caller_email = caller_email
        self.ticket_number = self.ticket_counter
        self.description = description
        self.status = "Open"
        self.feedback = "No Feedback yet"
        self.comments = []

        Ticket.ticket_counter += 1

    def reset_password(self, admin_name):
        self.status = "Resolved"
        string = f'Password reset by {admin_name}. New password: {self.caller_name[:2]}{admin_name[:3]}'
        print(string)
        self.comments.append(string)

    def solve_ticket(self, resolution_notes, admin_name):
        self.status = "Resolved"
        self.comments.append(
            f"Ticked solved by {admin_name}. Resolution notes: {resolution_notes}\n")

    def submit_feedback(self, rating, comment):
        self.feedback = (f"Rating {rating}/5 - {comment}")

    def submit_comment(self, user_name, comment):
        self.comments.append(f"\nComment by {user_name}: {comment}\n")

    def reopen_ticket(self, user_name, comment):
        if self.status == "Resolved":
            self.status = "Open"
            self.feedback = "No Feedback yet. Reopened case"
            self.comments.append(
                f"Ticket reopened. {user_name} indicates: {comment}")

    def __str__(self):
        return f"🔢Ticket Number: {self.ticket_number}\n" \
               f"❗Status: {self.status}\n" \
               f"Ticket Creator: {self.ticket_creator}\n" \
               f"Caller Name: {self.caller_name}\n" \
               f"Caller Email: {self.caller_email}\n" \
               f"Feedback: {self.feedback}\n" \
               f"Description: {self.description}\n" \
               f"🔵Comments: {'  |  '.join(self.comments)}"
