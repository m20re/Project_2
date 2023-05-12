from randomuser import RandomUser
from PIL import Image
import requests, io

def generate_user_info()-> list:
    user = RandomUser()
    return user.get_full_name(), user.get_gender(), user.get_email(), user.get_picture()

    
def get_image_bytes(image_url) -> io:
    im = Image.open(requests.get(url=image_url, stream=True).raw)
    im.thumbnail((500,500))
    bio = io.BytesIO()
    im.save(bio, format="PNG")
    return bio.getvalue()