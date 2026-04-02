const API_URL = 'http://localhost:5000/health/status'; 

async function fetchHealth() {
    try {
        const res = await fetch(API_URL);
        const data = await res.json();
        renderDashboard(data);
    } catch (err) {
        document.getElementById('services-grid').innerHTML = '<p class="error">Erro ao conectar na API</p>';
        document.getElementById('overall-status').querySelector('.status-text').innerText = 'Offline';
        console.error(err);
    }
}

function renderDashboard(data) {
    // Status geral
    const overallCard = document.getElementById('overall-status');
    overallCard.querySelector('.status-text').innerText = data.overall === 'healthy' ? 'Saudável' : 'Degradado';
    overallCard.querySelector('.status-indicator').style.color = data.overall === 'healthy' ? 'green' : 'red';

    // Cards de serviços
    const grid = document.getElementById('services-grid');
    grid.innerHTML = '';
    data.services.forEach(s => {
        const card = document.createElement('div');
        card.className = 'service-card';
        card.innerHTML = `
            <h3>${s.service}</h3>
            <p>Status: <span class="${s.healthy ? 'healthy' : 'unhealthy'}">${s.healthy ? 'OK' : 'Falha'}</span></p>
            <p>Response Time: ${s.response_time_ms ?? 0} ms</p>
            ${s.status_code ? `<p>Status Code: ${s.status_code}</p>` : ''}
            ${s.error ? `<p>Erro: ${s.error}</p>` : ''}
        `;
        grid.appendChild(card);
    });

    renderCharts(data.services);
}

// SUBSTITUI por isso:
function renderCharts(services) {
    const labels = services.map(s => s.service);
    const responseTimes = services.map(s => s.response_time_ms ?? 0);
    const uptimes = services.map(s => s.healthy ? 100 : 0);

    updateCharts(labels, responseTimes, uptimes);
}

// Atualiza a cada 5 segundos
setInterval(fetchHealth, 5000);
fetchHealth();