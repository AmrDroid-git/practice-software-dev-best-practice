import tkinter as tk
from tkinter import ttk
import config

STYLE = config.load_style()

def create_table(root):
    table_frame = tk.Frame(root)
    table_frame.pack(expand=True, fill="both", pady=10, padx=10)

    tree = ttk.Treeview(table_frame, columns=("ID", "Name", "Age"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")

    tree.column("ID", anchor="center", width=50)
    tree.column("Name", anchor="w", width=200)
    tree.column("Age", anchor="center", width=80)

    vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=vsb.set)
    vsb.pack(side="right", fill="y")
    tree.pack(expand=True, fill="both")

    # Styling
    style = ttk.Style()
    style.configure("Treeview", font=STYLE["treeview"]["font"], rowheight=STYLE["treeview"]["rowheight"])
    style.configure("Treeview.Heading", font=STYLE["treeview"]["heading_font"])
    tree.tag_configure("evenrow", background=STYLE["treeview"]["alt_even"])
    tree.tag_configure("oddrow", background=STYLE["treeview"]["alt_odd"])

    return tree
