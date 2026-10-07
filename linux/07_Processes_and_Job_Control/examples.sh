ps aux | head -n 10
pgrep -a bash
sleep 30 &
PID=$!
echo "PID=$PID"
ps -p "$PID"
kill "$PID"
wait "$PID" 2>/dev/null || true
# Interactive practice: run `sleep 60`, press Ctrl+Z, then use `bg`, `jobs`, `fg`, and Ctrl+C.
