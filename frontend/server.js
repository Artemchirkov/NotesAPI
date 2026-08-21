const express = require('express');
const proxy = require('express-http-proxy');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(express.static(path.join(__dirname, 'public')));

// Проксируем все API запросы (включая /api/token/ и /api/notes/)
app.use('/api', proxy('http://127.0.0.1:8000', {
    proxyReqPathResolver: (req) => '/api' + req.url
}));

app.listen(PORT, () => {
    console.log(`🚀 JWT Фронтенд запущен: http://localhost:${PORT}`);
});