printf 'one\ntwo\nthree\n' > ~/linux-practice-output.txt
cat ~/linux-practice-output.txt | wc -l
printf 'four\n' >> ~/linux-practice-output.txt
ls /does-not-exist 2> ~/linux-error.txt
cat ~/linux-error.txt
true; echo "status=$?"
false; echo "status=$?"
true && echo success
false || echo fallback
sleep 2 &
echo "background PID=$!"
rm -f ~/linux-practice-output.txt ~/linux-error.txt
