import tkinter as tk
import yaml


# Create a function for writing values off to a yaml file
def write(dictionary):
    with open('data.yml', 'w') as outfile:
        yaml.dump(dictionary, outfile, sort_keys=False)


# Create a function to format the dictionary properly
def form(name, description, hp):
    data = dict(
            name=name,
            description=description,
            hp=hp,
    )
    return data


# Create a function to saving the entry to file
def save():
    name = name_entry.get()
    description = description_entry.get()
    hp = hp_entry.get()
    dictionary = form(name, description, hp)
    write(dictionary)
    status_label["text"] = "Saved"


# Create a function to saving the entry to file
def clear():
    name_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    hp_entry.delete(0, tk.END)
    status_label["text"] = "Cleared"


if __name__ == "__main__":

    # Create a Tkinter window
    window = tk.Tk()

    # Set the window title
    window.title("Options")

    # Create creature label and entry
    name_label = tk.Label(text="Name")
    name_entry = tk.Entry()

    # Create description label and entry
    description_label = tk.Label(text="description")
    description_entry = tk.Entry()

    # Create creature label and entry
    hp_label = tk.Label(text="hitpoint")
    hp_entry = tk.Entry()

    # Create the buttons
    save_button = tk.Button(window, text="Save", command=save)
    clear_button = tk.Button(window, text="Clear", command=clear)

    # Create a status label that is empty
    status_label = tk.Label(text="")

    # Add creature name label and entry to window
    name_label.pack()
    name_entry.pack()

    # Add creature description label and entry to window
    description_label.pack()
    description_entry.pack()

    # Add creature name label and entry to window
    hp_label.pack()
    hp_entry.pack()

    # Add the buttons to the window
    save_button.pack()
    clear_button.pack()

    # Add the status label to window
    status_label.pack()

    # Run the Tkinter event loop
    window.mainloop()
