function onLoad() {
    var url = new URL(window.location.href);
    var c = url.searchParams.get("page");
    console.log(c);
    if (c == "reload") {
        parent.location.reload();
    }
}