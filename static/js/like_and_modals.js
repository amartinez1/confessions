
	$(document).ready
    (function()
      {


    $('.likes').click(function() {
      
      var catid;
      catid = $(this).attr("data-catid");

      console.log("catid = "+catid);
      $.ajax({
        data:{'confession_id':catid},
        url: '/like/',
        type:'get',
        success: function(data){
          $('#'+catid).html(data.count);
          $('#button'+catid).html(data.label);
        }

      });

});
          $('.post').click(function() {
      var catid;
      catid = $(this).attr("data-catid");
      console.log("catid = "+catid);
      $.ajax({
        data:{'id':catid},
        url: '/fill/',
        type:'get',
        success: function(data){
          console.log("confirming id "+ data.pk);
         $('.modal-title').html(data.fields.title+ " &nbsp <small id = "+data.pk+"class ='badge count ' >"+data.fields.total_likes+" likes</small>");
         $('.modal-body').html("<h4 class='justified'>"+data.fields.text+"<h4>");
         $('.modal-footer').html(
          // "<button  id = 'button'"+data.pk+"&nbsp data-catid="+data.pk+" class='btn btn-primary likes pull-left' type='button'>Like</button>"+
          

          "<button type='button' class='btn btn-default' data-dismiss='modal'>Close</button>"


            );
        }

      });

});

    // $('.')
  });