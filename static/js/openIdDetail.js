function overItem(id) {
    document.getElementById(id).style.cursor = 'pointer';
    document.getElementById(id).style.color = '#FFFFFF';
    document.getElementById(id).style.background = '#007bff';
}

function outItem(id) {
    document.getElementById(id).style.color = '#000000';
    document.getElementById(id).style.background = '#FFFFFF';
    document.getElementById(id).style.cursor = 'pointer';
}