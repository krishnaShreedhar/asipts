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


def setup():
    return DirectoryManager()


def main():
    source = "Stop1"
    destination = "Stop2"
    gen_qr_code_ticket(source, destination)


if __name__ == '__main__':
    main()
