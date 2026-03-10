import json

# 把这里换成你本地 json 文件的实际路径
json_file = r"C:\Users\10920\Desktop\comp\comp4471\project\coco\annotations_trainval2017\annotations\captions_val2017.json"

print("正在加载 JSON 文件，请稍等...")
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 提取前 3 张图片的 ID
sample_images = data['images'][:3]

print("\n--- 开始匹配图文 ---")
for img in sample_images:
    img_id = img['id']
    file_name = img['file_name']
    
    # 在 annotations 里找出所有对应这个 img_id 的描述
    captions = [ann['caption'] for ann in data['annotations'] if ann['image_id'] == img_id]
    
    print(f"\n图片名: {file_name} (ID: {img_id})")
    print("对应的 5 条描述是:")
    for i, cap in enumerate(captions):
        print(f"  {i+1}. {cap}")