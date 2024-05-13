import os
import gi
import json

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Adw

def load_kernel_versions():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    json_path = os.path.join(dir_path, "../kernels.json")
    try:
        with open(json_path, "r") as file:
            data = json.load(file)
        return data["kernels"]
    except FileNotFoundError:
        print("Error: The kernels.json file was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: There was an issue decoding the kernels.json file.")
        return []

class KernelSelector(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Kernel Selector")
        self.set_default_size(400, 100)
        self.set_border_width(10)

        self.combo = Gtk.ComboBoxText()
        self.combo.connect("changed", self.on_combo_changed)
        self.load_kernels_into_combo()

        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        layout.append(self.combo)
        self.set_child(layout)

    def load_kernels_into_combo(self):
        kernels = load_kernel_versions()
        for kernel in kernels:
            self.combo.append_text(f"{kernel['version']}")

    def on_combo_changed(self, combo):
        text = combo.get_active_text()
        if text is not None:
            print(f"Selected Kernel: {text}")

class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__()

    def do_activate(self):
        win = KernelSelector(self)
        win.show()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApp()
app.run()
