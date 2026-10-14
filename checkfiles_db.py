import os
from dotenv import load_dotenv
from pymongo import MongoClient
from gridfs import GridFS

load_dotenv()
client = MongoClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("DB_NAME")]
fs = GridFS(db)

print("Files in the database:")
for grid_file in fs.find():
    print(f" - Filename:{grid_file.filename}")
    print(f" - Size: {grid_file.length} bytes")
    print(f" - Upload Date: {grid_file.upload_date}")
 