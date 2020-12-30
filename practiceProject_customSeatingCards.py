#! python3
# Create custom seating cards based on the file guests.txt from chapter 15.
# Use the Pillow module to also add the ballons img to the invitation.
# Ensure each card is the same size by adding black rectangle at the edges.

from PIL import Image, ImageDraw, ImageFont, ImageColor

# Open guests.txt and iterate over each guest on the file.
guestFile = open('guests.txt')
balloonsImg = Image.open('balloons.jpg')
for guest in guestFile:
    # Create a blank image for each guest.
    card = Image.new('RGBA', (288, 360), 'white')
    draw = ImageDraw.Draw(card)
    width, height = card.size
    # Add the name to the card.
    draw.text(((120), (height / 2)), str(guest), fill='black')
    card.save(str(guest).strip('\n') + '.png') # save the card with name
    # Add the ballons to the card.
    balloons = card.copy()
    balloonsImg = balloonsImg.resize(((int(width / 5)), int(height / 5)))
    balloons.paste(balloonsImg, (int(width - 70), int(height - 150)))
    # Ensure each card is the same size with black rectangles.
    # Black square on the top part.
    for x in range(288):
        for y in range(int(360/2)):
            balloons.putpixel((x, y), ImageColor.getcolor('black', 'RGBA'))
    # Black square on the bottom part.
    for x in range(288):
        for y in range(285, 360):
            balloons.putpixel((x, y), ImageColor.getcolor('black', 'RGBA'))
    # Save each card.
    balloons.save(str(guest).strip('\n') + '.png') # overwrite the card save
print('Done')
print(balloons.getpixel((0,0)))
