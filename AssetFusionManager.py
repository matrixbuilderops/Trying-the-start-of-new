import os
import hashlib
import json

ASSET_ROOT = "GameAssets/"
MANIFEST_FILE = "GameAssets/manifest.qtlmeta"
FUSION_OUTPUT = "GameAssets/FusedAssets.qtlpack"

def hash_file(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def walk_assets():
    assets = {}
    for root, dirs, files in os.walk(ASSET_ROOT):
        for file in files:
            full_path = os.path.join(root, file)
            asset_key = os.path.relpath(full_path, ASSET_ROOT)
            assets[asset_key] = {
                "hash": hash_file(full_path),
                "path": full_path,
                "extension": os.path.splitext(file)[1]
            }
    return assets

def generate_manifest(assets):
    with open(MANIFEST_FILE, 'w') as f:
        json.dump(assets, f, indent=2)
    print(f"📄 Manifest generated at {MANIFEST_FILE}")

def fuse_assets(assets):
    with open(FUSION_OUTPUT, 'w') as f:
        for asset in assets.values():
            f.write(f"# Fused: {asset['path']} [hash: {asset['hash']}]\n")
    print(f"🎮 Assets fused into {FUSION_OUTPUT}")

def execute_asset_fusion():
    print("🔄 Fusing all game assets...")
    assets = walk_assets()
    generate_manifest(assets)
    fuse_assets(assets)
    print("✅ Fusion complete.")

if __name__ == "__main__":
    execute_asset_fusion()

