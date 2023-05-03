<script>
const clusterFilter = document.getElementById('cluster-filter');
const rows = document.querySelectorAll('table tbody tr');
const clusters = Array.from(new Set(Array.from(rows, row => row.querySelector('td:last-child').textContent)));

clusters.forEach(cluster => {
    const option = document.createElement('option');
    option.value = cluster;
    option.textContent = `Cluster ${cluster}`;
    clusterFilter.appendChild(option);
});

clusterFilter.addEventListener('change', () => {
    const selectedCluster = clusterFilter.value;
    rows.forEach(row => {
        if (selectedCluster === 'all' || row.querySelector('td:last-child').textContent === selectedCluster) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
});
</script>