  // Auto close mobile sidebar when clicking nav links
    document.addEventListener('DOMContentLoaded', function() {
        const mobileNavLinks = document.querySelectorAll('#mobileSidebar .nav-link');
        const mobileSidebar = document.getElementById('mobileSidebar');
        
        mobileNavLinks.forEach(link => {
            link.addEventListener('click', function() {
                // Close the offcanvas when a nav link is clicked
                const offcanvasInstance = bootstrap.Offcanvas.getInstance(mobileSidebar);
                if (offcanvasInstance) {
                    offcanvasInstance.hide();
                }
            });
        });
    });