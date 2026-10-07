df -h
du -sh .
free -h
lsof -p $$ 2>/dev/null | head -n 10 || true
