import torch
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class AdvancedCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Calculator")

     
        self.label = ttk.Label(master, text="Enter numerical data (comma-separated):")
        self.label.pack(pady=10)

        self.input_entry = ttk.Entry(master)
        self.input_entry.pack(pady=10)

       
        self.calculate_button = ttk.Button(master, text="Perform Tensor Operations", command=self.calculate_tensor_operations)
        self.calculate_button.pack(pady=20)

       
        self.visualize_button = ttk.Button(master, text="Visualize Tensor", command=self.visualize_tensor)
        self.visualize_button.pack(pady=20)

    def calculate_tensor_operations(self):
        try:
            input_data = [float(x) for x in self.input_entry.get().split(',')]
            tensor_data = torch.tensor(input_data)

           
            result_tensor = torch.sin(tensor_data)

            messagebox.showinfo("Tensor Operations Result", f"Result Tensor: {result_tensor}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numerical data.")

    def visualize_tensor(self):
        try:
            input_data = [float(x) for x in self.input_entry.get().split(',')]
            tensor_data = torch.tensor(input_data)

           
            fig, ax = plt.subplots()
            sns.barplot(x=np.arange(len(tensor_data)), y=tensor_data.numpy(), ax=ax)
            ax.set_title("Visualization of Input Tensor")
            ax.set_xlabel("Index")
            ax.set_ylabel("Value")
            plt.show()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numerical data.")


def main():
    root = tk.Tk()
    app = AdvancedCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
