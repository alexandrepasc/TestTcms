function newItem(view) {
    document.getElementById('frame').src = '/' + view + '/';

    document.getElementById("listGroup").childNodes.forEach(function(element) {
        element.className = 'list-group-item';
    });
}