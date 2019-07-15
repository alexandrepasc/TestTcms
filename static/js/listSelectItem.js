function clickItem() {
    var url = new URL(window.location.href);
    if (typeof url.searchParams.get("id") !== 'undefined') {
        var c = url.searchParams.get("id");
        console.log(c);
        document.getElementById(c).click();
    }
}