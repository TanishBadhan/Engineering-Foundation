mkdir -p ~/linux-practice/files/subdir
cd ~/linux-practice/files
touch one.txt
cp one.txt copy.txt
mv copy.txt renamed.txt
ln -s one.txt one-link.txt
ls -lah
rm renamed.txt
rmdir subdir
