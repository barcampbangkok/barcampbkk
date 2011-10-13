function string_to_date(string) {
    return new Date(string);
}

function compare_by_created_at(a, b) {
    return a.created_at < b.created_at;
}

