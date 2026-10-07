mkdir -p ~/linux-practice/search
printf 'INFO started\nERROR database failed\nINFO complete\n' > ~/linux-practice/search/app.log
printf 'alice 80\nbob 120\ncarol 95\n' > ~/linux-practice/search/data.txt
find ~/linux-practice/search -type f -name '*.txt'
grep -i 'error' ~/linux-practice/search/app.log
sed 's/error/ERROR/g' ~/linux-practice/search/app.log
awk '{print $1}' ~/linux-practice/search/data.txt
awk '$2 > 100 {print $1, $2}' ~/linux-practice/search/data.txt
find ~/linux-practice/search -type f -name '*.log' -print0 | xargs -0 grep -l ERROR
