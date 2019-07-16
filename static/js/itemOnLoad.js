//function onLoad() {
//    var url = new URL(window.location.href);
//    var c = url.searchParams.get("page");
//    console.log(c);
//    if (c == "reload") {
//        parent.location.reload();
//    }
//}
function onLoad(view) {
    var url = new URL(window.location.href);
    var c = url.searchParams.get("id");
    if (c != undefined || c != null) {

        console.log(c);
        parent.location.href = "/" + view + "/?id=" + c;
    }
}