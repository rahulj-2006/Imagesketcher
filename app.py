import customtkinter as ctk
from tkinter import filedialog, messagebox
from sketchpy import canvas
import turtle  # Added to control the drawing screen

class ImageSketcherApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Configuration ---
        self.title("Image to Sketch Converter")
        self.geometry("500x300")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.selected_image_path = None

        # --- Main Frame for all widgets ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # --- Title ---
        self.title_label = ctk.CTkLabel(self.main_frame, text="Image Sketcher 🎨", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(10, 20))

        # --- Select Image Button ---
        self.select_button = ctk.CTkButton(self.main_frame, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=10, padx=40, fill="x")

        # --- Label to show the selected file path ---
        self.file_label = ctk.CTkLabel(self.main_frame, text="No image selected", text_color="gray")
        self.file_label.pack(pady=5)

        # --- Generate Sketch Button ---
        self.generate_button = ctk.CTkButton(
            self.main_frame,
            text="Generate Sketch",
            command=self.generate_sketch,
            state="disabled"  # Disabled until an image is selected
        )
        self.generate_button.pack(pady=20, padx=40, fill="x")

    def select_image(self):
        """Opens a file dialog to let the user select an image."""
        file_path = filedialog.askopenfilename(
            title="Select an Image File",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
        )
        
        if file_path:
            self.selected_image_path = file_path
            display_path = "..." + file_path[-35:] if len(file_path) > 35 else file_path
            self.file_label.configure(text=display_path, text_color="white")
            self.generate_button.configure(state="normal")
        else:
            self.file_label.configure(text="No image selected", text_color="gray")
            self.generate_button.configure(state="disabled")

    def generate_sketch(self):
        """Generates and displays the sketch, clearing the screen first."""
        if not self.selected_image_path:
            messagebox.showerror("Error", "Please select an image first!")
            return

        try:
            messagebox.showinfo(
                "Processing", 
                "Sketch generation has started.\nA new window will open to draw the sketch. Please wait."
            )
            
            # This line clears the previous drawing before starting a new one.
            turtle.clearscreen()
            
            # Create and draw the new sketch on the clean screen
            sketch = canvas.sketch_from_image(self.selected_image_path)
            sketch.draw()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# --- Run the Application ---
if __name__ == "__main__":
    app = ImageSketcherApp()
    app.mainloop()