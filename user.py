from randomuser import RandomUser
from PIL import Image
import requests, io, secrets, string, csv

def generate_user_info() -> list:
    """
    creates a user from Random User API
    :return: returns the following: full name, gender
     email, phone, username, password, picture
    """
    user = RandomUser()
    return [user.get_full_name(), user.get_gender(), user.get_email(), user.get_phone(), user.get_username(), user.get_password(), user.get_picture()]

    
def get_image_bytes(image_url: str) -> io:
    """
    gets a image url from RandomUser, sets the thumbnail to 500, 500
     convert the file into byte so it can be saved in the memory
    :return: bio.getvalue()
     """
    im = Image.open(requests.get(url=image_url, stream=True).raw)
    im.thumbnail((500,500))
    bio = io.BytesIO()
    im.save(bio, format="PNG")
    return bio.getvalue()

def generate_new_password() -> string:
    """
    generates a new password by using secrets and string module
    :return: 8 digit password
    """
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(8))
    return password

def generate_new_name(data: list) -> str:
    user = RandomUser()
    return user.get_full_name()

def write_header_csv(file: str) -> None:
    with open(file, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['full name', 'gender', 'email', 'phone', 'username', 'password', 'image_url'])
    return

def write_user_row_csv(data: list, file: str):
    with open(file, "a", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        while True:
            try:
                csv_writer.writerow(data)
                break
            except UnicodeEncodeError:
                data[0] = generate_new_name(data)
    return

