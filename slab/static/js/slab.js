var main_url = location.protocol+'//'+location.hostname+(location.port ? ':'+location.port: '');

$( document ).ready( function(){
  console.log(main_url);
  $.ajax({
    url:main_url+"/get_slab_data/",
    method:"get",
    datatype:"application/json",
    data:"",
    success: function(data){
      console.log(data);
      for (var i=0; i< data.length; i++){
        var x = document.getElementById("id_comm_data");
        var choices = document.createElement('option');
        choices.text = data[i]['slab'];
        choices.value = data[i]['id'];
        x.add(choices);

        var x = document.getElementById("id_comm_type");
        var choices = document.createElement('option');
        choices.text = data[i]['slab'];
        choices.value = data[i]['id'];
        x.add(choices);
      }
      get_data_ajax(1);
    }
  });

  $("#id_comm_data").on('change', function(){
    var selected = $(this).children("option:selected").val()
    $('#id_comm_type').val(selected);
    get_data_ajax(selected)
  });

  $("#id_post_create").on('click', function(){
    var data = {}
    data['dist_id'] = $("#dist_id").val();
    data['slab'] = $("#id_comm_data").val();
    data['z_comm'] = $("#id_zrupee_comm").val();
    data['c_comm'] = $("#id_dist_comm").val();
    data['m_comm'] = $("#id_marchent_comm").val();
    data['tds'] = $("#id_tds_comm").val();
    data['gst'] = $("#id_gst").val();
    data['cust_fee'] = $("#id_cust_fee").val()

    var token = '{{csrf_token}}';
    var form = $(this).closest("form");

    $.ajax({
      url:main_url+"/post_create/",
      method: "post",
      data:data,
      success: function(data){
        console.log("Data sent successfully.");
        alert("Data saved successfully!");
      }
    });
  });

  $("#dist_id").on('change', function(){
      var d = $("#dist_id").val()
      $("#id_dists").val(d);
  });

  $(".change").bind('keyup mouseup', function () {
    console.log(this.id);
    if (this.id == "id_zrupee_comm"){
      var v = $("#"+this.id).val();
      var m_data = 100-v;
      console.log(m_data);
      $("#id_marchent_comm").val('');
      $("#id_marchent_comm").val(m_data-19);
    } else if(this.id == "id_marchent_comm") {
      var v = $("#"+this.id).val();
      var m_data = 100-v;
      console.log(m_data);
      $("#id_zrupee_comm").val('');
      $("#id_zrupee_comm").val(m_data-19);
    }

  });
});

function get_data_ajax(selected){
  $.ajax({
    url: main_url+"/get_selected_data/",
    method: "get",
    data: {"data":selected},
    success: function(data){
      data = data['data']
      for (var i=0; i<data.length; i++){
        var keyy = data[i]['comm']
        if (keyy == 'Zurupee Commission'){
          $("#id_zrupee_comm").val(data[i]['share']);
        } else if (keyy == "Distributer Commission"){
          $("#id_dist_comm").val(data[i]['share']);
        } else if (keyy == "Marchant Commission"){
          $("#id_marchent_comm").val(data[i]['share']);
        }
      }
    }
  });
}
