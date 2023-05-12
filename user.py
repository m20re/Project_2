from randomuser import RandomUser
from PIL import Image
import requests, io

def generate_user_info()-> list:
    user = RandomUser()
    return user.get_full_name(), user.get_gender(), user.get_email()

    
