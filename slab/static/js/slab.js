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
