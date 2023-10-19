from ticket import Ticket
print('welcome to service desk')

tickets = []


def list_tickets(status):
    list_of_tickets = []
    for i in tickets:
        if i.status == status:
            list_of_tickets.append(i.ticket_number)
    return list_of_tickets


while True:
    action = input(
        '\n\n❓SELECT OPTION: \n1: create new ticket. \n2: reopen ticket. \n3: list all tickets. \n4: resolve ticket. \n5: Place Feedback \n6: Stats: ')
    print('\n\n')
    if action == '1':  # new ticket
        operator_name = input('enter creator name (operator): ')
        callerID = input('enter caller UserID: ')
        caller_email = input('enter caller email: ')
        description = input('describe the issue: ')
        new_ticket = Ticket(operator_name, callerID, caller_email, description)
        if description.find('password reset') > -1:
            new_ticket.reset_password(operator_name)
        tickets.append(new_ticket)

    elif action == '2':  # reopen ticket
        print(
            f"\nClosed Tickets: {list_tickets('Resolved')}")
        ticket_id = int(input('enter the ticket ID: '))-2000
        if ticket_id+2000 in list_tickets('Resolved'):
            reopen_reason = input('enter reason for reopening: ')
            tickets[ticket_id].reopen_ticket("Caller", reopen_reason)
        else:
            print('number not valid ⛔')

    elif action == '3':  # list all tickets
        if len(tickets) == 0:
            print("\n\n\n NO TICKETS ⛔")
        else:
            for i in tickets:
                print(i)

    elif action == '4':  # resolve ticket
        print(f"\nOpen tickets: {list_tickets('Open')}")
        ticket_id = int(input('enter the ticket ID: '))-2000
        if ticket_id+2000 in list_tickets('Open'):
            admin_name = input('enter Service desk operator: ')
            solve_comment = input('enter resolve notes: ')
            tickets[ticket_id].solve_ticket(solve_comment, admin_name)
        else:
            print('number not valid ⛔')

    elif action == '5':  # place feedback
        print(f"\nClosed tickets: {list_tickets('Resolved')}")
        ticket_id = int(input('enter the ticket ID: '))-2000
        if ticket_id+2000 in list_tickets('Resolved'):
            rating = input("please rate 1-5: ")
            comment = input("Enter your comments: ")
            tickets[ticket_id].submit_feedback(rating, comment)
        else:
            print('number not valid ⛔')

    elif action == '6':  # stats
        print(
            f"\nSTATS: \n{len(list_tickets('Open'))} Open Tickets: {list_tickets('Open')}\nTotal Tickets: {len(tickets)}")

    else:
        print('no valid input ⛔')
