"""
============================================================
                SMART FILE ORGANIZER
============================================================

Internship Project - Synent Technologies

Developer : Harsh Bhanarkar

Description:
Automatically organizes files into categorized folders.
============================================================
"""

import shutil
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

SOURCE_FOLDER = BASE_DIR / "Test_Files"
DESTINATION_FOLDER = BASE_DIR / "Organized_Files"


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".cpp", ".c", ".java", ".js", ".html", ".css", ".json", ".xml"],
}

summary = {}


def display_header():
    """Display project header."""

    print("\n" + "=" * 60)
    print("               SMART FILE ORGANIZER")
    print("=" * 60)
    print("Automatically organize files by category")
    print("=" * 60)


def create_folders():
    """Create destination folders automatically."""

    DESTINATION_FOLDER.mkdir(exist_ok=True)

    for category in FILE_TYPES.keys():
        (DESTINATION_FOLDER / category).mkdir(exist_ok=True)

    (DESTINATION_FOLDER / "Others").mkdir(exist_ok=True)


def get_category(extension):
    """Return folder name based on extension."""

    extension = extension.lower()

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_filename(destination_folder, filename):
    """Prevent duplicate file names."""

    destination = destination_folder / filename

    if not destination.exists():
        return filename

    name = destination.stem
    extension = destination.suffix

    counter = 1

    while True:
        new_name = f"{name}_{counter}{extension}"

        if not (destination_folder / new_name).exists():
            return new_name

        counter += 1


def organize_files():
    """Move files into categorized folders."""

    if not SOURCE_FOLDER.exists():
        print(f"\nError: '{SOURCE_FOLDER.name}' folder not found.")
        return

    files = list(SOURCE_FOLDER.iterdir())

    if not files:
        print("\nNo files found in Test_Files.")
        return

    total_files = 0

    for file in files:

        if file.is_dir():
            continue

        category = get_category(file.suffix)

        destination_folder = DESTINATION_FOLDER / category

        new_filename = get_unique_filename(destination_folder, file.name)

        destination_path = destination_folder / new_filename

        shutil.move(str(file), str(destination_path))

        summary[category] = summary.get(category, 0) + 1

        total_files += 1

    print("\n" + "=" * 60)
    print("          FILE ORGANIZATION COMPLETED")
    print("=" * 60)

    for category in sorted(summary.keys()):
        print(f"{category:<15}: {summary[category]} file(s)")

    print("-" * 60)
    print(f"Total Files Moved : {total_files}")
    print("=" * 60)


def main():
    display_header()
    create_folders()
    organize_files()


if __name__ == "__main__":
    main()