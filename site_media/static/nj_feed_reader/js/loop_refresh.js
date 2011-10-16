function delayed_refresh() {
    var ten_minutes = 1000 * 60 * 10
    // setTimeout can't be used in a loop
    setTimeout(refresh, ten_minutes)
}

function refresh() {
   window.location = '.'
   delayed_refresh() // loop it
}
