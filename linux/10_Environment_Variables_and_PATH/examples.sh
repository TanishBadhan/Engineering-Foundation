printenv | head
printenv USER
echo "$PATH" | tr ':' '\n'
export DEMO_ENV='linux-foundations'
echo "$DEMO_ENV"
bash -c 'echo "child sees: $DEMO_ENV"'
command -v bash
which bash
alias ll='ls -lah'
ll ~/linux-practice 2>/dev/null || true
