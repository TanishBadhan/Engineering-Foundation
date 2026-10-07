printenv USER
echo "$PATH" | tr ':' '\n'
export DEMO_ENV='engineering-foundation'
echo "$DEMO_ENV"
bash -c 'echo "child sees: $DEMO_ENV"'
command -v bash
which bash
alias ll='ls -lah'
ll .
