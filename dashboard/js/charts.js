const responseTimeChartCtx = document.getElementById('responseTimeChart').getContext('2d');
const uptimeChartCtx = document.getElementById('uptimeChart').getContext('2d');

let responseTimeChart = new Chart(responseTimeChartCtx, {
    type: 'bar',
    data: { labels: [], datasets: [{ label: 'Response Time (ms)', data: [], backgroundColor: 'rgba(54, 162, 235, 0.6)' }] },
    options: { scales: { y: { beginAtZero: true } } }
});

let uptimeChart = new Chart(uptimeChartCtx, {
    type: 'bar',
    data: { labels: [], datasets: [{ label: 'Uptime (%)', data: [], backgroundColor: 'rgba(75, 192, 192, 0.6)' }] },
    options: { scales: { y: { beginAtZero: true, max: 100 } } }
});

function updateCharts(labels, responseTimes, uptimes) {
    responseTimeChart.data.labels = labels;
    responseTimeChart.data.datasets[0].data = responseTimes;
    responseTimeChart.update();

    uptimeChart.data.labels = labels;
    uptimeChart.data.datasets[0].data = uptimes;
    uptimeChart.update();
}