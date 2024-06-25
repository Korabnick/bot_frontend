#!/usr/bin/env bash

if [[ $WEBHOOK_URL != "" ]];
  then
    exec uvicorn core:create_app --host=$BIND_IP --port=$BIND_PORT
  else
    exec python core/tg_bot.py
fi;