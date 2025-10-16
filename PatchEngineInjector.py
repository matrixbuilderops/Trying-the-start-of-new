import os
import json

def locate_game_engine_directory(base_path):
    for root, dirs, files in os.walk(base_path):
        for dir in dirs:
            if "EngineCore" in dir or "GameEngine" in dir:
                return os.path.join(root, dir)
    return None

def inject_patch_module(engine_path, patch_code, module_name="PatchModule"):
    target_file = os.path.join(engine_path, f"{module_name}.py")
    with open(target_file, 'w') as f:
        f.write(patch_code)
    return target_file

def create_patch_module(settings):
    return f"""
# Auto-generated PatchModule for Game Engine Compatibility

class PatchModule:
    def __init__(self):
        self.settings = {json.dumps(settings, indent=4)}

    def apply_patch(self, game_env):
        for key, value in self.settings.items():
            if hasattr(game_env, key):
                setattr(game_env, key, value)
        return game_env
"""

def run_patch_injection(base_path, settings):
    engine_dir = locate_game_engine_directory(base_path)
    if not engine_dir:
        raise FileNotFoundError("Game engine directory not found.")
    patch_code = create_patch_module(settings)
    patched_file = inject_patch_module(engine_dir, patch_code)
    return patched_file

# Example usage
if __name__ == "__main__":
    game_base = "./GameBuilder/Runtime"
    patch_settings = {
        "enable_mod_hooks": True,
        "optimize_runtime": True,
        "debug_mode": False
    }
    try:
        result = run_patch_injection(game_base, patch_settings)
        print(f"Patch module injected: {result}")
    except Exception as e:
        print(f"Injection failed: {str(e)}")

