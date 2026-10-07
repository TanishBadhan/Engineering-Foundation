printf 'banana\napple\napple\ncarrot\n' > ~/linux-practice/items.txt
cat -n ~/linux-practice/items.txt
head -n 2 ~/linux-practice/items.txt
tail -n 2 ~/linux-practice/items.txt
wc -l ~/linux-practice/items.txt
sort ~/linux-practice/items.txt | uniq
printf 'banana\napple\n' > ~/linux-practice/a.txt
printf 'banana\ncarrot\n' > ~/linux-practice/b.txt
diff ~/linux-practice/a.txt ~/linux-practice/b.txt
