const params = new URLSearchParams(window.location.search);
const page = parseInt(params.get('page'), 10);
console.log('page:', page);

if (page > 0 && page <= navItems.length) {
    navItems.item(page).click();
}
