mkdir -p ~/linux-archive-practice/source ~/linux-archive-practice/extracted
printf 'alpha\nbeta\ngamma\n' > ~/linux-archive-practice/source/data.txt
printf 'log entry\n' > ~/linux-archive-practice/source/app.log
cd ~/linux-archive-practice
tar -cf bundle.tar source
tar -tf bundle.tar
tar -czf bundle.tar.gz source
tar -xzf bundle.tar.gz -C extracted
gzip -c source/data.txt > data.txt.gz
gunzip -c data.txt.gz
