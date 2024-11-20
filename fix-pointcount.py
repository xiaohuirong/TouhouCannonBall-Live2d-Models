import os
import json

def modify_json_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            data['Meta']['TotalPointCount'] += data['Meta']['CurveCount'] - 1
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Updated: {filename}")

for item in os.listdir('.'):
    item_path = os.path.join('.', item)
    if os.path.isdir(item_path) and not item.startswith('.'):
        item_path+="/motions"
        print(f'{item_path}')
        modify_json_files(item_path)
