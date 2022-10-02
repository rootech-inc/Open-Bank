function swal_reload(message='')
{
    Swal.fire({

        icon: 'success',
        title: 'RELOAD',
        text:message,
        showDenyButton: false,
        showCancelButton: false,
        confirmButtonText: 'OK',
        denyButtonText: `Don't save`,
    }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
            location.reload()
        } else if (result.isDenied) {
            location.reload()
        }
    })
}

// process completed
function task_successful(message='Task completed successfully')
{
    Swal.fire({

        icon: 'success',
        text:message,
        showDenyButton: false,
        showCancelButton: false,
        confirmButtonText: 'OK',
        denyButtonText: `Don't save`,
    }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
            location.reload()
        } else if (result.isDenied) {
            location.reload()
        }
    })
}

// error handler
function error_handler(response)
{
    // split response
    if(response.split('%%').length === 2)
    {
        let response_split = response.split('%%');
        let response_type = response_split[0];
        let response_message = response_split[1];
        $('#gen_modal').modal('hide')
        // switching response type
        switch (response_type)
        {
            case 'error': // when the response type is an error

                switch (response_message) // switch between error message
                {
                    case "barcode_multiple_not_number": // item quantity is not a number
                        $('#general_input').addClass('bg-danger');
                        setTimeout(function (){$('#general_input').removeClass('bg-danger')},2000)
                        Swal.fire({
                            icon: 'error',
                            title: 'Oops...',
                            text: 'Quantity value must be a number',
                        })
                        break;
                    case 'item_does_not_exist':
                        swal_error("Item Not Found");
                        break;
                    case 'bill_recall_does_not_exits': // bill recall does not exist
                        swal_error("Bill does not exist")
                        $('#general_input').val('');
                        break;
                    case 'bill_not_on_hold':
                        swal_error("Bill is not on hold")
                        $('#general_input').val('');
                        break;
                    case 'no_clerk_account':
                        swal_error("Invalid Clerk or Key")
                        break;
                    case 'no_clerk_key':
                        swal_error("Invalid Key")
                        break;
                    default:
                        swal_error(response_message)
                }
                break;
            case 'done':
                switch (response_message) {
                    case 'done':
                        location.reload()
                        break;
                    case 'bill_added':
                        get_bill();
                        $('#general_input').val('');
                        // clear bill input
                        break;
                    case 'item_group_sub_added':

                        let parent = $('#sort_right').val();
                        loadCategory(parent);
                        break;
                    case 'prod_added':
                        location.reload();
                        break;
                    case 'done_reload':
                        swal_reload()
                        break;
                    default:
                        swal.fire(response_message);
                }
        }

    }
}