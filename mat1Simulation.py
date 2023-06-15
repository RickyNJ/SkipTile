import time
import tkinter as tk
import paho.mqtt.client as mqtt
import numpy as np

CELL_SIZE = 10
GRID_SIZE = 40
WINDOW_WIDTH = CELL_SIZE * GRID_SIZE
WINDOW_HEIGHT = CELL_SIZE * GRID_SIZE

broker_hostname = "localhost"
broker_port = 1883
topic = "matten/1"
client = mqtt.Client()
client.connect(broker_hostname, broker_port)
array = np.zeros(1601)
old_cursor_x = 0
old_cursor_y = 0

def draw_grid(canvas, cursor_x, cursor_y):
    canvas.delete("all")
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            if i == cursor_y and j == cursor_x:
                canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")

def update_cursor(event):
    global cursor_x, cursor_y, old_cursor_x, old_cursor_y
    cursor_x = event.x // CELL_SIZE
    cursor_y = event.y // CELL_SIZE
    # print(f"Cursor location: ({cursor_x}, {cursor_y})")
    if cursor_x != old_cursor_x or cursor_y != old_cursor_y:
        old_cursor_x = cursor_x
        old_cursor_y = cursor_y
        mes = np.zeros(1601, dtype= int)
        cursorlocation = cursor_y*40 + cursor_x
        mes[cursorlocation] = int(500)
        print("x " + str(cursor_x))
        print("y " + str(cursor_y))
        string_representation = ", ".join(str(x) for x in mes)
        client.publish(topic, string_representation)


def main():
    global cursor_x, cursor_y, array

    root = tk.Tk()
    root.title("Grid Display")
    canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack()
    canvas.bind("<Motion>", update_cursor)
    cursor_x = 0
    cursor_y = 0

    while True:
        draw_grid(canvas, cursor_x, cursor_y)
        root.update()
        time.sleep(0.01)

if __name__ == "__main__":
    main()
