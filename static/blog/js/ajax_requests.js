//load more
$(document).ready(function() {

        $("#add-more-category").click(function(event){

        //console.log("ajax call");
         var page = $(this).attr("data-href"); // page
         var category = $(this).attr("name");
         var button = $(this);

        $.ajax({
        url: '/blog/add-posts/',
        dataType: 'json', // request type html/json/xml
        data: {'page':page,'category':category},
        beforeSend: function() {
                    button.html('Loading....'); // change submit button text
                },

         success: function(data) {
                    //console.log(data);
                    $("#more").append(data.posts);

                    if(data.has_next==true)
                    {
                        button.attr("data-href",data.next_page);
                        button.html('Load more..');
                    }
                    if(data.has_next==false)
                    {
                        button.hide();
                    }


        },
        error: function(e) {
                    console.log(e);
                }


      });
      });


      $("#add-more-author").click(function(event){

         var page = $(this).attr("data-href"); // page
         var author = $(this).attr("name");
         var button = $(this);

        $.ajax({

        url: '/blog/add-posts/',
        dataType: 'json', // request type html/json/xml
        data: {'page':page,'author':author},
        beforeSend: function() {

                    button.html('Loading...'); // change submit button text
                },

         success: function(data) {
                     $("#more").append(data.posts);
                    //console.log(data);
                    if(data.has_next==true)
                    {
                        button.attr("data-href",data.next_page);
                        button.html('Load more..');

                    }
                    if(data.has_next==false)
                    {
                        button.hide();
                    }

        },
        error: function(e) {
                    console.log(e);
                }


      });

});


$("#subscribe-btn").click(function(){



  var Email = $('#email-input').val();
  var csrftoken = $("[name=csrfmiddlewaretoken]").val();

  if ($.trim(Email).length == 0 ) {
        
        bootbox.alert({
    message: "All fields are mandatory",
    backdrop: true
     });

        e.preventDefault();
    }

        if (validateEmail(Email)) {
                $.ajax({
                url:'/blog/subscribe/',
                type:'POST',
                headers:{
                    "X-CSRFToken": csrftoken
               },
                dataType:'json',
                data: {'email':Email},
                success:function(data){
                    if(data.result){

                        thanks();
                    }
                    else if(data.result==false){
                        exists();
                    }

                },
                error:function(e){

                    console.log(e)
                }



                });
            }

        else {

             bootbox.alert({
           message: "Invalid email address",
           backdrop: true
          });
            e.preventDefault();
            }


});



$("#subscribe-btn-bottom").click(function(){
    


  var Email = $('#email-input-bottom').val();
  var csrftoken = $("[name=csrfmiddlewaretoken]").val();

  if ($.trim(Email).length == 0 ) {
        
         bootbox.alert({
    message: "All fields are mandatory",
    backdrop: true
     });
        e.preventDefault();
    }

        if (validateEmail(Email)) {
                $.ajax({
                url:'/blog/subscribe/',
                type:'POST',
                headers:{
                    "X-CSRFToken": csrftoken
               },
                dataType:'json',
                data: {'email':Email},
                success:function(data){
                    if(data.result){

                        thanks();
                    }
                    else if(data.result==false){
                        exists();
                    }

                },
                error:function(e){

                    console.log(e)
                }



                });
            }

        else {
            bootbox.alert({
           message: "Invalid email address",
           backdrop: true
          });
            e.preventDefault();
            }


});




});


 // Function that validates email address through a regular expression.
        function validateEmail(Email) {
        var filter = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/ ;
        if (filter.test(Email)) {
            return true;
                    }
            else {
                return false;
            }
         }


function thanks()
{

   
         bootbox.alert({
    message: "Thanks for subscribing",
    backdrop: true
     });


}

function exists()
{


         bootbox.alert({
    message: "You are already subscribed !!",
    backdrop: true
     });


}


