var page = document.querySelector('.light-theme');

let button_theme = document.querySelector('.btn-01');
button_theme.onclick = function() {
    page.classList.toggle('light-theme');
    page.classList.toggle('dark-theme');
}

// Меню

document.getElementById('nav').onmouseover = function(event) {
    var target = event.target;
    if (target.className == 'menu-item') {
        var s = target.getElementsByClassName('submenu');
        closeMenu();
        s[0].style.display = 'block';
    }
}

document.onmouseover = function(event) {
    var target = event.target;
    console.log(event.target);
    if (target.className != 'menu-item' && target.className != 'submenu') {
        closeMenu();
    }
}

function closeMenu() {
    var menu = document.getElementById('nav');
    var subm = document.getElementsByClassName('submenu');
    for (var i=0; i < subm.length; i++) {
        subm[i].style.display='none';
    }
}
//Меню 2//
function openMenu() {
                document.getElementById("sidebar").classList.toggle('active');
                }