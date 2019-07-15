function clickItem(view) {
    var url = new URL(window.location.href);
    if (url.searchParams.get("id") !== undefined || url.searchParams.get("id") !== null) {
        var c = url.searchParams.get("id");
        console.log(c);
        document.getElementById(c).click();
        ChangeUrl("", "/" + view + "/")
    }
}

function ChangeUrl(title, url) {
    if (typeof (history.pushState) != "undefined") {
        var obj = { Title: title, Url: url };
        history.pushState(obj, obj.Title, obj.Url);
    } else {
        alert("Browser does not support HTML5.");
    }
}