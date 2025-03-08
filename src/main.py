import os
import sys
import shutil
from pathlib import Path

def copy_directory(src, dest):
  # check if source directory exists
  if not os.path.exists(src):
    print(f"Errror: Source directory '{src}' does not exist.")
    return

  # delete destination directory if it exists
  if os.path.exists(dest):
    print(f"Removing existing directory '{dest}'.")
    shutil.rmtress(dest)

  # create destination directory
  print(f"Creating directory '{dest}'.")
  os.makedirs(dest)

  # copy all files and subdirectories
  for item in os.listdir(src):
    src_path = os.path.join(src, item)
    dest_path = os.path.join(dest, item)

    if os.path.isfile(src_path):
      print(f"Copying file: {src_path} -> {dest_path}")
      # copy2 preserves metadata
      shutil.copy2(src_path, dest_path)

    elif os.path.isdir(src_path):
      print(f"Copying directory: {src_path} -> {dest_path}")
      # recursively copy subdirectory
      copy_directory(src_path, dest_path)


def main():
  # define source & destination directories
  current_dir = os.path.dirname(os.path.abspath(__file__))
  static_dir = os.path.join(current_dir, "static")
  public_dir = os.path.join(current_dir, "public")

  # copy static files to public directory
  print("Starting to copy static files...")
  copy_directory(static_dir, public_dir)
  print("Static files copied successfully!!!")


if __name__ == "__main__":
  main()