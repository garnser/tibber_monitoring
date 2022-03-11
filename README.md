# Tibber realtime monitoring

Run `docker-compose up -d` to start grafana and influx.

Log into influx and define a org, bucket and create a read/write token.

Update py-scripts with:

```
bucket = "" # influx bucket
org = "" # influx org
token = "" # influx token
url="http://localhost:8086"
ACCESS_TOKEN="" # Tibber API Token
```
