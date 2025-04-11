const loader_container = document.querySelector('.loader-container');
const loader = document.querySelector('.loader');

function hideLoader() {
    if (loader_container) {
        loader_container.style.opacity = 0;
        setTimeout(() => {
            loader_container.style.display = 'none';
        }, 500)
    }
}


window.addEventListener('pageshow', () => {
    setTimeout(hideLoader, 500);
});

window.addEventListener('beforeunload', () => {
    loader_container.style.display = 'flex';
    loader_container.style.opacity = 1;
});