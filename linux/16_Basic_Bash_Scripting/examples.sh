#!/bin/bash
name='Linux'
echo "Hello, $name"
echo "Script: $0"
echo "First argument: $1"
echo "All arguments: $@"
if [[ -z "$1" ]]; then echo 'No argument supplied'; elif [[ "$1" == 'help' ]]; then echo 'Usage: ./examples.sh <name>'; else echo "Argument received: $1"; fi
case "${1:-unknown}" in help) echo 'Help selected' ;; linux) echo 'Linux selected' ;; *) echo 'Other input' ;; esac
items=('python' 'sql' 'linux')
for item in "${items[@]}"; do echo "Topic: $item"; done
count=1
while [[ $count -le 3 ]]; do echo "count=$count"; ((count++)); done
greet(){ echo "Function says hello to $1"; }
greet "${1:-engineer}"
true; echo "true status=$?"
false; echo "false status=$?"
exit 0
