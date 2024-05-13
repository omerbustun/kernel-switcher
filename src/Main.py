import os
import gi
import json

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

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

class KernelSelector(Gtk.Window):
    def __init__(self):
        super().__init__(title="Kernel Selector")
        self.set_border_width(10)
        self.set_default_size(400, 200)
        
        self.set_resizable(False)
        
        self.load_css()

        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        layout.get_style_context().add_class("window")
        self.add(layout)

        header = Gtk.Label(label="Select a kernel version")
        header.get_style_context().add_class("header-label")
        layout.pack_start(header, False, False, 0)

        self.combo = Gtk.ComboBoxText()
        self.combo.connect("changed", self.on_combo_changed)
        self.load_kernels_into_combo()
        self.combo.get_style_context().add_class("combobox")
        layout.pack_start(self.combo, False, False, 0)

        button_box = Gtk.Box(spacing=10)
        button_box.get_style_context().add_class("button-box")

        self.download_button = Gtk.Button(label="Download")
        self.download_button.connect("clicked", self.on_download_clicked)
        self.download_button.get_style_context().add_class("button")
        button_box.pack_start(self.download_button, True, True, 0)

        self.install_button = Gtk.Button(label="Compile & Install")
        self.install_button.connect("clicked", self.on_install_clicked)
        self.install_button.get_style_context().add_class("button")
        button_box.pack_start(self.install_button, True, True, 0)

        layout.pack_start(button_box, False, False, 0)

    def load_kernels_into_combo(self):
        kernels = load_kernel_versions()
        for kernel in kernels:
            self.combo.append_text(f"{kernel['version']}")

    def on_combo_changed(self, combo):
        text = combo.get_active_text()
        if text is not None:
            print(f"Selected Kernel: {text}")

    def on_download_clicked(self, button):
        selected_kernel = self.combo.get_active_text()
        if selected_kernel:
            print(f"Downloading Kernel: {selected_kernel}")
            # Implement download logic here

    def on_install_clicked(self, button):
        selected_kernel = self.combo.get_active_text()
        if selected_kernel:
            print(f"Compiling and Installing Kernel: {selected_kernel}")
            # Implement compile and install logic here

    def load_css(self):
        css_provider = Gtk.CssProvider()
        css_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../css/style.css")

        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

if __name__ == "__main__":
    win = KernelSelector()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
