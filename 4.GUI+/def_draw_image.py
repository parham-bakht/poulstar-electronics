def draw_image(image, width, height):
    for y in range(height):
        for x in range(width):
            byte_index = (x + (y // 8) * width) % len(image)
            bit = (image[byte_index] >> (y % 8)) & 1
            oled.pixel(x, y, bit)
            