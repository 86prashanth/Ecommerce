$(document).ready(function () {
    $('.paywithRazorpay').click(function (e) {
        e.preventDefault();
        var fname=$("[name='fname']").val();
        var lname=$("[name='lname']").val();
        var email=$("[name='email']").val();
        var phone=$("[name='phone']").val();
        var address=$("[name='address']").val();
        var city=$("[name='city']").val();
        var state=$("[name='state']").val();
        var country=$("[name='country']").val();
        var pincode=$("[name='pincode']").val();
        var token=$("[name='csrfmiddlewaretoken']").val();

        if(fname==""|| lname=="" || email=="" || phone=="" || address=="" || state=="" || country=="" ||pincode=="")
        {
            swal("Alert","all fields are mandatary!","warning")
            return false;
        }
        else{
            $.ajax({
                method:'GET',
                url:'/process-to-pay',
                success:function(response){
                    console.log(response);
                }
            });
            var options = {
                "key": "rzp_test_peAOxXTKroZdOB", // Enter the Key ID generated from the Dashboard
                "amount": 1*100, // response.total_price * 100, Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                "currency": "INR",
                "name": "Apna shopping Apna Barosa",
                "description": "Thank you for buying with us",
                "handler":function (responseb)
                {
                    alert(responseb.razorpay_payment_id);
                    data={
                        "fname":fname,
                        "lname":lname,
                        "email":email,
                        "phone":phone,
                        "city":city,
                        "state":state,
                        "country":country,
                        "pincode":pincode,
                        "payment_mode":"Razorpay",
                        "payment_id":"responseb.razorpay_payment_id",
                        csrfmiddlewaretoken: token
                    }
                    $.ajax({
                        method:"POST",
                        url:"/placeorder",
                        data: data,
                        success: function(feedback) {
                            swal("Congratulations","your order has been added successfully","success").then((value) =>{
                                window.location.href="/myorders"
                            });
                        }
                    });
                },
                "prefill": {
                    "name": fname+" "+lname,
                    "email": email,
                    "contact":phone,
                },
                "theme": {
                    "color": "#3399cc"
                }
            };
            var razp1=new Razorpay(options);
            razp1.open();
        }
       
    });
});