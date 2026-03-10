import os
import requests
from tqdm import tqdm

def download_file(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    filename = url.split('/')[-1]
    file_path = os.path.join(dest_folder, filename)
    
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(file_path, 'wb') as f, tqdm(
        desc=filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = f.write(data)
            bar.update(size)

# Target dataset path
base_path = ""

urls = [
    "http://images.cocodataset.org/zips/train2017.zip",
    "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
]

for url in urls:
    download_file(url, base_path)