document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('scanForm');
    const loading = document.getElementById('loading');

    form.addEventListener('submit', function() {
        loading.style.display = 'block';
    });
});
