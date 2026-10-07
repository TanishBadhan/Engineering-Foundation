command -v systemctl && systemctl --version | head -n 2 || echo 'systemctl unavailable'
command -v journalctl && journalctl -n 10 --no-pager || echo 'journalctl unavailable'
# systemctl status <service>
# journalctl -u <service> -n 50 --no-pager
