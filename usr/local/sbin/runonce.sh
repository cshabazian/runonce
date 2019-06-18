#!/bin/sh
RUNONCE="/etc/local/runonce.d"
RANONCE="/etc/local/runonce.d/ran"
DATE=`date +%m-%d-%Y_%H:%M:%S`
for FILE in `ls $RUNONCE`
do
    [ ! -f "$RUNONCE/$FILE" ] && continue
    bash $RUNONCE/$FILE
    mv "$RUNONCE/$FILE" "$RANONCE/$FILE.$DATE"
    logger -t runonce -p local3.info "$RUNONCE/$FILE"
done
