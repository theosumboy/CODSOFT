import tkinter as tk

# Define functions for managing to-do list items
def add_task():
    task_text = task_entry.get()
    if task_text:
        task_list.insert(tk.END, task_text)
        task_entry.delete(0, tk.END)

def remove_task():
    if task_list.curselection():
        task_list.delete(task_list.curselection()[0])

def mark_task_as_done():
    if task_list.curselection():
        selected_task = task_list.get(task_list.curselection()[0])
        task_list.delete(task_list.curselection()[0])
        task_list.insert(tk.END, f"✔ {selected_task}")

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create labels and entry field for task input
task_label = tk.Label(window, text="Enter task:")
task_label.grid(row=0, column=0, pady=5)
task_entry = tk.Entry(window)
task_entry.grid(row=0, column=1, pady=5)

# Create buttons for adding, removing, and marking tasks as done
add_button = tk.Button(window, text="Add", command=add_task)
add_button.grid(row=1, column=0, pady=5)
remove_button = tk.Button(window, text="Remove", command=remove_task)
remove_button.grid(row=1, column=1, pady=5)
done_button = tk.Button(window, text="Mark as Done", command=mark_task_as_done)
done_button.grid(row=1, column=2, pady=5)

# Create a listbox to display the to-do list items
task_list = tk.Listbox(window)
task_list.grid(row=2, column=0, columnspan=3, pady=5)

# Start the event loop
window.mainloop()
