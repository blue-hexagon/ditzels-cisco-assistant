import tkinter
from tkinter import *


class Checkbox():
    boxes = []

    def __init__(self, parent, statusbar, text, statusbar_text, col, row):
        self.var = BooleanVar()
        self.elem = Checkbutton(parent, text=text, var=self.var)
        self.elem.bind("<Enter>", lambda event, text=statusbar_text: statusbar.set_statusbar_text(event, text))
        self.elem.bind("<Leave>", statusbar.clear_statusbar)
        self.elem.grid(column=col, row=row, sticky="w")
        Checkbox.boxes.append(self.elem)

    @staticmethod
    def clear_checkboxes():
        for i in range(0, len(Checkbox.boxes)):
            Checkbox.boxes[i].deselect()

class ConfigPanel:
    def __init__(self, config_panel, statusbar):
        self.config_checkboxes1 = PanedWindow(config_panel)
        self.config_checkboxes1.grid(column=0, row=0, sticky="ns")
        self.config_checkboxes2 = PanedWindow(config_panel)
        self.config_checkboxes2.grid(column=1, row=0, sticky="ns")
        self.config_checkboxes3 = PanedWindow(config_panel)
        self.config_checkboxes3.grid(column=2, row=0, sticky="ns")
        self.config_checkboxes4 = PanedWindow(config_panel)
        self.config_checkboxes4.grid(column=3, row=0, sticky="ns")
        self.config_checkboxes5 = PanedWindow(config_panel)
        self.config_checkboxes5.grid(column=4, row=0, sticky="ns")

        self.running_config = Checkbox(self.config_checkboxes1, statusbar, "Running Configuration", "Retrieve the running configuration", 0, 0)
        self.startup_config = Checkbox(self.config_checkboxes1, statusbar, "Startup Configuration", "Retrieve the startup configuration", 0, 1)
        self.system = Checkbox(self.config_checkboxes1, statusbar, "System", "Retrieve system details", 0, 2)
        self.hardware = Checkbox(self.config_checkboxes1, statusbar, "Hardware", "Retrieve hardware details", 0, 3)
        self.users = Checkbox(self.config_checkboxes1, statusbar, "Users", "Retrieve information about users", 0, 4)
        self.logging = Checkbox(self.config_checkboxes1, statusbar, "Logging", "Retrieve system logs", 0, 5)
        self.tech_support = Checkbox(self.config_checkboxes1, statusbar, "Tech Support",
                                "Retrieve detailed information about the device to be used by tech support", 0, 6)

        self.mac_address_table = Checkbox(self.config_checkboxes2, statusbar, "Mac Table", "Show the MAC table", 0, 0)
        self.arp = Checkbox(self.config_checkboxes2, statusbar, "ARP", "Show details about ARP", 0, 1)
        self.interfaces = Checkbox(self.config_checkboxes2, statusbar, "Interfaces", "Retrieve information about the device interfaces", 0, 2)
        self.routes = Checkbox(self.config_checkboxes2, statusbar, "Routes", "Retrieve details about routes", 0, 3)
        self.protocols = Checkbox(self.config_checkboxes2, statusbar, "Protocols", "Retrieve details about protocols", 0, 4)
        self.spannign_tree = Checkbox(self.config_checkboxes2, statusbar, "Spanning Tree", "Retrieve details about STP", 0, 5)
        self.access_control_lists = Checkbox(self.config_checkboxes2, statusbar, "ACLs", "Retrieve information about access control lists", 0, 6)

        self.dhcp = Checkbox(self.config_checkboxes3, statusbar, "DHCP", "", 0, 0)
        self.vtp = Checkbox(self.config_checkboxes3, statusbar, "VTP", "", 0, 1)
        self.vlan = Checkbox(self.config_checkboxes3, statusbar, "VLAN", "", 0, 2)
        self.etherchannel = Checkbox(self.config_checkboxes3, statusbar, "Etherchannel", "", 0, 3)
        self.cdp = Checkbox(self.config_checkboxes3, statusbar, "CDP", "", 0, 4)
        self.ntp = Checkbox(self.config_checkboxes3, statusbar, "NTP", "", 0, 5)

        # = Checkbox(self.config_checkboxes4, statusbar, "", "", 0, 0)

