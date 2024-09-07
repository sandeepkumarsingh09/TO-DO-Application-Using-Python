# def task():
#     tasks = []  # Initialize an empty list to store tasks
#     print("----WELCOME TO THE TASK MANAGEMENT APP----")
#     total_task = int(input("Enter how many tasks you want to add = "))
#     for i in range(1, total_task + 1):
#         task_name = input(f"Enter task {i} = ")
#         tasks.append(task_name)
#     print(f"Today's tasks are\n{tasks}")

#     while True:
#         try:
#             operation = int(
#                 input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
#             if operation == 1:
#                 add = input("Enter task you want to add = ")
#                 tasks.append(add)
#                 print(f"Task '{add}' has been successfully added.")
#             elif operation == 2:
#                 updated_val = input(
#                     "Enter the task name you want to update = ")
#                 if updated_val in tasks:
#                     up = input("Enter new task = ")
#                     ind = tasks.index(updated_val)
#                     tasks[ind] = up
#                     print(f"Updated task '{updated_val}' to '{up}'.")
#                 else:
#                     print("Task not found.")
#             elif operation == 3:
#                 del_val = input("Which task you want to delete = ")
#                 if del_val in tasks:
#                     ind = tasks.index(del_val)
#                     del tasks[ind]
#                     print(f"Task '{del_val}' has been deleted.")
#                 else:
#                     print("Task not found.")
#             elif operation == 4:
#                 print(f"Total tasks = {tasks}")
#             elif operation == 5:
#                 print("Closing the program....")
#                 break
#             else:
#                 print("Invalid Input. Please enter a number from 1 to 5.")
#         except ValueError:
#             print("Invalid Input. Please enter a valid number.")


# task()


import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo Application")
        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_task = task["task"]
            if task["completed"]:
                display_task += " [Done]"
            self.task_listbox.insert(tk.END, display_task)

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["completed"] = True
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
