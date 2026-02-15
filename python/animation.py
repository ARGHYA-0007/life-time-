import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(0, 10)   # x-axis limits
ax.set_ylim(0, 10)   # y-axis limits

# Create a ball (plot a red circle)
ball, = ax.plot(5, 9, 'o', markersize=20, color="red")

# Ball parameters
x = 5              # fixed x position
y = 9              # starting y position
v = 0              # initial velocity
g = -0.5           # gravity
bounce_factor = 0.8  # energy retained after bounce

# Update function for animation
def update(frame):
    global y, v
    v += g      # apply gravity
    y += v      # update position

    # Bounce condition
    if y <= 1:
        y = 1
        v = -v * bounce_factor

    ball.set_data(x, y)
    return ball,

# Run animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=30, blit=True)

plt.show()


