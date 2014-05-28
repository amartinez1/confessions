
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
         $('.modal-title').html(data.fields.title+ " &nbsp <small id = "+data.fields.pk+"class ='badge count ' >"+data.fields.total_likes+" likes</small>");
         $('.modal-body').html('<h4>'+data.fields.text+"<h4>");
         $('.modal-footer').html("<button  id = 'button'"+data.fields.pk+"data-catid="+data.fields.pk+" class='btn btn-primary likes pull-left' type='button'>Like</button>"+
          

          "<button type='button' class='btn btn-default' data-dismiss='modal'>Close</button>"


            );
        }

      });

});

    // $('.')
  });