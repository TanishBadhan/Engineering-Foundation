command -v systemctl && systemctl --version | head -n 2 || echo 'systemctl unavailable'
command -v journalctl && journalctl -n 10 --no-pager || echo 'journalctl unavailable'
# systemctl status ssh
# journalctl -u ssh -n 50 --no-pager
