import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from ttkbootstrap import Style

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.style = Style(theme='darkly')
        self.root.title("To-Do List App")
        self.root.geometry("600x400")
        self.root.minsize(600, 400)
        self.root.maxsize(600, 400)

        self.tasks = []
        self.filtered_tasks = []
        self.filter_mode = "All"

        self.create_widgets()

    def create_widgets(self):
        bg_color = "#FFFFFF"  
        fg_color = "#000000"  
        button_bg_color = "#3F51B5" 
        button_fg_color = "#FFFFFF"  

        font = ("Arial", 10)

        input_frame = tk.Frame(self.root, bg=bg_color)
        input_frame.pack(fill="x", padx=10, pady=(10, 0))

        tk.Label(input_frame, text="Task Name:", anchor="w", bg=bg_color, fg=fg_color, font=font).grid(row=0, column=0, padx=(0, 5), sticky="w")
        self.task_entry = tk.Entry(input_frame, width=50)
        self.task_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(self.task_entry))
        self.task_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(self.task_entry))
        self.task_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Task Description (Optional):", anchor="w", bg=bg_color, fg=fg_color, font=font).grid(row=1, column=0, padx=(0, 5), pady=5, sticky="w")
        self.description_entry = tk.Entry(input_frame, width=50)
        self.description_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(self.description_entry))
        self.description_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(self.description_entry))
        self.description_entry.grid(row=1, column=1)

        tk.Label(input_frame, text="Due Date (dd-mm-yyyy) (Optional):", anchor="w", bg=bg_color, fg=fg_color, font=font).grid(row=2, column=0, padx=(0, 5), sticky="w")
        self.date_entry = tk.Entry(input_frame, width=50)
        self.date_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(self.date_entry))
        self.date_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(self.date_entry))
        self.date_entry.grid(row=2, column=1)

        add_button = tk.Button(input_frame, text="Add Task", command=self.add_task, bg=button_bg_color, fg=button_fg_color, font=font)
        add_button.grid(row=3, columnspan=2, pady=(10, 0))

        button_frame = tk.Frame(self.root, bg=bg_color)
        button_frame.pack(fill="x", padx=10, pady=(5, 10))

        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, bg=button_bg_color, fg=button_fg_color, font=font)
        delete_button.pack(side="right", padx=(0, 5))

        complete_button = tk.Button(button_frame, text="Mark as Complete", command=self.mark_as_complete, bg=button_bg_color, fg=button_fg_color, font=font)
        complete_button.pack(side="left")

        button_frame.pack(side="bottom", fill="x", padx=10, pady=(0, 10))

        filter_frame = tk.Frame(self.root, bg=bg_color)
        filter_frame.pack(fill="x", padx=10, pady=(5, 0))

        ttk.Button(filter_frame, text="All", command=lambda: self.filter_tasks("All")).pack(side="left")
        ttk.Button(filter_frame, text="Pending", command=lambda: self.filter_tasks("Pending")).pack(side="left")
        ttk.Button(filter_frame, text="Completed", command=lambda: self.filter_tasks("Completed")).pack(side="left")

        self.tree = ttk.Treeview(self.root, columns=("Name", "Description", "Due Date", "Added Date", "Status"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Due Date", text="Due Date")
        self.tree.heading("Added Date", text="Added Date")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill="both", expand=True, padx=10, pady=(5, 10))

        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Mark as Complete", command=self.mark_as_complete)
        self.context_menu.add_command(label="Delete Task", command=self.delete_task)

        self.tree.bind("<Button-3>", self.show_context_menu)

    def show_context_menu(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            self.context_menu.post(event.x_root, event.y_root)

    def clear_placeholder(self, entry):
        if entry.get() == "Task Name" or entry.get() == "Due Date (dd-mm-yyyy) (Optional)" or entry.get() == "Task Description (Optional)":
            entry.delete(0, tk.END)

    def restore_placeholder(self, entry):
        if not entry.get():
            if entry == self.task_entry:
                entry.insert(0, "")
            elif entry == self.date_entry:
                entry.insert(0, "")
            elif entry == self.description_entry:
                entry.insert(0, "")

    def add_task(self):
        name = self.task_entry.get().strip()
        description_optional = self.description_entry.get().strip()
        due_date_str = self.date_entry.get().strip()

        if not name or name == "Task Name":
            messagebox.showwarning("Warning", "Please enter a task name.")
            return

        due_date = None
        if due_date_str and due_date_str != "Due Date (dd-mm-yyyy) (Optional)":
            try:
                due_date = datetime.strptime(due_date_str, "%d-%m-%Y")
            except ValueError:
                messagebox.showwarning("Warning", "Invalid date format. Please use dd-mm-yyyy.")
                return

        added_date = datetime.now()

        task = {"name": name, "description_optional": description_optional, "due_date": due_date, "added_date": added_date, "status": "Pending"}
        self.tasks.append(task)
        self.refresh_tasks()

        self.task_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def refresh_tasks(self):
        self.tree.delete(*self.tree.get_children())

        if self.filter_mode == "All":
            self.filtered_tasks = self.tasks
        elif self.filter_mode == "Pending":
            self.filtered_tasks = [task for task in self.tasks if task["status"] == "Pending"]
        elif self.filter_mode == "Completed":
            self.filtered_tasks = [task for task in self.tasks if task["status"] == "Completed"]

        for task in self.filtered_tasks:
            self.tree.insert("", "end", values=(
                task["name"],
                task["description_optional"],
                task["due_date"].strftime("%d-%m-%Y") if task["due_date"] else "",
                task["added_date"].strftime("%d-%m-%Y %H:%M:%S"),
                task["status"]
            ))

    def filter_tasks(self, mode):
        self.filter_mode = mode
        self.refresh_tasks()

    def mark_as_complete(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = self.tree.index(selected_item)
            self.filtered_tasks[index]["status"] = "Completed"
            self.refresh_tasks()

    def delete_task(self):
        selected_items = self.tree.selection()
        if selected_items:
            for item in selected_items:
                index = self.tree.index(item)
                del self.tasks[self.tasks.index(self.filtered_tasks[index])]
                self.refresh_tasks()

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

