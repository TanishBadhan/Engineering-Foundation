df -h
du -sh ~/linux-practice 2>/dev/null || true
free -h
lsof -p $$ 2>/dev/null | head -n 10 || true
