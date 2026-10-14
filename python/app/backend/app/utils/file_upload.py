from pathlib import Path
from typing import Optional
from uuid import uuid4

from fastapi import UploadFile

from app.core.config import settings
from app.core.exceptions import AppError

ALLOWED_TYPES = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp"}


def _valid_signature(content_type: str, data: bytes) -> bool:
    if content_type == "image/jpeg":
        return data.startswith(b"\xff\xd8\xff")
    if content_type == "image/png":
        return data.startswith(b"\x89PNG\r\n\x1a\n")
    if content_type == "image/webp":
        return data[:4] == b"RIFF" and data[8:12] == b"WEBP"
    return False


async def save_photo(file: UploadFile) -> str:
    if file.content_type not in ALLOWED_TYPES:
        raise AppError("Only JPEG, PNG or WEBP images are allowed", 415)

    max_bytes = settings.MAX_UPLOAD_MB * 1024 * 1024
    data = await file.read(max_bytes + 1)
    if len(data) > max_bytes:
        raise AppError(f"File too large (max {settings.MAX_UPLOAD_MB} MB)", 413)
    if not _valid_signature(file.content_type, data):
        raise AppError("File content does not match its type", 400)

    folder = Path(settings.UPLOAD_DIR)
    folder.mkdir(parents=True, exist_ok=True)
    filename = f"{uuid4().hex}{ALLOWED_TYPES[file.content_type]}"
    (folder / filename).write_bytes(data)
    return f"/uploads/{filename}"


def delete_photo(photo_url: Optional[str]) -> None:
    if photo_url:
        (Path(settings.UPLOAD_DIR) / Path(photo_url).name).unlink(missing_ok=True)

        """1. Imports
- Path: Works with file and folder paths.
- Optional: Indicates that a value can be a particular type or None.
- uuid4: Generates a unique identifier to create filenames that are unlikely to collide.
- UploadFile: FastAPI's object for receiving uploaded files.
- settings: Contains application configuration, such as the upload folder and maximum file size.
- AppError: Used to raise application-specific errors with HTTP status codes.
2. Allowed image types
The application allows three image formats: JPEG, PNG, and WEBP.
The mapping connects each MIME content type to its corresponding file extension. This helps the application determine which extension to use when saving an image.
3. Validate the image signature
This function checks the actual bytes at the beginning of the uploaded file.
- JPEG files have a specific byte signature.
- PNG files have their own identifying signature.
- WEBP files are identified using the RIFF marker and the WEBP marker.
Why is this important? A user might rename a text file to .jpg or claim that a file is an image. Checking the signature helps detect files whose contents do not match their declared type.
However, signature validation alone does not guarantee that a file is a safe or fully valid image.
4. Save the photo
This is the main upload function. It performs several steps.
Step 1: Check the content type
It checks whether the uploaded file declares itself as JPEG, PNG, or WEBP. If not, the application raises 415 Unsupported Media Type.
Step 2: Check the file size
The maximum allowed size comes from the application settings.
The configured size in megabytes is converted into bytes. The function reads at most one byte more than the allowed limit.
For example, if the maximum is 5 MB, it reads up to 5 MB plus one byte. If the result exceeds the limit, it raises 413 Content Too Large.
Reading one extra byte helps detect an oversized file without loading the entire file into memory.
Step 3: Validate the file contents
The function compares the file's signature with its declared content type. If they do not match, it raises 400 Bad Request.
Step 4: Prepare the upload folder
It creates the upload directory if it does not already exist. If the folder already exists, the operation does not fail.
Step 5: Generate a unique filename
It generates a random UUID-based filename and attaches the appropriate image extension.
This avoids using the original filename, which could contain unwanted or conflicting names.
Step 6: Write the image to disk
It saves the validated image bytes inside the configured upload folder.
Step 7: Return the photo URL
It returns a relative URL pointing to the uploaded image. The application can store this URL in the user's database record and use it to display the photo later, provided the /uploads route is configured to serve the files.
5. Delete the photo
This function removes a previously saved photo.
- If the supplied photo URL is None or empty, it does nothing.
- It extracts the filename from the URL rather than using the entire URL as a filesystem path.
- It combines the filename with the configured upload directory.
- It deletes the corresponding file.
- If the file does not exist, deletion does not raise an error because missing files are allowed.
Important security considerations
- The upload size should also be limited at the request or reverse-proxy level when appropriate.
- Image signatures are a basic check, not a complete image decoder or malware scanner.
- The upload directory should be configured so that uploaded files cannot execute as server-side code.
- Deletion should verify that the photo belongs to the authenticated user before removing it.
- The returned /uploads/... URL works only if the application or web server serves that directory."""
