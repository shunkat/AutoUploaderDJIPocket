import os
import subprocess
import argparse

def remove_files_with_extension(dir_path, extension):
    for file in os.listdir(dir_path):
        if file.endswith(extension):
            os.remove(os.path.join(dir_path, file))

def integrate_mp4_files(dir_path, storage_path):
    mp4_files = [f for f in os.listdir(dir_path) if f.endswith('.MP4') and not f.startswith('._')]
    mp4_files.sort()

    if not mp4_files:
        return False

    with open("file_list.txt", "w") as f:
        for mp4_file in mp4_files:
            f.write(f"file '{os.path.join(dir_path, mp4_file)}'\n")

    result = subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "file_list.txt", "-c", "copy", os.path.join(storage_path, "integrated.mp4")])

    os.remove("file_list.txt")

    for mp4_file in mp4_files:
        os.remove(os.path.join(dir_path, mp4_file))

    return result.returncode == 0

def main():
    # これはSDカードの動画が保存されている場所です。もしエラーが出るなら確認してpathを変更してください。
    dir_path = '/Volumes/Untitled/DCIM/101MEDIA'
    # これはまとめた後の動画を置いておく場所です。適当な場所に変更してください。
    storage_path = "/Users/user/hogehoge"

    parser = argparse.ArgumentParser(description="Integrate and upload video.")
    parser.add_argument("title", type=str, help="Title for the uploaded video.")
    args = parser.parse_args()

    remove_files_with_extension(dir_path, '.LRF')

    # 処理が完了したらupload.pyを実行します。もし他の処理を入れたければここに入れてください。
    if integrate_mp4_files(dir_path, storage_path):
        subprocess.run(["python", "upload.py", "--title", args.title])

    print("操作が完了しました。")

if __name__ == "__main__":
    main()