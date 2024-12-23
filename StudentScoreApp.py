import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import matplotlib.pyplot as plt
import numpy as np

class StudentScoreApp:
    def __init__(self, master):
        self.master = master
        master.title("Dynamic Student Score Visualization 📊")
        master.geometry("600x400")
        master.configure(bg='lightpink')  # Change background color to light pink

        self.student_names = []
        self.scores = []

        self.label = tk.Label(master, text="Student Score Visualization", font=("Helvetica", 16), bg='lightpink')
        self.label.pack(pady=10)

        self.entry_button = tk.Button(master, text="Input Scores", command=self.input_scores, width=20)
        self.entry_button.pack(pady=5)

        self.graph_button = tk.Button(master, text="Show Graph", command=self.show_graph, width=20)
        self.graph_button.pack(pady=5)

        self.graph_type_label = tk.Label(master, text="Select Graph Type:", bg='lightpink')
        self.graph_type_label.pack(pady=10)

        self.graph_type_var = tk.StringVar(master)
        self.graph_type_var.set("Bar Graph")  # Default value
        self.graph_type_menu = tk.OptionMenu(master, self.graph_type_var,
                                             "Bar Graph", "Line Graph", "Scatter Plot", "Histogram", "Box Plot",
                                              "Area Chart", "Step Plot", "Error Bar Plot")
        self.graph_type_menu.pack(pady=5)

    def input_scores(self):
        self.student_names = []
        self.scores = []

        num_students = simpledialog.askinteger("Input", "How many students? (max 10)", minvalue=1, maxvalue=10)

        if num_students is None:
            return  # Exit if no input is provided

        for i in range(num_students):
            name = simpledialog.askstring("Input", f"Enter name for Student {i + 1}:")
            if name is None:
                return  # Exit if no input is provided

            score = simpledialog.askinteger("Input", f"Enter score for {name} (0-100):", minvalue=0, maxvalue=100)
            if score is None:
                return  # Exit if no input is provided

            self.student_names.append(name)
            self.scores.append(score)

    def show_graph(self):
        graph_type = self.graph_type_var.get()

        if not self.student_names or not self.scores:
            messagebox.showwarning("Input Error", "Please input student scores first.")
            return

        plt.figure(figsize=(10, 6))

        if graph_type == "Bar Graph":
            plt.bar(self.student_names, self.scores, color='pink', alpha=0.7)
            plt.title('Student Scores - Bar Graph')
        elif graph_type == "Line Graph":
            plt.plot(self.student_names, self.scores, marker='o', color='pink')
            plt.title('Student Scores - Line Graph')
        elif graph_type == "Scatter Plot":
            plt.scatter(self.student_names, self.scores, color='pink', s=100)
            plt.title('Student Scores - Scatter Plot')
        elif graph_type == "Histogram":
            plt.hist(self.scores, bins=5, color='pink', alpha=0.7)
            plt.title('Student Scores - Histogram')
            plt.xticks(range(0, 101, 10))
        elif graph_type == "Box Plot":
            plt.boxplot(self.scores, patch_artist=True, boxprops=dict(facecolor='pink'))
            plt.title('Student Scores - Box Plot')
            plt.xticks([1], ['Scores'])
        elif graph_type == "Area Chart":
            plt.fill_between(self.student_names, self.scores, color='pink', alpha=0.5)
            plt.title('Student Scores - Area Chart')
        elif graph_type == "Step Plot":
            plt.step(self.student_names, self.scores, where='mid', color='pink')
            plt.title('Student Scores - Step Plot')
        elif graph_type == "Error Bar Plot":
            plt.errorbar(self.student_names, self.scores, yerr=5, fmt='o', color='pink', capsize=5)
            plt.title('Student Scores - Error Bar Plot')

        plt.xlabel('Students')
        plt.ylabel('Scores')
        plt.ylim(0, 100)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentScoreApp(root)
    root.mainloop()
