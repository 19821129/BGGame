import tkinter as tk
import random

WIDTH, HEIGHT = 950, 900
PADDLE_WIDTH, PADDLE_HEIGHT = 980, 18
BALL_RADIUS = 10
BRICK_WIDTH, BRICK_HEIGHT = 75, 20


class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = WIDTH // 2
        self.y = HEIGHT // 1.2
        self.dx = random.choice([-7, 7])
        self.dy = -14
        self.id = self.canvas.create_oval(self.x - BALL_RADIUS, self.y - BALL_RADIUS,
                                          self.x + BALL_RADIUS, self.y + BALL_RADIUS,
                                          fill='cyan')

    def move(self):
        self.canvas.move(self.id, self.dx, self.dy)
        pos = self.canvas.coords(self.id)


        if pos[0] <= 0 or pos[2] >= WIDTH:
            self.dx *= -1
        if self.y <= 0:
            self.y = 400
            self.x = 400
        if pos[1] <= 0:
            self.dy *= -5

class Paddle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = (WIDTH - PADDLE_WIDTH) // 1.5
        self.id = self.canvas.create_rectangle(self.x, HEIGHT - PADDLE_HEIGHT - 15,
                                               self.x + PADDLE_WIDTH, HEIGHT - 15,
                                               fill='green')

    def move(self, dy):
        self.canvas.move(self.id, dy, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] < 0:
            self.canvas.move(self.id, -pos[0], 0)
        if pos[2] > WIDTH:
            self.canvas.move(self.id, WIDTH - pos[2], 0)


class Brick:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(x, y, x + BRICK_WIDTH, y + BRICK_HEIGHT,
                                               fill='red')
bricks = []

def create_bricks(canvas):
    if random.randint(1, 5) == 1:
        bricks.append(Brick(canvas, random.randint(1, 1000) , random.randint(1, 700)))
    return bricks

class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
        self.canvas.pack()

        self.ball = Ball(self.canvas)
        self.paddle = Paddle(self.canvas)

        self.score = 0
        self.game_over = False

        self.root.bind("<Up>", lambda event: self.paddle.move(-25))
        self.root.bind("<Down>", lambda event: self.paddle.move(25))

        self.update()

    def update(self):
        if not self.game_over:
            self.ball.move()
            self.bricks = create_bricks(self.canvas)

            ball_pos = self.canvas.coords(self.ball.id)
            paddle_pos = self.canvas.coords(self.paddle.id)

            if (paddle_pos[0] < ball_pos[0] < paddle_pos[2]) and (paddle_pos[1] < ball_pos[3] < paddle_pos[3]):
                self.ball.dy *= -1
                self.ball.y = paddle_pos[1] - BALL_RADIUS


            for brick in self.bricks[:]:
                if self.canvas.coords(brick.id) and self.check_collision(ball_pos, self.canvas.coords(brick.id)):
                    self.canvas.delete(brick.id)
                    self.bricks.remove(brick)
                    self.ball.dy *= -1
                    self.score += 1


            self.root.after(10, self.update)

    def check_collision(self, ball_pos, brick_pos):
        return (ball_pos[2] >= brick_pos[0] and ball_pos[0] <= brick_pos[2] and
                ball_pos[3] >= brick_pos[1] and ball_pos[1] <= brick_pos[3])

if __name__ == "__main__":
    root = tk.Tk()
    root.title("弹球游戏")
    game = Game(root)
    root.mainloop()