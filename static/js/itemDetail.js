function detailItem(view, id) {
    document.getElementById('frame').src = '/' + view + '/' + id;

    document.getElementById("listGroup").childNodes.forEach(function(element) {
        element.className = 'list-group-item';
    });

    document.getElementById(id).className = 'list-group-item active';
}