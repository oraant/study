#!/bin/bash
for i in `seq 100`; do
    echo -n "$i - "
    python ConcurrentLogHandler-multiprocess.py 50 >/dev/null && cat tmp.log |sort -Vu |wc -l
    sleep 1
done
