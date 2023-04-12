set LIB_DIR=%pwd%

if exist .git\hooks\commit-msg del /F .git\hooks\commit-msg
mklink .git\hooks\commit-msg %LIB_DIR%\githooks\commit_message.py

if exist .git\hooks\%LIB_DIR% rmdir /S /Q .git\hooks\%LIB_DIR%
mklink /D .git\hooks\%LIB_DIR% %LIB_DIR%\githooks

echo "Git hooks installed successfully !"