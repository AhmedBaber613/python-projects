import random
import time
import os

# Set up the game
def setup_game():
    global bird_pos, bird_velocity, gravity, gap_size, obstacle_gap, score
    bird_pos = 5
    bird_velocity = 0
    gravity = 1
    gap_size = 4
    obstacle_gap = 10
    score = 0

def draw_game():
    os.system('clear')  # Clears the console (for Linux/Unix)
    print("Flappy Bird - Current Score:", score)
    for i in range(10):
        if i == bird_pos:
            print("o", end="")
        else:
            print(" ", end="")
        if i == bird_pos + 2:
            print("|", end="")
        else:
            print(" ", end="")
        print(" " * (obstacle_gap - gap_size), end="")
        if i >= obstacle_gap and i < obstacle_gap + gap_size:
            print(" " * gap_size, end="")
        else:
            print("X", end="")
        print()

def update_game():
    global bird_pos, bird_velocity, gravity, gap_size, obstacle_gap, score
    bird_velocity += gravity
    bird_pos += bird_velocity

    # Check if bird hits the ground or the ceiling
    if bird_pos < 0:
        bird_pos = 0
        bird_velocity = 0
    if bird_pos >= 10:
        bird_pos = 9
        bird_velocity = 0

    # Check if bird passes through the gap
    if bird_pos == obstacle_gap or bird_pos == obstacle_gap + gap_size:
        score += 1

    # Move obstacle
    obstacle_gap -= 1
    if obstacle_gap < -1 * gap_size:
        obstacle_gap = 10
        score += 1

# Main game loop
setup_game()
while True:
    draw_game()
    update_game()
    time.sleep(0.1)  # Adjust the speed of the game by changing the sleep duration
