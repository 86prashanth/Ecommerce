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
        
        if(fname== " " || lname== "" || email == "" || phone== "" || address=="" || city=="" ||state=="" ||country=="" ||pincode=="")
        {
            swal('Alert!',"All fields are mandatory","warning");
            return false;
        }
        else{
            $.ajax({
                method:"GET",
                url: "/proceed-to-pay/",
                success: function (response) {
                    var options = {
                        "key": "rzp_test_peAOxXTKroZdOB", // Enter the Key ID generated from the Dashboard
                        "amount": 1*100,
                        // "amount": response.total_price * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "Developer", //your business name
                        "description": "Thank you for buying from us",
                        "image": "https://example.com/your_logo",
                            //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (responsed){
                        alert(responsed.razorpay_payment_id);
                            
                            // var fname=$("[name='fname']").val();
                            // var lname=$("[name='lname']").val();
                            // var email=$("[name='email']").val();
                            // var phone=$("[name='phone']").val();
                            // var address=$("[name='address']").val();
                            // var city=$("[name='city']").val();
                            // var state=$("[name='state']").val();
                            // var country=$("[name='country']").val();
                            // var pincode=$("[name='pincode']").val();
                            // var token=$("[name='csrfmiddlewaretoken']").val();

                            data={
                                "fname":fname,
                               "lname":lname,
                               "email":email,
                                "phone":phone,
                                "address":address,
                                "city":city,
                               "state":state,
                                "country":country,
                                "pincode":pincode,
                                "payment_mode":"Paid by Razorpay",
                                "payment_id":responsed.razorpay_payment_id,
                                csrfmiddlewaretoken: token
                            }
                            $.ajax({
                                method: "POST",
                                url: "/place-order/",
                                data: data,
                                success: function (responsec) {
                                    swal("Congratualtion!", responsec.status, "success").then((value) => {
                                        window.location.href='/my-order/'
                                });
                            }
                        });
                        },
                        "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information, especially their phone number
                                "name": fname+" "+lname, //your customer's name
                                "email": email,
                                "contact": phone  //Provide the customer's phone number for better conversion rates 
                            },
                            "theme": {
                                "color": "#3399cc"
                            }
                        };
                        var rzp1 = new Razorpay(options);
                        rzp1.open();
                    }// console.log(response)
                
            });
         
        }
    });
});
