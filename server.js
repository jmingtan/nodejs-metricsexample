const express = require('express');
const metrics = require('metrics');

const app = express();
const metricsServer = new metrics.Server(9091);

const requests = new metrics.Timer();
metricsServer.addMetric('requests', requests);

app.get('/', (req, res) => {
    const start = Date.now();
    for (let i=0; i<1000; i++)
      res.write('Hello World!');
    res.end();
    console.log(Date.now() - start);
    requests.update(Date.now() - start);
});

app.listen(3000, () => {
    console.log('Example app listening on port 3000, metrics on :9091/metrics!');
});
