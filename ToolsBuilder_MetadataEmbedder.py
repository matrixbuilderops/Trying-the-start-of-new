# ToolsBuilder_MetadataEmbedder.py
# Embeds metadata directly into source files at compile-time for traceability and indexing.

import os
import json

class MetadataEmbedder:
    def __init__(self, metadata_path):
        self.metadata_path = metadata_path
        self.metadata = {}

    def load_metadata(self):
        with open(self.metadata_path, 'r') as f:
            self.metadata = json.load(f)

    def embed_into_file(self, target_file):
        with open(target_file, 'r') as f:
            content = f.read()
        header = "# [Metadata]\n" + "\n".join(f"# {k}: {v}" for k, v in self.metadata.items()) + "\n\n"
        with open(target_file, 'w') as f:
            f.write(header + content)
        print(f"[Metadata embedded in {target_file}]")

if __name__ == "__main__":
    embedder = MetadataEmbedder("app_metadata.json")
    embedder.load_metadata()
    embedder.embed_into_file("ToolsBuilder_Final.py")

