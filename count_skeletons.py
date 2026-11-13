import zipfile
import json
from collections import Counter

# 1. Đếm person theo nhóm
zp = zipfile.ZipFile('src/exports/PhamDucManh_persons.zip')
dp = json.loads(zp.read('annotations/person_keypoints_default.json'))
pool = json.load(open('src/lab/pool.json', encoding='utf-8'))

by_group = {p['file']: p['group'] for p in pool['persons']}
imgs = {i['id']: i['file_name'] for i in dp['images']}

counts = Counter(by_group[imgs[a['image_id']]] for a in dp['annotations'])

# 2. Đếm face
zf = zipfile.ZipFile('src/exports/PhamDucManh_faces.zip')
df = json.loads(zf.read('annotations/person_keypoints_default.json'))

print("=" * 45)
print(" SỐ LƯỢNG SKELETON ĐÃ GÁN (THEO TỪNG NHÓM)")
print("=" * 45)
for g in ['easy', 'occluded', 'back', 'small', 'crowd']:
    print(f"  Nhóm {g:10s} : {counts[g]} skeleton")
print(f"  Nhóm {'faces':10s} : {len(df['annotations'])} skeleton")
print("-" * 45)
print(f"  Tổng cộng person: {len(dp['annotations'])} skeleton (trong {len(dp['images'])} ảnh)")
print(f"  Tổng cộng faces : {len(df['annotations'])} skeleton (trong {len(df['images'])} ảnh)")
print("=" * 45)

