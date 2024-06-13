import cloudinary.uploader
from decouple import config


def get_url_from_cloudinary(file, name_file):
    try:
        cloudinary.config(
            cloud_name = config('CLOUDINARY_CLOUD_NAME'),
            api_key = config('CLOUDINARY_API_KEY'),
            api_secret = config('CLOUDINARY_API_SECRET'),
            secure = True
        )

        upload_file = cloudinary.uploader.upload(file, public_id=name_file)

        return upload_file['secure_url']

    except Exception as e:
        print(f'Error al subir la imagen : {str(e)}')
        return None
