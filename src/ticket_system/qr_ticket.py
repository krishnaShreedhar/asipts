"""
sudo apt-get update
sudo apt-get install python-qrtools

pip install pyqrcode pypng zbar pillow
"""

import pyqrcode
import os
import png
from pyqrcode import QRCode
from ticket_system.ticket_generator import TicketGenerator
from core.directory_management.dir_manager import DirectoryManager


def gen_qr_code_ticket(source, destination, **kwargs):
    dirm = kwargs.get("dirm", DirectoryManager())
    obj_ticket = TicketGenerator(source, destination)
    str_ticket = obj_ticket.get_json_ticket()

    # Generate QR code
    url = pyqrcode.create(str_ticket)

    # Create and save the svg file naming "myqr.svg"
    svg_file_path = os.path.join(dirm.get_dir_tickets(), 'first_ticket.svg')
    url.svg(svg_file_path, scale=8)

    # Create and save the png file naming "myqr.png"
    png_file_path = os.path.join(dirm.get_dir_tickets(), 'first_ticket.png')
    url.png(png_file_path, scale=6)


# def read_qr_code_ticket(file_path):
#     from qrtools import QR
#
#     # creates the QR object
#     my_QR = QR(data=[u"geeksforgeeks", u"https://www.geeksforgeeks.org/"],
#                data_type='bookmark')
#
#     # encodes to a QR code
#     my_QR.encode()
#     from qrtools import QR
#     my_QR = QR(filename="home/user/Desktop/qr.png")
#
#     # decodes the QR code and returns True if successful
#     my_QR.decode()
#
#     # prints the data
#     print
#     my_QR.data


def setup():
    return DirectoryManager()


def main():
    source = "Stop1"
    destination = "Stop2"
    gen_qr_code_ticket(source, destination)


if __name__ == '__main__':
    main()
