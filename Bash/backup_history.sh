#!/bin/bash

mkdir -p ${HOME}/.local/share/history_backups/

tar czf ${HOME}/.local/share/history_backups/backup-$(date +%Y%m%d).tgz ${HOME}/.bash*
if [ $? -ge 1 ]; then
	logger "$(date +%Y%m%d) HISTORY_BACKUPS FAILED"
else
	logger "$(date +%Y%m%d) HISTORY_BACKUPS SUCCEDED"
fi
