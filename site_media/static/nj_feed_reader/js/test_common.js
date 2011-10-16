function test_string_to_date() {
    test_string_to_date_from_twitter()
    test_string_to_date_returns_date_with_same_string()
    test_precision_lost_when_call_string_to_date()
}

function test_compare_by_created_at() {
    test_compare_by_created_at_compares_according_to_created_at_property()
}

function test_empty_array() {
    test_empty_array_removes_all_elements()
}

function test_compare_by_created_at_compares_according_to_created_at_property() {
    msg = "compare_by_created_at should compare according to created_at property"
    first_item = {"created_at": new Date("22 May 2011 8:00")}
    second_item = {"created_at": new Date("22 May 2011 8:01")}
    result = compare_by_created_at(first_item, second_item) 
    jqUnit.ok(result > 0, msg)
}

function test_string_to_date_from_twitter() {
    msg =  "string_to_date should support date returned from twitter api (%s)"
    date_from_twitter = "Sun, 22 May 2011 11:10:27 +0000"

    actual = string_to_date(date_from_twitter).getTime()

    expected = new Date(date_from_twitter).getTime()
    jqUnit.ok(actual == expected, msg.replace("%s", date_from_twitter))
}

function test_string_to_date_returns_date_with_same_string() {
    msg =  "string_to_date(date_str).toString() should equal to date_str" 
    date_str = new Date().toString()

    actual = string_to_date(date_str).toString()

    jqUnit.ok(actual == date_str, msg)
}

function test_precision_lost_when_call_string_to_date() {
    today = new Date()
    date_str = today.toString()
    error_rate = 1000 // 1 sec lost should be ok

    returned_date = string_to_date(date_str)

    difference = Math.abs(returned_date - today)
    /*
    test below is to document that string_to_date is losing some precision
    but it not necessary that it should do. Feel free to remove the line below
    if the implementation of string_to_date is improved.

    juacompe (May 22, 2011)
    */
    jqUnit.ok(difference > 0, "string_to_date lose some precision")
    jqUnit.ok(difference < error_rate, "precision lost less than 1000 millisecs")
}

function test_empty_array_removes_all_elements() {
    a = ['a', 'b', 'c']
    empty_array(a)
    jqUnit.ok(a.length == 0)
}

