import tkinter as tk
import config

STYLE = config.load_style()

def create_inputs(root, add_person_callback, delete_person_callback):
    # --- Top bar with delete ---
    top_frame = tk.Frame(root, bg=STYLE["root"]["bg"])
    top_frame.pack(fill="x", pady=5)

    btn_delete = tk.Button(
        top_frame,
        text="Delete Selected",
        command=delete_person_callback,
        **STYLE["button_delete"]
    )
    btn_delete.pack(side="right", padx=10)

    # --- Input row ---
    input_frame = tk.Frame(root, bg=STYLE["root"]["bg"])
    input_frame.pack(pady=5)

    tk.Label(input_frame, text="Name:", **STYLE["label"]).pack(side="left", padx=5)
    entry_name = tk.Entry(input_frame, width=STYLE["entry"]["width_name"], font=STYLE["entry"]["font"])
    entry_name.pack(side="left", padx=5)

    tk.Label(input_frame, text="Age:", **STYLE["label"]).pack(side="left", padx=5)
    entry_age = tk.Entry(input_frame, width=STYLE["entry"]["width_age"], font=STYLE["entry"]["font"])
    entry_age.pack(side="left", padx=5)

    btn_add = tk.Button(
        input_frame,
        text="Add Person",
        command=add_person_callback,
        **STYLE["button_add"]
    )
    btn_add.pack(side="left", padx=15)

    return entry_name, entry_age
