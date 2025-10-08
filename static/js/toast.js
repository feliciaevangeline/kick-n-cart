function showToast(title, message, type = 'info', duration = 3000) {
    const toast = document.getElementById('toast-component');
    const titleElem = document.getElementById('toast-title');
    const messageElem = document.getElementById('toast-message');
    const iconElem = document.getElementById('toast-icon');

    if (!toast) return;

    // Reset style
    toast.classList.remove(
        'border-[#2E4365]', 'border-green-600', 'border-red-600', 
        'bg-[#EBDDC5]', 'bg-green-50', 'bg-red-50'
    );

    let icon = '';
    if (type === 'success') {
        toast.classList.add('bg-green-50', 'border-green-600');
        icon = '✅';
    } else if (type === 'error') {
        toast.classList.add('bg-red-50', 'border-red-600');
        icon = '❌';
    } else {
        toast.classList.add('bg-[#EBDDC5]', 'border-[#2E4365]');
        icon = 'ℹ️';
    }

    // Isi konten
    titleElem.textContent = title;
    messageElem.textContent = message;
    iconElem.textContent = icon;

    toast.classList.remove('opacity-0', 'scale-90');
    toast.classList.add('opacity-100', 'scale-100');

    // Hilang setelah beberapa detik
    setTimeout(() => {
        toast.classList.remove('opacity-100', 'scale-100');
        toast.classList.add('opacity-0', 'scale-90');
    }, duration);

    function getCSRFToken() {
    const name = 'csrftoken';
    const cookie = document.cookie.split('; ').find(row => row.startsWith(name + '='));
    return cookie ? decodeURIComponent(cookie.split('=')[1]) : '';
    }

}
