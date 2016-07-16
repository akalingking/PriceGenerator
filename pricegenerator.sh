#! /bin/bash
BIN_FILE="pricegeneratord.py"
BIN_PATH="."

case "$1" in
  start)
    echo "Starting server"
    # Start the daemon
    python $BIN_PATH/$BIN_FILE -s
    ;;
  stop)
    echo "Stopping server"
    # Stop the daemon
    python $BIN_PATH/$BIN_FILE -k
    ;;
  restart)
    echo "Restarting server"
    python $BIN_PATH/$BIN_FILE -r
    ;;
  *)
    # Refuse to do other stuff
    echo "Usage: $BIN_PATH/$BIN_FILE {start|stop|restart}"
    exit 1
    ;;
esac

exit 0
