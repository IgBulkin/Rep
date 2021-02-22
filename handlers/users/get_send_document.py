from aiogram import types
from loader import dp
from pathlib import Path


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def download_document(message: types.Message):
    path_to_download = Path().joinpath("items", "categories", "subcategories", "photos")
    path_to_download.mkdir(parents=True, exist_ok=True)
    path_to_download = path_to_download.joinpath(message.document.file_name)

    await message.document.download(destination=path_to_download)
    await message.answer(f"Документ был сохранен в путь: {path_to_download}")

