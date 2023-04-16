import tkinter as tk
from datetime import date
from tkcalendar import DateEntry


def calculate():
    """Calculate the number of days since the selected date.

       Returns: str: A string representation of the number of days since the
       selected date.
    """
    # get the selected date from the DateEntry widget
    user_input = start_date.get_date()

    # check if the selected date is later than today
    if user_input > date.today():
        result = "0 days"
    else:
        # calculate the number of days since the selected date
        days = (date.today() - user_input).days
        result = f"{days}"

    return result


def update_label():
    """Update the result label with the number of days since the selected
    date. """
    answer = f"You have gone {calculate()} days without porn."
    result_label.config(text=answer)


# create the main window
window = tk.Tk()
window.title("Streak Counter")
window.geometry("300x200")
window.resizable(False, False)

# create the widgets
no_porn = tk.Label(window, text="When was the last time you watched porn?")
start_date = DateEntry(window, width=12, background='darkblue',
                       foreground='white', borderwidth=2)
result_label = tk.Label(window, text="")
button = tk.Button(window, text="Enter",
                   command=update_label)

# pack the widgets into the window
no_porn.pack()
start_date.pack()
button.pack()
result_label.pack()

# run the main event loop
window.mainloop()
