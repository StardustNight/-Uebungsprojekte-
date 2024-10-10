import tkinter as tk

class Ampel:
    def __init__(self, master, image_file, position_y):
        self.image = tk.PhotoImage(file=image_file)
        self.canvas = tk.Canvas(master, width=self.image.width(), height=self.image.height(), bg='black')
        self.canvas.pack(side=tk.TOP)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        self.red_light = self.canvas.create_oval(70, 120, 130, 180, fill='gray')
        self.yellow_light = self.canvas.create_oval(70, 190, 130, 250, fill='gray')
        self.green_light = self.canvas.create_oval(70, 260, 130, 320, fill='gray')

    def switch(self, color):
        self.canvas.itemconfig(self.red_light, fill='gray')
        self.canvas.itemconfig(self.yellow_light, fill='gray')
        self.canvas.itemconfig(self.green_light, fill='gray')
        if color == 'rot':
            self.canvas.itemconfig(self.red_light, fill='red')
        elif color == 'rot-gelb':
            self.canvas.itemconfig(self.red_light, fill='red')
            self.canvas.itemconfig(self.yellow_light, fill='yellow')
        elif color == 'gelb':
            self.canvas.itemconfig(self.yellow_light, fill='yellow')
        elif color == 'grün':
            self.canvas.itemconfig(self.green_light, fill='green')

class AutoAmpel(Ampel):
    def __init__(self, master):
        super().__init__(master, 'Straßenampel.png', 0)
        self.states = ['rot', 'rot-gelb', 'grün', 'gelb']
        self.current_state = 0
        self.switch(self.states[self.current_state])

    def change_state(self):
        self.current_state = (self.current_state + 1) % len(self.states)
        self.switch(self.states[self.current_state])

class FussgaengerAmpel(Ampel):
    def __init__(self, master):
        super().__init__(master, 'Fussgängerampel.png', 250)
        self.states = ['rot', 'grün']
        self.current_state = 0
        self.switch(self.states[self.current_state])

    def change_state(self):
        self.current_state = (self.current_state + 1) % len(self.states)
        self.switch(self.states[self.current_state])

def main():
    root = tk.Tk()
    root.title('Ampelsteuerung')

    auto_ampel_frame = tk.Frame(root)
    auto_ampel_frame.pack(side=tk.TOP)
    auto_ampel = AutoAmpel(auto_ampel_frame)

    fussgaenger_ampel_frame = tk.Frame(root)
    fussgaenger_ampel_frame.pack(side=tk.TOP)
    fussgaenger_ampel = FussgaengerAmpel(fussgaenger_ampel_frame)

    def auto_change():
        auto_ampel.change_state()
        root.after(2000, auto_change)

    def fussgaenger_change():
        fussgaenger_ampel.change_state()
        root.after(3000, fussgaenger_change)

    auto_button = tk.Button(root, text="Auto-Ampel wechseln", command=auto_ampel.change_state)
    auto_button.pack(side=tk.TOP)

    fussgaenger_button = tk.Button(root, text="Fußgänger-Ampel wechseln", command=fussgaenger_ampel.change_state)
    fussgaenger_button.pack(side=tk.TOP)

    auto_change()
    fussgaenger_change()

    root.mainloop()

if __name__ == '__main__':
    main()
