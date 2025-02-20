from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string

def generate_captcha_text(length=4):
    """Генерирует случайный текст из заданного количества символов (A-Z и 0-9)."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def draw_random_lines(draw,
                      width, 
                      height, 
                      line_count=3, 
                      line_color="black", 
                      line_width=2):
    """Рисует случайные линии на изображении."""
    for _ in range(line_count):
        start_point = (random.randint(0, width), random.randint(0, height))
        end_point = (random.randint(0, width), random.randint(0, height))
        draw.line([start_point, end_point], fill=line_color, width=line_width)

def add_random_noise(draw, 
                     width, 
                     height, 
                     noise_count=3, 
                     noise_color="black"):
    """Добавляет случайные точки шума на изображении."""
    for _ in range(noise_count):
        noise_x = random.randint(0, width)
        noise_y = random.randint(0, height)
        draw.point((noise_x, noise_y), fill=noise_color)

def place_rotated_text(image, 
                       text,
                       font,
                       width,
                       height,
                       rotation_range=(-30, 30), 
                       min_y_offset=5):
    """Размещает повёрнутый текст на изображении."""
    symbol_spacing = width // (len(text) + 1)
    max_y_offset = height // 3

    for i, char in enumerate(text):
        # Координаты символа
        x = symbol_spacing * (i + 1)
        y = random.randint(min_y_offset, height - max_y_offset)
        
        # Создать временное изображение для одного символа
        temp_image = Image.new('RGBA', (50, 50), (255, 255, 255, 0))
        temp_draw = ImageDraw.Draw(temp_image)
        temp_draw.text((5, 5), char, font=font, fill='black')
        
        # Повернуть символ на случайный угол
        angle = random.randint(*rotation_range)
        temp_image = temp_image.rotate(angle, expand=True)
        
        # Разместить символ на основном изображении
        image.paste(temp_image, (x, y), temp_image)

def create_captcha(text,
                   width=300,
                   height=100, 
                   font_path="arial.ttf",
                   font_size=42):
    """Генерирует изображение капчи с заданным текстом."""
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    place_rotated_text(draw, image, text, font, width, height)
    draw_random_lines(draw, width, height)
    add_random_noise(draw, width, height)
    image = image.filter(ImageFilter.SMOOTH)
    
    return image

if __name__ == "__main__":
    captcha_text = generate_captcha_text()
    print("Сгенерированный текст капчи:", captcha_text)
    
    captcha_image = create_captcha(captcha_text)
    captcha_image.save("captcha.png")
    captcha_image.show()
