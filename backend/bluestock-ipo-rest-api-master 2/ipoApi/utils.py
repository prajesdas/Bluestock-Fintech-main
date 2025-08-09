import requests
from django.core.files.base import ContentFile

def save_image_from_url(image_url, instance, field_name):
    try:
        if "drive.google.com" in image_url:
            file_id = image_url.split('/d/')[1].split('/')[0]
            image_url = f"https://drive.google.com/uc?export=download&id={file_id}"

        response = requests.get(image_url)
        if response.status_code == 200:
            file_name = image_url.split("/")[-1]
            file_content = ContentFile(response.content, file_name)
            field = getattr(instance, field_name)
            field.save(file_name, file_content)
            return field
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image: {e}")
    return None
