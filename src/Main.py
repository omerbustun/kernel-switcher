import gi
import json

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def load_kernel_versions(filepath="../kernels.json"):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
        return data["kernels"]
    except FileNotFoundError:
        print("Error: The kernels.json file was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: There was an issue decoding the kernels.json file.")
        return []


class KernelSelector(Gtk.Window):
    def __init__(self):
        super().__init__(title="Kernel Selector")
        self.set_border_width(10)

        self.combo = Gtk.ComboBoxText()
        self.combo.connect("changed", self.on_combo_changed)
        self.load_kernels_into_combo()

        layout = Gtk.Box(spacing=6)
        layout.pack_start(self.combo, True, True, 0)
        self.add(layout)

    def load_kernels_into_combo(self):
        kernels = load_kernel_versions()
        for kernel in kernels:
            self.combo.append_text(f"{kernel['version']}")

    def on_combo_changed(self, combo):
        text = combo.get_active_text()
        if text is not None:
            print(f"Selected Kernel: {text}")


if __name__ == "__main__":
    win = KernelSelector()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
