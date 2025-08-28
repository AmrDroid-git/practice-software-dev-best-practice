import tkinter as tk
import database
import config

STYLE = config.load_style()

# Load components dynamically
inputComponent = config.load_component(config.INPUT_COMPONENT_PATH, "inputComponent")
tableComponent = config.load_component(config.TABLE_COMPONENT_PATH, "tableComponent")

def run_app():
    database.init_db()

    def refresh_table():
        for row in tree.get_children():
            tree.delete(row)
        for i, person in enumerate(database.get_all_persons()):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            tree.insert("", "end", values=person, tags=(tag,))

    def add_person():
        name = entry_name.get().strip()
        age = entry_age.get().strip()
        if name and age.isdigit():
            database.add_person(name, int(age))
            entry_name.delete(0, tk.END)
            entry_age.delete(0, tk.END)
            refresh_table()

    def delete_person():
        selected_item = tree.selection()
        if selected_item:
            person_id = tree.item(selected_item[0])['values'][0]
            database.delete_person(person_id)
            refresh_table()

    # --- Root ---
    root = tk.Tk()
    root.title(STYLE["root"]["title"])
    root.geometry(STYLE["root"]["geometry"])
    root.configure(bg=STYLE["root"]["bg"])

    # Components (loaded from files via config paths)
    entry_name, entry_age = inputComponent.create_inputs(root, add_person, delete_person)
    tree = tableComponent.create_table(root)

    refresh_table()
    root.mainloop()
