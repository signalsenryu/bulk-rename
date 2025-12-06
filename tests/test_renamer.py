from src.renamer import generate_new_name


def test_generate_new_name_basic():
    """Test basic filename generation with zero-padded numbering."""
    result = generate_new_name("ASMR_{:03d}", 1, "mp4")
    assert result == "ASMR_001.mp4"


def test_generate_new_name_double_digit():
    """Test filename generation with two-digit zero padding."""
    result = generate_new_name("video_{:02d}", 25, "mkv")
    assert result == "video_25.mkv"


def test_generate_new_name_starting_from_zero():
    """Test filename generation starting from index 0."""
    result = generate_new_name("file_{:03d}", 0, "txt")
    assert result == "file_000.txt"


def test_generate_new_name_large_number():
    """Test filename generation with number exceeding padding width."""
    result = generate_new_name("track_{:02d}", 999, "mp3")
    assert result == "track_999.mp3"
