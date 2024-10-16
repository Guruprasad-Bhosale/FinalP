import os
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Define paths
image_base_path = image_base_path = 'C:\\Users\\shivani\\Desktop\\plant\\plantdata\\aloevera'
  # e.g., plantdata/
csv_file_path = 'C:\\Users\\shivani\\Desktop\\plant\\plants_dataset.csv'

# Load CSV file
plant_info_df = pd.read_csv(csv_file_path)

# Function to get image paths for each plant
def get_image_paths():
    plant_images = {}
    for plant_name in os.listdir(image_base_path):
        plant_dir = os.path.join(image_base_path, plant_name)
        if os.path.isdir(plant_dir):
            images = [f"{plant_dir}/{img}" for img in os.listdir(plant_dir) if img.endswith(('jpg', 'png'))]
            plant_images[plant_name] = images
    return plant_images

@app.route('/plants', methods=['GET'])
def get_plants():
    plant_images = get_image_paths()
    plants_with_info = []
    
    for index, row in plant_info_df.iterrows():
        plant_name = row['name'].lower()
        plant_data = {
            'name': row['name'],
            'description': row['description'],
            'images': plant_images.get(plant_name, [])
        }
        plants_with_info.append(plant_data)

    return jsonify(plants_with_info)

if __name__ == '__main__':
    app.run(debug=True)
