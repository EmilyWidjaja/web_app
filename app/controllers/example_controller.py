from loguru import logger
from fastapi import APIRouter, Depends, File, UploadFile
from processing_methods import process_image

example_router = APIRouter()


# @example_router.post("/")
# async def upload_file(file: UploadFile = File(...)):
#     """
#     Upload file and ...
#     """
#     logger.info(f"Received file name = {file.filename}")

#     # TODO

#     return {"file_name": file.filename}


@example_router.get("/api/energy_default")
async def energy_default():
    """ """

    # TODO
    energy, time = process_image(False)

    return {"energy": energy, "time": time}

@example_router.get("/api/energy_efficient")
async def energy_efficient():
    """ """

    # TODO
    energy, time = process_image(True)

    return {"energy": energy, "time": time}