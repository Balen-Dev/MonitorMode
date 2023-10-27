#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface you want to put in monitor mode")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[AQUA]: Please specify an interface, use --help for more info.")
    return options


def change_mode(interface):
    print("[AQUA]: Putting [" + interface + "] in monitor mode")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["iwconfig", interface, "mode", "monitor"])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mode(options.interface)

output = subprocess.check_output(["iwconfig", options.interface])
if b"Mode:Monitor" in output:
    print("[AQUA]: Successfully put [" + options.interface + "] in monitor mode")
else:
    print("[AQUA]: Failed to put [" + options.interface + "] in monitor mode")