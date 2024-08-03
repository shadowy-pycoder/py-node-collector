# Python Node Collector

A python wrapper for [Prometheus Node Collector](https://github.com/shadowy-pycoder/go-node-collector) 

# Installation

```shell
pip install py-node-collector
```

# Usage


```python
from prometheus_client import parser
from py_node_collector import collector

metric = next(parser.text_string_to_metric_families(collector.collect()))
print(metric)
```

```shell
# Output
Metric(go_gc_duration_seconds, A summary of the pause duration of garbage collection cycles., summary, , 
[Sample(name='go_gc_duration_seconds', labels={'quantile': '0'}, value=0.0, timestamp=None, exemplar=None), 
Sample(name='go_gc_duration_seconds', labels={'quantile': '0.25'}, value=0.0, timestamp=None, exemplar=None), 
Sample(name='go_gc_duration_seconds', labels={'quantile': '0.5'}, value=0.0, timestamp=None, exemplar=None), 
Sample(name='go_gc_duration_seconds', labels={'quantile': '0.75'}, value=0.0, timestamp=None, exemplar=None), 
Sample(name='go_gc_duration_seconds', labels={'quantile': '1'}, value=0.0, timestamp=None, exemplar=None), 
Sample(name='go_gc_duration_seconds_sum', labels={}, value=0.0, timestamp=None, exemplar=None), 
Sample(name='go_gc_duration_seconds_count', labels={}, value=0.0, timestamp=None, exemplar=None)])
```