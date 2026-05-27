from pathlib import Path


EXTENSION_RULES = {
    ".png": "images",
    ".jpg": "images",
    ".txt": "docs",
    ".pdf": "pdf"
}

class FileMover:
    def move_file(self, file_path, destination_dir):

        destination_dir.mkdir(parents=True, exist_ok=True)
        
        target_path = destination_dir / file_path.name
        file_path.rename(target_path)
        print(f"Moved: {file_path.name} -> {destination_dir.name}/")

class DirectoryOrganizer:
    def __init__(self, target_folder, rules, mover):
        self.target_folder = Path(target_folder)
        self.rules = rules
        self.mover = mover 

    def organize(self):
        if not self.target_folder.exists():
            print("Folder not found!")
            return

        for item in self.target_folder.iterdir():
            if item.is_file():
                ext = item.suffix.lower() 
                
                if ext in self.rules:
                    folder_name = self.rules[ext]
                    dest_dir = self.target_folder / folder_name
                    
                    self.mover.move_file(item, dest_dir)

if __name__ == "__main__":

    my_mover = FileMover()
    
    organizer = DirectoryOrganizer("./database", EXTENSION_RULES, my_mover)
    
    organizer.organize()
