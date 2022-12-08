pyinstaller --noconfirm \
    --onefile \
    --name="EDL-Patcher" \
    --add-data="image.jpg:img" \
    gui.py