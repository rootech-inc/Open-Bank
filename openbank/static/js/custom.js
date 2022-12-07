function transaction() {
    // validate inputs
    let from,to,amt
    from = $('#from')
    to = $('#to')
    amt = $('#amt')

    if(from.val() || to.val() == '0')
    {
        Swal.fire("Please Select Account")
    } else if(amt.val() < 1)
    {
        Swal.fire('Invalid Amount')
    } els
    {
        // submit form
    }
}
