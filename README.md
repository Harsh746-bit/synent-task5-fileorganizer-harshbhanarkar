# Smart File Organizer

A Python-based Command-Line Interface (CLI) application that automatically organizes files into categorized folders based on their file extensions.

## Features

- Automatically organizes files by category
- Supports:
  - Images
  - Documents
  - Videos
  - Audio
  - Archives
  - Code Files
  - Others
- Creates folders automatically
- Prevents duplicate filenames
- Displays organization summary
- Simple CLI interface

## Technologies Used

- Python 3
- os
- shutil
- pathlib

## Folder Structure

```
.
├── Test_Files/
├── Organized_Files/
├── organizer.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Categories Supported

| Category | Extensions |
|----------|------------|
| Images | jpg, jpeg, png, gif, bmp, webp |
| Documents | pdf, doc, docx, txt, ppt, pptx, xls, xlsx |
| Videos | mp4, mkv, avi, mov, webm |
| Audio | mp3, wav, aac, flac |
| Archives | zip, rar, 7z, tar |
| Code | py, cpp, c, java, js, html, css, json, xml |

## How to Run

1. Clone the repository

```bash
git clone https://github.com/Harsh746-bit/synent-task5-fileorganizer-harshbhanarkar.git
```

2. Open the project folder

```bash
cd synent-task5-fileorganizer-harshbhanarkar
```

3. Place sample files inside the **Test_Files** folder.

4. Run

```bash
python organizer.py
```

5. Organized files will be available inside the **Organized_Files** folder.

## Sample Output

```
========================================
FILE ORGANIZATION COMPLETED
========================================

Images      : 2
Documents   : 3
Videos      : 1
Audio       : 1
Archives    : 1
Code        : 3

Total Files Moved : 11
```

## Project Demo

### Before Running

![Before](assets/before.png)

### After Running

![After](assets/after.png)

## Internship

Developed as part of the **Synent Technologies Python Development Internship Program**.

## Developer

**Harsh Bhanarkar**
