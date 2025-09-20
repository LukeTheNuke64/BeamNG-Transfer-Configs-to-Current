import os
import shutil

appdata = os.environ["LOCALAPPDATA"]
src = os.path.join(appdata, "BeamNG.drive", "0.36", "vehicles")
dst = os.path.join(appdata, "BeamNG", "BeamNG.drive", "current", "vehicles")

def copy(src_root, dst_root):
    if not os.path.exists(src_root):
        print(f"Source folder not found: {src_root}")
        return
    os.makedirs(dst_root, exist_ok=True)
    for vehicle in os.listdir(src_root):
        src = os.path.join(src_root, vehicle)
        dst = os.path.join(dst_root, vehicle)
        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
            print(f"moved: {vehicle}")
        else:
            continue
    print("\nfiles moved successfully!")

if __name__ == "__main__":
    copy(src, dst)
