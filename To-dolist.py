import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Create a text box to input tasks
        self.task_entry = tk.Entry(root, width=35)
        self.task_entry.pack(pady=10)

        # Create a button to add tasks
        self.add_button = tk.Button(root, text="Add Task",bg= "pink",command=self.add_task)
        self.add_button.pack(pady=5)

         # Create a text box to display tasks
        self.task_list = tk.Text(root, height=10, width=35)
        self.task_list.pack(pady=10)

        # Create a button to display tasks
        self.display_button = tk.Button(root, text="Display Tasks",bg="pink", command=self.display_tasks)
        self.display_button.pack(pady=5)

        # Create a button to delete tasks
        self.delete_button = tk.Button(root, text="Delete Task",bg="pink", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Create a button to update tasks
        self.update_button = tk.Button(root, text="Update Task",bg="pink", command=self.update_task)
        self.update_button.pack(pady=5)

        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, f"- {task}\n")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Error", "Please enter a task.")

    def delete_task(self):
        if self.task_list.get("1.0", tk.END):
            selected_task = self.task_list.selection_get()
            self.tasks.remove(selected_task)
            self.task_list.delete("1.0", tk.END)
            for task in self.tasks:
                self.task_list.insert(tk.END, f"- {task}\n")
        else:
            messagebox.showinfo("Error", "No task selected.")

    def update_task(self):
        if self.task_list.get("1.0", tk.END):
            selected_task = self.task_list.selection_get()
            new_task = self.task_entry.get()
            if new_task:
                index = self.tasks.index(selected_task)
                self.tasks[index] = new_task
                self.task_list.delete("1.0", tk.END)
                for task in self.tasks:
                    self.task_list.insert(tk.END, f"- {task}\n")
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showinfo("Error", "Please enter a new task.")
        else:
            messagebox.showinfo("Error", "No task selected.")
    def display_tasks(self):
        self.task_list.delete("1.0", tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, f"- {task}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)


    root.mainloop()