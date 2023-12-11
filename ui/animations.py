```python
import tkinter as tk
from tkinter import PhotoImage

# Animation class to handle various UI animations
class Animation:
    def __init__(self, canvas):
        self.canvas = canvas
        self.animations = []

    def add(self, image_path, position, duration, loop=False):
        """
        Add an animation to the canvas.
        :param image_path: Path to the image file.
        :param position: Tuple (x, y) for the image position.
        :param duration: Duration of the animation in milliseconds.
        :param loop: Boolean indicating if the animation should loop.
        """
        image = PhotoImage(file=image_path)
        animation = {
            'image': image,
            'position': position,
            'duration': duration,
            'loop': loop,
            'id': None
        }
        self.animations.append(animation)

    def play(self):
        """
        Play all animations added to the canvas.
        """
        for animation in self.animations:
            if animation['id'] is None:
                animation['id'] = self.canvas.create_image(
                    animation['position'][0],
                    animation['position'][1],
                    image=animation['image']
                )
            self.canvas.after(animation['duration'], self._update, animation)

    def _update(self, animation):
        """
        Update the animation state. If loop is True, restart the animation.
        :param animation: The animation to update.
        """
        if animation['loop']:
            self.canvas.delete(animation['id'])
            animation['id'] = None
            self.play()
        else:
            self.canvas.delete(animation['id'])
            self.animations.remove(animation)

# Example usage of the Animation class
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gamified Workflow Automation Tool")
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    # Initialize the Animation object
    animation = Animation(canvas)

    # Add animations (example paths and positions)
    animation.add('assets/fireworks.gif', (400, 300), 1000, loop=True)
    animation.add('assets/confetti.gif', (200, 150), 1500, loop=True)

    # Play all animations
    animation.play()

    root.mainloop()
```
