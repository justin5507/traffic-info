@echo off
echo 正在初始化 Git 儲存庫...
git init
git add dev.html
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/justin5507/traffic-info.git
git push -u origin main
echo 完成！
pause 