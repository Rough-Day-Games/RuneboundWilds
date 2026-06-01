import os
import zipfile
import shutil

# If needed, this is where you can set the working directory
directory = os.getcwd()
temp_extract_path = os.path.join(directory, "temp_extract")

# Ensure temp directory is clean
if os.path.exists(temp_extract_path):
    shutil.rmtree(temp_extract_path)
os.makedirs(temp_extract_path, exist_ok=True)


def extract(folder_name_filter):
    for filename in os.listdir(directory):
        if filename.endswith(".jar"):
            jar_path = os.path.join(directory, filename)
            print(f"- Extracting {folder_name_filter}: {filename}")
            with zipfile.ZipFile(jar_path, 'r') as jar:
                for member in jar.namelist():
                    if member.startswith(f"{folder_name_filter}/") and not member.endswith("/"):
                        jar.extract(member, temp_extract_path)


print("Working...")
extract("data")
print("Finished extracting data. Moving over to assets...")
extract("assets")
input("Done!")
