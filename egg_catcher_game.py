import tkinter as tk
import random

class EggCatcherGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Egg Catcher Game")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="skyblue")
        self.canvas.pack()

        self.basket_width = 100
        self.basket_height = 20
        self.basket_x = 250
        self.basket_y = 350
        self.basket = self.canvas.create_rectangle(self.basket_x, self.basket_y,
                                                   self.basket_x + self.basket_width,
                                                   self.basket_y + self.basket_height,
                                                   fill="brown")

        self.egg_radius = 15
        self.eggs = []
        self.egg_speed = 5

        self.score = 0
        self.score_text = self.canvas.create_text(50, 20, text=f"Score: {self.score}", font=("Helvetica", 16), fill="black")

        self.game_over = False

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.spawn_egg()
        self.update_game()

    def spawn_egg(self):
        if not self.game_over:
            x = random.randint(self.egg_radius, 600 - self.egg_radius)
            egg = self.canvas.create_oval(x - self.egg_radius, 0,
                                          x + self.egg_radius, 2 * self.egg_radius,
                                          fill="white", outline="black")
            self.eggs.append(egg)
            # Spawn new egg every 1500 ms
            self.root.after(1500, self.spawn_egg)

    def move_left(self, event):
        if self.basket_x > 0:
            self.basket_x -= 20
            self.canvas.move(self.basket, -20, 0)

    def move_right(self, event):
        if self.basket_x + self.basket_width < 600:
            self.basket_x += 20
            self.canvas.move(self.basket, 20, 0)

    def update_game(self):
        if self.game_over:
            return

        eggs_to_remove = []
        for egg in self.eggs:
            self.canvas.move(egg, 0, self.egg_speed)
            pos = self.canvas.coords(egg)
            if pos[3] >= self.basket_y:
                # Check if egg is within basket horizontally
                if pos[0] >= self.basket_x and pos[2] <= self.basket_x + self.basket_width:
                    self.score += 1
                    self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                    eggs_to_remove.append(egg)
                else:
                    # Missed egg - game over
                    self.game_over = True
                    self.show_game_over()
                    return
            elif pos[1] > 400:
                eggs_to_remove.append(egg)

        for egg in eggs_to_remove:
            self.canvas.delete(egg)
            self.eggs.remove(egg)

        self.root.after(50, self.update_game)

    def show_game_over(self):
        self.canvas.create_text(300, 200, text="Game Over!", font=("Helvetica", 32), fill="red")
        self.canvas.create_text(300, 240, text=f"Final Score: {self.score}", font=("Helvetica", 24), fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    game = EggCatcherGame(root)
    root.mainloop()
