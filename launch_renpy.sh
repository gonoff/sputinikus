#!/bin/bash
# Launch Ren'Py with JDK in PATH for Android builds

export JAVA_HOME="/home/deck/Documents/sputinikus/jdk-17.0.13+11"
export PATH="$JAVA_HOME/bin:$PATH"

echo "Using Java: $(java -version 2>&1 | head -1)"
echo ""

/home/deck/Documents/sputinikus/renpy-8.3.4-sdk/renpy.sh "$@"
