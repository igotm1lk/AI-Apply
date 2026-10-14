import os
import asyncio
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from gridfs import GridFS
from pymongo import MongoClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")

sync_client = MongoClient(MONGODB_URI)
db = sync_client[DB_NAME]
fs = GridFS(db)

def upload_pdf_to_db(pdf_path: str):
    if not os.path.exists(pdf_path):
        print(f"File {pdf_path} does not exist")
        return


    filename = os.path.basename(pdf_path)

    existing = fs.find_one({"filename": filename})
    if existing:
        fs.delete(existing._id)
        print(f"Replacing existing file '{filename}' in the database")

    with open(pdf_path, "rb") as f:
        file_id = fs.put(f, filename=filename, metadata={"user_id": "main_user", "type": "resume"})
    
    print(f"successfully uploaded file '{filename}' to the database")
    print(f"File ID: {file_id}")


    
if __name__ == "__main__":
    pdf_filename = "resume.pdf"
    upload_pdf_to_db(pdf_filename)
    
