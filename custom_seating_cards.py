#! python3
# custom_seating_cards.py — An exercise in using Pillow to manipulate images.
# For more information, see project_details.txt.

import logging
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.DEBUG)  # Note out to enable logging.

GUESTS_FILE = "guests.txt"


def get_guest_list():
    """Create properly formatted guest list from text file containing one name per line."""
    with open(GUESTS_FILE, "r", encoding="utf-8") as f_name:
        guests = f_name.readlines()
        guest_list = [guest.strip() for guest in guests]
    return guest_list


def create_card(guests):
    """Create card featuring black border, picture of flowers at top and guest name at bottom."""
    for guest in guests:
        card_width, card_height = 288, 360
        card_img = Image.new("RGBA", (card_width, card_height), "white")

        draw = ImageDraw.Draw(card_img)
        draw.rectangle((0, 0, card_width - 1, card_height - 1), outline="black")

        pd_flowers = "public_domain_flowers.png"
        flower_img = Image.open(pd_flowers)
        flower_width, _ = flower_img.size
        flower_center = int((card_width / 2) - (flower_width / 2))
        card_img.paste(flower_img, (flower_center, 30))

        font_path = "/Users/josh/Fonts/Anton/Anton-Regular.ttf"
        font_size = 45
        anton_font = ImageFont.truetype(font_path, font_size)
        font_width = anton_font.getlength(guest)
        center_point = int((card_width / 2) - (font_width / 2))
        draw.text((center_point, 280), guest, fill="black", font=anton_font)

        card_img.save(f"{guest}_card.png")


create_card(get_guest_list())
