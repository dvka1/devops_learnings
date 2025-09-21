# Prometheus + Node Exporter + Grafana Setup (Docker)

# create docker network 
```
docker network create monitoring
```

# run node exporter

```
docker run -d \
  --name=node-exporter \
  --network=monitoring \
  -p 9100:9100 \
  prom/node-exporter
Exposes Linux system metrics (CPU, RAM, Disk, Network) on port 9100.

```
# run promethus container

```
docker run -d \
  --name=prometheus \
  --network=monitoring \
  -p 9090:9090 \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
Prometheus UI available at http://localhost:9090

Prometheus scrapes Node Exporter metrics every 5 seconds.

```
# run grafana container
```
docker run -d \
  --name=grafana \
  --network=monitoring \
  -p 3000:3000 \
  grafana/grafana
Grafana UI available at http://localhost:3000

Default login: admin / admin
```
# connect grafana to prometheus

##Connect Grafana to Prometheus

Open http://localhost:3000
 → Login

Go to Configuration → Data Sources → Add data source

Select Prometheus

Set URL:

http://prometheus:9090


Click Save & Test → should show Data source is working
##

# import node exporter dashboard

##
Click + → Import

Enter Dashboard ID: 1860

Select Prometheus as the data source → Click Import

Dashboard now displays CPU, RAM, Disk, Network metrics in real-time.
##

