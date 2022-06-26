#/bin/bash
WORKING_DIR=$(pwd)
CONFIG=$WORKING_DIR/config.py
if ! [ -f "$CONFIG" ]; then
	cp $WORKING_DIR/default_config.py $CONFIG
fi
sudo python3 multi_instance.py
