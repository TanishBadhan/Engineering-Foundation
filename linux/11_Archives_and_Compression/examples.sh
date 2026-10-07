mkdir -p ~/linux-practice/archive/source
printf 'alpha\nbeta\ngamma\n' > ~/linux-practice/archive/source/data.txt
printf 'log entry\n' > ~/linux-practice/archive/source/app.log
cd ~/linux-practice/archive
tar -cf bundle.tar source
tar -tf bundle.tar
tar -czf bundle.tar.gz source
mkdir -p extracted
tar -xzf bundle.tar.gz -C extracted
ls -R extracted
gzip -c source/data.txt > data.txt.gz
gunzip -c data.txt.gz
