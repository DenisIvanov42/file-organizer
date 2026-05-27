from main import DirectoryOrganizer, FileMover

def test_organizer_moves_files_correctly(tmp_path):
    print(f"\n---> HERE IS THE TEMP PATH: {tmp_path}")

    
    fake_image = tmp_path / "vacation.png"
    fake_doc = tmp_path / "homework.txt"
    fake_unknown = tmp_path / "random.xyz"
    
    fake_image.touch()
    fake_doc.touch()
    fake_unknown.touch()

    test_rules = {
        ".png": "images",
        ".txt": "docs"
    }

    mover = FileMover()
    organizer = DirectoryOrganizer(target_folder=tmp_path, rules=test_rules, mover=mover)
    organizer.organize()

    
    assert (tmp_path / "images" / "vacation.png").exists() == True
    assert (tmp_path / "docs" / "homework.txt").exists() == True
    
    assert fake_image.exists() == False
    assert fake_doc.exists() == False
    
    assert fake_unknown.exists() == True