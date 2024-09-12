import tkinter as tk
from tkinter import messagebox, simpledialog

class Kaffeemaschine:
    def __init__(self, kaffee, tassen, wasser, milch, zucker):
        self.kaffee = kaffee
        self.tassen = tassen
        self.wasser = wasser
        self.milch = milch
        self.zucker = zucker

    def kaffee_zubereiten(self, kaffee_art, zucker):
        if zucker:
            self.zucker -= 5

        if kaffee_art == "Espresso":
            self.kaffee -= 50
            self.wasser -= 30
        elif kaffee_art == "Filterkaffee":
            self.kaffee -= 50
            self.wasser -= 200
        elif kaffee_art == "Latte":
            self.kaffee -= 50
            self.wasser -= 200
            self.milch -= 30
        elif kaffee_art == "Cappuccino":
            self.kaffee -= 50
            self.wasser -= 200
            self.milch -= 30

        self.tassen -= 1
        return kaffee_art

    def kaffeebericht(self):
        return {
            "Kaffee": self.kaffee,
            "Wasser": self.wasser,
            "Milch": self.milch,
            "Zucker": self.zucker,
            "Tassen": self.tassen
        }

class KaffeemaschineGUI:
    def __init__(self, master):
        self.master = master
        self.kaffeemaschine = Kaffeemaschine(3500, 25, 3000, 750, 125)
        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.main_frame.pack(fill="both", expand=True)

        self.title_label = tk.Label(self.main_frame, text="Kaffeemaschine", font=("Arial", 24), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        self.resource_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.resource_frame.pack(fill="x", padx=20)

        self.kaffee_label = tk.Label(self.resource_frame, text="Kaffee:", font=("Arial", 16), bg="#f0f0f0")
        self.kaffee_label.grid(row=0, column=0, padx=10)
        self.kaffee_value_label = tk.Label(self.resource_frame, text=str(self.kaffeemaschine.kaffee), font=("Arial", 16), bg="#f0f0f0")
        self.kaffee_value_label.grid(row=0, column=1, padx=10)

        self.wasser_label = tk.Label(self.resource_frame, text="Wasser:", font=("Arial", 16), bg="#f0f0f0")
        self.wasser_label.grid(row=1, column=0, padx=10)
        self.wasser_value_label = tk.Label(self.resource_frame, text=str(self.kaffeemaschine.wasser), font=("Arial", 16), bg="#f0f0f0")
        self.wasser_value_label.grid(row=1, column=1, padx=10)

        self.milch_label = tk.Label(self.resource_frame, text="Milch:", font=("Arial", 16), bg="#f0f0f0")
        self.milch_label.grid(row=2, column=0, padx=10)
        self.milch_value_label = tk.Label(self.resource_frame, text=str(self.kaffeemaschine.milch), font=("Arial", 16), bg="#f0f0f0")
        self.milch_value_label.grid(row=2, column=1, padx=10)

        self.zucker_label = tk.Label(self.resource_frame, text="Zucker:", font=("Arial", 16), bg="#f0f0f0")
        self.zucker_label.grid(row=3, column=0, padx=10)
        self.zucker_value_label = tk.Label(self.resource_frame, text=str(self.kaffeemaschine.zucker), font=("Arial", 16), bg="#f0f0f0")
        self.zucker_value_label.grid(row=3, column=1, padx=10)

        self.tassen_label = tk.Label(self.resource_frame, text="Tassen:", font=("Arial", 16), bg="#f0f0f0")
        self.tassen_label.grid(row=4, column=0, padx=10)
        self.tassen_value_label = tk.Label(self.resource_frame, text=str(self.kaffeemaschine.tassen), font=("Arial", 16), bg="#f0f0f0")
        self.tassen_value_label.grid(row=4, column=1, padx=10)

        self.kaffee_zubereiten_button = tk.Button(self.main_frame, text="Kaffee zubereiten", command=self.kaffee_zubereiten)
        self.kaffee_zubereiten_button.pack(pady=20)

    def kaffee_zubereiten(self):
        kaffee_art = simpledialog.askstring("Kaffeeauswahl", "Welchen Kaffee möchtest du trinken? (Espresso, Filterkaffee, Latte, Cappuccino)")
        zucker = messagebox.askyesno("Zucker", "Möchtest du Zucker?")
        produkt = self.kaffeemaschine.kaffee_zubereiten(kaffee_art, zucker)
        self.update_labels()
        messagebox.showinfo("Kaffee zubereitet", f"Dein {produkt} ist fertig!")

    def update_labels(self):
        self.kaffee_value_label.config(text=str(self.kaffeemaschine.kaffee))
        self.wasser_value_label.config(text=str(self.kaffeemaschine.wasser))
        self.milch_value_label.config(text=str(self.kaffeemaschine.milch))
        self.zucker_value_label.config(text=str(self.kaffeemaschine.zucker))
        self.tassen_value_label.config(text=str(self.kaffeemaschine.tassen))
    def kaffee_zubereiten(self):
        kaffee_art = simpledialog.askstring("Kaffeeauswahl", "Welchen Kaffee möchtest du trinken? (Espresso, Filterkaffee, Latte, Cappuccino)")
        zucker = messagebox.askyesno("Zucker", "Möchtest du Zucker?")
        produkt = self.kaffeemaschine.kaffee_zubereiten(kaffee_art, zucker)
        self.update_labels()
        messagebox.showinfo("Kaffee zubereitet", f"Dein {produkt} ist fertig!")

    def update_labels(self):
        self.kaffee_value_label.config(text=str(self.kaffeemaschine.kaffee))
        self.wasser_value_label.config(text=str(self.kaffeemaschine.wasser))
        self.milch_value_label.config(text=str(self.kaffeemaschine.milch))
        self.zucker_value_label.config(text=str(self.kaffeemaschine.zucker))
        self.tassen_value_label.config(text=str(self.kaffeemaschine.tassen))

if __name__ == "__main__":
    root = tk.Tk()
    app = KaffeemaschineGUI(root)
    root.mainloop()
