import tkinter as tk
from tkinter import simpledialog

class RecipeManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Manager")

        self.recipes = {}

        self.create_widgets()

    def create_widgets(self):
        self.recipe_name_label = tk.Label(self.root, text="Recipe Name")
        self.recipe_name_label.pack(padx=10, pady=5)

        self.recipe_name_entry = tk.Entry(self.root, width=50)
        self.recipe_name_entry.pack(padx=10, pady=5)

        self.recipe_instructions_label = tk.Label(self.root, text="Instructions")
        self.recipe_instructions_label.pack(padx=10, pady=5)

        self.recipe_instructions_text = tk.Text(self.root, width=50, height=10)
        self.recipe_instructions_text.pack(padx=10, pady=5)

        self.add_recipe_button = tk.Button(self.root, text="Add Recipe", command=self.add_recipe)
        self.add_recipe_button.pack(pady=5)

        self.view_recipe_button = tk.Button(self.root, text="View Recipe", command=self.view_recipe)
        self.view_recipe_button.pack(pady=5)

        self.search_recipe_button = tk.Button(self.root, text="Search Recipe", command=self.search_recipe)
        self.search_recipe_button.pack(pady=5)

    def add_recipe(self):
        name = self.recipe_name_entry.get()
        instructions = self.recipe_instructions_text.get("1.0", tk.END).strip()
        if name and instructions:
            self.recipes[name] = instructions
            self.recipe_name_entry.delete(0, tk.END)
            self.recipe_instructions_text.delete("1.0", tk.END)
            tk.messagebox.showinfo("Success", "Recipe added successfully.")
        else:
            tk.messagebox.showwarning("Input Error", "Please fill out both fields.")

    def view_recipe(self):
        name = simpledialog.askstring("View Recipe", "Enter the recipe name:")
        if name:
            instructions = self.recipes.get(name, "Recipe not found.")
            tk.messagebox.showinfo("Recipe Instructions", instructions)

    def search_recipe(self):
        name = simpledialog.askstring("Search Recipe", "Enter the recipe name:")
        if name:
            instructions = self.recipes.get(name, "Recipe not found.")
            tk.messagebox.showinfo("Search Result", instructions)

# Create the main window
root = tk.Tk()
app = RecipeManager(root)
root.mainloop()
